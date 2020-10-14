import csv
import os
import re

def return_to_assignment3():
    os.chdir(r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment3')

#Function for checking Pre-existing files and adding the header accordingly
def check_pre_existing_file(filename, fieldnames):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()

def course():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.DictReader(file)
        cur_path = os.path.join(os.getcwd(), r'analytics\course')
        # print(cur_path)
        os.chdir(r'analytics\course')
        # print(os.getcwd())
        course_name = {'01' : 'btech', '11' : 'mtech', '12' : 'msc', '21' : 'phd'}
        for row in reader:
            roll_no = row['id']
            cur_filename = ''
            try:
                branch_name = roll_no[4:6].lower()
                if re.match("\d\d\d\d[A-Z][A-Z]\d\d", roll_no):
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
            check_pre_existing_file(cur_filename, fieldnames)
            with open(cur_filename, 'a', newline = '') as w_file:
                writer = csv.DictWriter(w_file, fieldnames = fieldnames)
                writer.writerow(row)
            os.chdir(cur_path)


def country():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        os.chdir(r'analytics\country')
        cur_path = os.getcwd()
        
        reader = csv.DictReader(file)
        for row in reader:
            cur_country = row['country']
            filename = cur_country + '.csv'
            if not re.match("\D+", cur_country):
                filename = 'misc.csv'

            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)

            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames=fieldnames)
                writer.writerow(row)
            
            os.chdir(cur_path)


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