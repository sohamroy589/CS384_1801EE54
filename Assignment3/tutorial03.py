import csv
import os
import re
import shutil

#This Function sets the current working directory to Assignment3
def return_to_assignment3():
    os.chdir(r'C:\Users\hp\Desktop\CS384_1801EE54\Assignment3')

#This function creates corresponding directories when other functions are called
def create_directory(name):
    os.chdir('analytics')
    if os.path.exists(name):
        shutil.rmtree(name, ignore_errors=True)
    os.mkdir(name)

#Function for checking Pre-existing files and adding the header accordingly
def check_pre_existing_file(filename, fieldnames):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()

def del_create_analytics_folder():
    return_to_assignment3()
    if os.path.exists('analytics'):
        shutil.rmtree('analytics', ignore_errors=True)
    os.mkdir('analytics')

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
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        create_directory('dob')
        os.chdir('dob')
        cur_path = os.getcwd()

        reader = csv.DictReader(file)
        for row in reader:
            cur_dob = row['dob']
            ddmmyy = re.split('[/-]', cur_dob)
            try:
                date = int(ddmmyy[0])
                month = int(ddmmyy[1])
                year = int(ddmmyy[2])
                if 1995 <= year <= 1999:
                    filename = 'bday_1995_1999.csv'
                elif 2000 <= year <= 2004:
                    filename = 'bday_2000_2004.csv'
                elif 2005 <= year <= 2009:
                    filename = 'bday_2005_2009.csv'
                elif 2010 <= year <= 2014:
                    filename = 'bday_2010_2014.csv'
                elif 2015 <= year <= 2020:
                    filename = 'bday_2015_2020.csv'
                else:
                    filename = 'misc.csv'
                if not (1 <= date <= 31) or not (1 <= month <= 12):
                    filename = 'misc.csv'
            except:
                filename = 'misc.csv'
            
            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)

            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames)
                writer.writerow(row)

        os.chdir(cur_path)


def state():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        create_directory('state')
        os.chdir('state')
        cur_path = os.getcwd()
        
        reader = csv.DictReader(file)
        for row in reader:
            cur_state = row['state']
            filename = cur_state + '.csv'
            if not cur_state:
                filename = 'misc.csv'

            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)

            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames=fieldnames)
                writer.writerow(row)
            
            os.chdir(cur_path)


def blood_group():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        create_directory('blood_group')
        os.chdir('blood_group')
        cur_path = os.getcwd()
        
        reader = csv.DictReader(file)
        for row in reader:
            cur_blood_group = row['blood_group']
            filename = cur_blood_group + '.csv'
            if not re.match("[ABO]{1,2}[+-]", cur_blood_group):
                filename = 'misc.csv'

            fieldnames = list(row.keys())
            check_pre_existing_file(filename, fieldnames)

            with open(filename, 'a', newline='') as w_file:
                writer = csv.DictWriter(w_file, fieldnames=fieldnames)
                writer.writerow(row)
            
        os.chdir(cur_path)

# Create the new file here and also sort it in this function only.
def new_file_sort():
    return_to_assignment3()
    with open('studentinfo_cs384.csv', 'r') as file:
        os.chdir('analytics')
        
        data = []
        reader = csv.DictReader(file)

        for row in reader:
            new_row = {}
            for key in row.keys():
                if key == 'full_name':
                    full_name = row[key].split(' ')
                    first_name, last_name = full_name[0], full_name[1]
                    new_row['first_name'] = first_name
                    new_row['last_name'] = last_name
                else:
                    new_row[key] = row[key]
            data.append(new_row)

        fieldnames = list(data[0].keys())
        with open('studentinfo_cs384_names_split.csv', 'w', newline='') as w_file:
            writer = csv.DictWriter(w_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    
    with open('studentinfo_cs384_names_split.csv', 'r') as file:
        reader = csv.DictReader(file)

        fieldnames = reader.fieldnames
        data = sorted(reader, key=lambda row: row['first_name'])

        with open('studentinfo_cs384_names_split_sorted_first_name.csv', 'w', newline='') as w_file:
            writer = csv.DictWriter(w_file, fieldnames)
            writer.writeheader()
            writer.writerows(data)