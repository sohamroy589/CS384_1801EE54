import os
import csv
import re
import shutil

def create_grades_folder():
    os.chdir(r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment4')
    if os.path.exists('grades'):
        shutil.rmtree('grades', ignore_errors=True)
    os.mkdir('grades')

def create_individual():
    with open('acad_res_stud_grades.csv', 'r') as rfile:
        reader = csv.DictReader(rfile, skipinitialspace=True)
        os.chdir('grades')
        fieldnames = ['Subject', 'Credits', 'Type', 'Grade', 'Sem']
        columns = ['sub_code', 'total_credits', 'sub_type', 'credit_obtained', 'sem']
        for row in reader:
            roll = row['roll']
            filename = ''
            if re.match(r'\d{4}[a-zA-Z]{2}\d{2}', roll):
                filename = roll + '_individual.csv'
            else:
                filename = 'misc_individual.csv'
            if not os.path.exists(filename):
                with open(filename, 'a', newline='') as wfile:
                    if filename != 'misc_individual.csv': 
                        title_writer = csv.writer(wfile)
                        title_writer.writerows([['Roll: ' + roll], ['Semester Wise Details']])
                    writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                    writer.writeheader()
            with open(filename, 'a', newline='') as wfile:
                writer = csv.DictWriter(wfile, fieldnames=fieldnames)
                new_row = {}
                for i in range(len(columns)):
                    new_row[fieldnames[i]] = row[columns[i]]
                writer.writerow(new_row)

def result_generator():
    create_grades_folder()
    create_individual()

if __name__ == '__main__':
    result_generator()