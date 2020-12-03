import os
import time
import csv
import re
import threading
import keyboard
from Question import question

user_input = None
home = os.getcwd()

def get_user_input():
    global user_input
    user_input = input()

class quiz():
    def __init__(self, q_name, name, roll):
        self.participant = {
            'name' : name,
            'roll_no': roll
        }
        self.total_quiz_marks = 0
        self.correct = 0
        self.unattempted = []
        self.questions = self.set_questions(q_name)
        self.marks = 0
        self.show_unattempted = False
        keyboard.add_hotkey('ctrl+alt+u', self.show_una)
        keyboard.add_hotkey('ctrl+alt+g', self.goto_q)
        keyboard.add_hotkey('ctrl+alt+f', self.final_sub)
        self.cur_question = None
        self.response = {}
        self.ask = False
        self.final_submit = False
        self.name = q_name.rstrip('.csv')

    def final_sub(self):
        self.final_submit = True
        t1 = threading.Thread(target=get_user_input)
        t1.start()

    def show_una(self):
        self.show_unattempted ^= True
    
    def record_resp(self, response):
        if response != 's':
            self.response[self.cur_question.no] = response
            if self.cur_question.no in self.unattempted:
                self.unattempted.remove(self.cur_question.no)
        self.cur_question = None

    def get_resp(self):
        t1 = threading.Thread(target=get_user_input)
        t1.start()

    def goto_q(self):
        self.ask = True
        t1 = threading.Thread(target=get_user_input)
        t1.start()
    
    def display(self):
        global user_input
        os.system('cls')
        print('*'*20 + '|| Quiz ||' + '*'*20)
        print('Timer: {:02d} : {:02d}'.format(int(self.timer) // 60, int(self.timer) % 60))
        print('Roll:', self.participant['roll_no'])
        print('Name:', self.participant['name'])
        if self.final_submit:
            print('Do you want to finish?\nEnter \'yes\' to final submit.')
            resp = None
            if user_input:
                resp = user_input.strip().lower()
                if resp == 'yes':
                    self.timer = 0
                self.final_submit = False
            user_input = None
        else:
            print('Press Ctrl+Alt+F to finish the quiz')
            if not self.show_unattempted:
                print('Press Ctrl+Alt+U to see the unattempted questions')
            else:
                print('Unattempted Questions - ', end=' ')
                for q in self.unattempted:
                    print(q, end=' ')
                print()
            if self.cur_question:
                self.show_question()
                # self.get_resp()
                if user_input:
                    response = user_input.strip().lower()
                    user_input = None
                    self.record_resp(response)
            elif self.ask:
                print('Enter the question number..')
                if user_input:
                    try:
                        self.cur_question = self.questions[user_input.strip()]
                        self.get_resp()
                        self.ask = False
                    except:
                        print('Invalid question number!')
                        user_input = None
                        self.goto_q()
                    user_input = None
            else:
                print('Press Ctrl+Alt+G to go to any question')

    
    def show_question(self):
        print(self.cur_question.no + ')', self.cur_question.statement)
        for opt, val in self.cur_question.option.items():
            print("Option " + opt + ')', val)
        print()
        print('Credits if Correct Option:', self.cur_question.correct_marks)
        print('Negative Marking:', self.cur_question.wrong_marks)
        print('Is compulsory:', 'Yes' if self.cur_question.is_compulsory else 'No', '\n')
        print('Enter Choice:', end=' ')
        for opt in self.cur_question.option.keys():
            print(opt, end=', ')
        print('S: S is to skip question')
    
    def set_questions(self, q_name):
        q_list = {}
        with open(os.path.join(os.getcwd(), 'quiz_wise_questions', q_name), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                q_list[row['ques_no']] = question(row)
                self.unattempted.append(row['ques_no'])
                self.total_quiz_marks += int(row['marks_correct_ans'])
            tstring = reader.fieldnames[-1]
            h_match = re.search(r'\d+(?=h)', tstring)
            m_match = re.search(r'\d+(?=m)', tstring)
            hh, mm = 0, 0
            if h_match:
                hh = int(h_match.group())
            if m_match:
                mm = int(m_match.group())
            self.timer = 60 * (mm + hh * 60)
        return q_list

    def result_calculate(self):
        for q, res in self.response.items():
            if self.questions[q].answer == res:
                self.marks += self.questions[q].correct_marks
                self.correct += 1
            else:
                self.marks += self.questions[q].wrong_marks
        for q in self.unattempted:
            if self.questions[q].is_compulsory:
                self.marks += self.questions[q].wrong_marks
    
    def export(self):
        # Export into the database
        filename = self.name + '_' + self.participant['roll_no'] + '.csv'
        path = os.path.join(os.getcwd(), 'individual_responses', filename)
        if os.path.exists(path):
            os.remove(path)
        with open(path, 'a', newline='') as f:
            with open(os.path.join(os.getcwd(), 'quiz_wise_questions', self.name+'.csv'), 'r') as rf:
                reader = csv.DictReader(rf)
                fieldnames = reader.fieldnames
                fieldnames += ['marked_choice', 'Total', 'Legend']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                cnt = 1
                for row in reader:
                    new_row = row.copy()
                    new_row['marked_choice'] = self.response.get(row['ques_no'])
                    if cnt == 1:
                        new_row['Legend'] = 'Correct Choices'
                        new_row['Total'] = self.correct
                    elif cnt == 2:
                        new_row['Legend'] = 'Wrong Choices'
                        new_row['Total'] = len(self.questions) - self.correct - len(self.unattempted)
                    elif cnt == 3:
                        new_row['Legend'] = 'Unattmepted'
                        new_row['Total'] = len(self.unattempted)
                    elif cnt == 4:
                        new_row['Legend'] = 'Marks Obtained'
                        new_row['Total'] = self.marks
                    elif cnt == 5:
                        new_row['Legend'] = 'Total Quiz Marks'
                        new_row['Total'] = self.total_quiz_marks
                    writer.writerow(new_row)
                    cnt += 1
                while cnt <= 5:
                    new_row = {}
                    if cnt == 1:
                        new_row['Legend'] = 'Correct Choices'
                        new_row['Total'] = self.correct
                    elif cnt == 2:
                        new_row['Legend'] = 'Wrong Choices'
                        new_row['Total'] = len(self.questions) - self.correct - len(self.unattempted)
                    elif cnt == 3:
                        new_row['Legend'] = 'Unattmepted'
                        new_row['Total'] = len(self.unattempted)
                    elif cnt == 4:
                        new_row['Legend'] = 'Marks Obtained'
                        new_row['Total'] = self.marks
                    elif cnt == 5:
                        new_row['Legend'] = 'Total Quiz Marks'
                        new_row['Total'] = self.total_quiz_marks
                    writer.writerow(new_row)
                    cnt += 1

    def run(self):
        while self.timer > 0:
            self.display()
            time.sleep(1)
            self.timer -= 1
        os.system('cls')
        print("Quiz is done!")
        self.result_calculate()
        self.export()
        print('Press Ctrl+Alt+E to export the results to csv within 5 seconds')
    
if __name__ == '__main__':
    q = quiz('quiz_question.csv')
    q.run()