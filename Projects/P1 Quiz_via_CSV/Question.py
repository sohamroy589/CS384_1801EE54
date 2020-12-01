class question():
    def __init__(self, description):    
        self.statement = description['question']
        self.option = {'1':description['option1'], '2':description['option2'], '3':description['option3'], '4':description['option4']}
        self.answer = description['correct_option']
        self.correct_marks = int(description['marks_correct_ans'])
        self.wrong_marks = int(description['marks_wrong_ans'])
        self.is_compulsory = description['compulsory'] == 'y'
        self.no = description['ques_no']