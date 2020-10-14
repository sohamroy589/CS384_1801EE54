import csv
import os
import re

#This Function sets the current working directory to Assignment3
def return_to_assignment3():
    os.chdir(r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment3')

def create_directory(name):
    os.chdir('analytics')
    if not os.path.exists(name):
        os.mkdir(name)

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
        create_directory('course')
        os.chdir('course')
        cur_path = os.getcwd()
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
        create_directory('country')
        os.chdir('country')
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
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        reader = csv.DictReader(file)
        create_directory('email_domain')
        os.chdir('email_domain')
        cur_path = os.getcwd()
        
        for row in reader:
            domain = re.search("(?<=@)[^.]+(?=\.)", row['email'])
            filename = ''
            if domain:
                filename = domain.group() + '.csv'
            else:
                filename = 'misc.csv'
            
            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)
            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames = fieldnames)
                writer.writerow(row)
            os.chdir(cur_path)


def gender():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        create_directory('gender')
        os.chdir('gender')
        cur_path = os.getcwd()
        
        reader = csv.DictReader(file)
        for row in reader:
            cur_gender = row['gender'].lower()
            filename = cur_gender + '.csv'
            if cur_gender not in ('male', 'female'):
                filename = 'misc.csv'

            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)

            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames=fieldnames)
                writer.writerow(row)
            
            os.chdir(cur_path)


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