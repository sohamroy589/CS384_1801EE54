import csv
import os


def course():
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.DictReader(file)
        cur_path = os.path.join(os.getcwd(), r'analytics\course')
        # print(cur_path)
        os.chdir(r'analytics\course')
        # print(os.getcwd())
        course_name = {'01' : 'btech', '11' : 'mtech', '12' : 'msc', '21' : 'phd'}
        branches = ['cs', 'ee', 'me', 'cb', 'ce']
        for row in reader:
            roll_no = row['id']
            cur_filename = ''
            try:
                branch_name = roll_no[4:6].lower()
                if branch_name in branches:
                    if not os.path.exists(branch_name):
                        os.mkdir(branch_name)
                    os.chdir(branch_name)
                    course = course_name[roll_no[2:4]]
                    if not os.path.exists(course):
                        os.mkdir(course)
                    os.chdir(course)
                    cur_filename = roll_no[:2] + '_' + branch_name + '_' + course_name[roll_no[2:4]] + '.csv'
                else:
                    cur_filename = 'misc.csv'
            except:
                os.chdir(cur_path)
                cur_filename = 'misc.csv'

        
            fieldnames = list(row.keys())
            # print(fieldnames)
            if not os.path.exists(cur_filename):
                with open(cur_filename, 'w', newline='') as w_file:
                    writer = csv.DictWriter(w_file, fieldnames = fieldnames)
                    writer.writeheader()
            with open(cur_filename, 'a', newline = '') as w_file:
                writer = csv.DictWriter(w_file, fieldnames = fieldnames)
                writer.writerow(row)
            os.chdir(cur_path)


def country():
    # Read csv and process
    pass


def email_domain_extract():
    # Read csv and process
    pass


def gender():
    # Read csv and process
    pass


def dob():
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass