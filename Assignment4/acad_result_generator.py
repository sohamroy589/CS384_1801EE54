import os
import csv
import re
import shutil

# Global variable to store the current working directory
home = r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment4'
# Name of the input file
input_file = 'acad_res_stud_grades.csv'
# Grade Numeric Equivalent
grade = {
    'AA': 10,
    'AB': 9,
    'BB': 8,
    'BC': 7,
    'CC': 6,
    'CD': 5,
    'DD': 4,
    'F': 0,
    'I': 0
}
# Deletes the previous grades folder and creates a new one
def create_grades_folder():
    os.chdir(home)
    if os.path.exists('grades'):
        shutil.rmtree('grades', ignore_errors=True)
    os.mkdir('grades')

# Function for creating individual results for each student
def create_individual():
    with open(input_file, 'r') as rfile:
        reader = csv.DictReader(rfile, skipinitialspace=True)
        os.chdir('grades')
        columns = ['sub_code', 'total_credits', 'sub_type', 'credit_obtained', 'sem']
        for row in reader:
            fieldnames = ['Subject', 'Credits', 'Type', 'Grade', 'Sem'] 
            roll = row['roll']
            filename = ''
            if re.match(r'\d{4}[a-zA-Z]{2}\d{2}', roll):
                filename = roll + '_individual.csv'
            else:
                filename = 'misc.csv'
            if not(row['total_credits'] and row['credit_obtained'].upper() in grade.keys() and 1 <= int(row['sem']) <= 8):
                filename = 'misc.csv'
            if filename == 'misc.csv':
                fieldnames = list(row.keys())
            if not os.path.exists(filename):
                with open(filename, 'a', newline='') as wfile:
                    if filename != 'misc.csv': 
                        title_writer = csv.writer(wfile)
                        title_writer.writerows([['Roll: ' + roll], ['Semester Wise Details']])
                    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                    writer.writeheader()
            with open(filename, 'a', newline='') as wfile:
                writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                if filename != 'misc.csv':
                    new_row = {}
                    for i in range(len(columns)):
                        new_row[fieldnames[i]] = row[columns[i]]
                    writer.writerow(new_row)
                else:
                    writer.writerow(row)

# This function creates the overall result for each student but it should not be called before the create_individual() function
def create_overall():
        # os.chdir('grades')
        for rfile_name in os.listdir(os.getcwd()):
            if rfile_name == 'misc.csv':
                continue
            info = [{'Semester': i, 'Semester Credits': 0, 'Semester Credits Cleared': 0, 'SPI': 0, 'Total Credits': 0, 'Total Credits Cleared': 0, 'CPI': 0} for i in range(0, 9)]
            filename = ''
            total_sem = 9
            with open(rfile_name, 'r') as rfile:
                reader = csv.DictReader(rfile, fieldnames=['Subject', 'Credits', 'Type', 'Grade', 'Sem'])
                roll = rfile_name.split('_')[0]
                fieldnames = list(info[0].keys())
                filename = roll + '_overall.csv'
                next(reader)
                next(reader)
                next(reader)
                for row in reader:
                    # print(row)
                    sem = int(row['Sem'])
                    info[sem]['Semester Credits'] += int(row['Credits'])
                    info[sem]['Total Credits'] += int(row['Credits'])
                    if (grade[row['Grade']] > 0):
                        info[sem]['Semester Credits Cleared'] += int(row['Credits'])
                        info[sem]['Total Credits Cleared'] += int(row['Credits'])
                        info[sem]['SPI'] += grade[row['Grade']] * int(row['Credits'])
            for sem in range(1, 9):
                if info[sem]['Semester Credits'] == 0:
                    total_sem = sem
                    break
                info[sem]['Total Credits'] += info[sem-1]['Total Credits']
                info[sem]['Total Credits Cleared'] += info[sem-1]['Total Credits Cleared']
                info[sem]['CPI'] = (info[sem-1]['CPI'] * info[sem-1]['Total Credits'] + info[sem]['SPI']) / info[sem]['Total Credits']
                info[sem]['SPI'] /= info[sem]['Semester Credits']
            for sem in range(1, total_sem):
                info[sem]['SPI'] = round(info[sem]['SPI'], 2)
                info[sem]['CPI'] = round(info[sem]['CPI'], 2)
            if not os.path.exists(filename):
                with open(filename, 'a', newline='') as wfile:
                    if filename != 'misc_overall.csv': 
                        title_writer = csv.writer(wfile)
                        title_writer.writerow(['Roll: ' + roll])
                    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                    writer.writeheader()

            with open(filename, 'a', newline='') as wfile:
                writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                writer.writerows(info[1:total_sem])

# Function for generating the result
def result_generator():
    create_grades_folder()
    create_individual()
    create_overall()
    os.chdir(home)

if __name__ == '__main__':
    result_generator()