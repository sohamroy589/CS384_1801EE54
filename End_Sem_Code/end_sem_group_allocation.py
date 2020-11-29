import csv
import os
import re
import shutil

# Global variables to store some important data
home = os.getcwd()
data = {}
branch_strength_data = []

# General function used for writing the files
def write(filename, data, fieldnames):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as wfile:
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    else:
        with open(filename, 'a', newline='') as wfile:
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writerows(data)

# Creates the individual branch wise files
def create_branches(reader):
    global data, branch_strength_data
    data = {}
    fieldnames = reader.fieldnames
    for row in reader:
        branch = re.search(r'[A-Z]+', row['Roll']).group()
        if branch not in data.keys():
            data[branch] = [row]
        else:
            data[branch].append(row)
    branch_strength_data = []
    for key, val in data.items():
        if os.path.exists(key+'.csv'):
            os.remove(key+'.csv')
        write(key+'.csv', val, fieldnames)
        branch_strength_data.append({'BRANCH_CODE': key, 'BRANCH_STRENGTH': len(val)})
    branch_strength_data.sort(key=lambda x: x['BRANCH_STRENGTH'], reverse=True)
    with open('branch_strength.csv', 'w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=list(branch_strength_data[0].keys()))
        writer.writeheader()
        writer.writerows(branch_strength_data)

# Creating the groups
def create_groups(reader, no_of_groups):
    groups = [[] for i in range(no_of_groups)]
    stat = [{'group':None, 'total':None} for i in range(no_of_groups)]
    left = []
    ptr = [0 for i in range(len(branch_strength_data))]
    # Dividing according to the floor division
    for d in branch_strength_data:
        q = d['BRANCH_STRENGTH'] // no_of_groups
        r = d['BRANCH_STRENGTH'] % no_of_groups
        for i in range(no_of_groups):
            if stat[i].get(d['BRANCH_CODE']): 
                stat[i][d['BRANCH_CODE']] += q
            else:
                stat[i][d['BRANCH_CODE']] = q
        left += data[d['BRANCH_CODE']][-r:]
    # Including the remainders
    gr_no = 0
    for student in left:
        branch = re.search(r'[A-Z]+', student['Roll']).group()
        if stat[gr_no].get(branch):
            stat[gr_no][branch] += 1
        else:
            stat[gr_no][branch] = 1
        gr_no = (gr_no + 1) % no_of_groups
    # Finally adding in the groups
    for i in range(no_of_groups):
        for b in range(len(ptr)):
            branch = branch_strength_data[b]['BRANCH_CODE']
            groups[i] += data[branch][ptr[b]:ptr[b]+stat[i][branch]]
            ptr[b] += stat[i][branch]
    # Create the files and update the group statistics
    for i in range(no_of_groups):
        filename = 'Group_G' + format(i+1, '02d')
        write(filename + '.csv', groups[i], reader.fieldnames)
        stat[i]['total'] = len(groups[i])
        stat[i]['group'] = filename
    # Creating the stats_grouping file
    write('stats_grouping.csv', stat, list(stat[0].keys()))


def group_allocation(filename, number_of_groups):
    if os.path.exists('groups'):
        shutil.rmtree('groups', ignore_errors=True)
    os.mkdir('groups')
    with open(filename, 'r') as rfile:
        reader = csv.DictReader(rfile)
        os.chdir('groups')
        create_branches(reader)
        create_groups(reader, number_of_groups)

filename = "Btech_2020_master_data.csv"
number_of_groups = 12 
group_allocation(filename, number_of_groups)