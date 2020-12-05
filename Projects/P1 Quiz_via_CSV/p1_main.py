import os
import sqlite3
import time
import hashlib, csv
from Quiz import quiz

con = sqlite3.connect('project1_quiz_cs384.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS project1_registration
(name TEXT NOT NULL,
roll TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
whatsapp_no INT UNIQUE,
salt NOT NULL);
''')
cur.execute('''CREATE TABLE IF NOT EXISTS project1_marks(
    roll TEXT NOT NULL,
    quiz_num TEXT NOT NULL,
    total_marks INT NOT NULL,
    UNIQUE(roll,quiz_num));
''')

def gen_key(password, salt):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )

def register():
    os.system('cls')
    name = input('Enter your name--')
    roll = input('Enter your Roll No.--')
    password = input('Enter your password--')
    whatsapp = input('Enter your WhatsApp No.--')
    salt = os.urandom(16)
    key = gen_key(password, salt)
    os.system('cls')
    try:
        cur.execute('''INSERT INTO project1_registration
        VALUES (?, ?, ?, ?, ?);
        ''', (name, roll, key, whatsapp, salt))
        con.commit()
        print('You have successfully registered for the quiz. Now login using your Roll No. and password.')
        time.sleep(3)
    except:
        print('Could not register probably because your Roll No. or WhatsApp No. already exists')
        time.sleep(3)

def login():
    os.system('cls')
    username = input('Enter your username. It is same as your Roll No. --- ')
    password = input('Enter your password --- ')
    user = cur.execute('''SELECT * FROM project1_registration
    WHERE
        roll = ?;
    ''', (username,)).fetchall()
    if len(user) == 0:
        print('Incorrect username!')
        time.sleep(2)
    else:
        user = user[0]
        salt = user[-1]
        key = user[2]
        test_key = gen_key(password, salt)
        if test_key == key:
            return user
        else:
            print('Incorrect password!')
            time.sleep(2)

def export():
    for q_name in os.listdir('quiz_wise_questions'):
        name = q_name.rstrip('.csv')
        data = cur.execute('SELECT * FROM project1_marks WHERE quiz_num = ?;', (name,)).fetchall()
        if len(data) > 0:
            with open(os.path.join(os.getcwd(), 'quiz_wise_responses', name+'.csv'), 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['roll', 'quiz_num', 'total_marks'])
                writer.writerows(data)

logged_in = None
while not logged_in:
    os.system('cls')
    resp = input('Press 1 to register\nPress 2 to login if you are already registered\nPress q to exit\n')
    if resp == '1':
        register()
    elif resp == '2':
        logged_in = login()
    elif resp == 'q':
        os._exit(1)

print('Choose the quiz number that you want to attempt')
for quiz_name in os.listdir('quiz_wise_questions'):
    q_name = quiz_name.rstrip('.csv')
    print(q_name, end=' ')
print()
q_name = input()

q = quiz(q_name+'.csv', logged_in[0], logged_in[1])
q.run()
try:
    cur.execute(
        '''INSERT INTO project1_marks
        VALUES (?, ?, ?);
        '''
    , (logged_in[1], q_name, q.marks))
except:
    cur.execute(
        '''UPDATE project1_marks
        SET total_marks = ?
        WHERE roll = ? AND quiz_num = ?;
        '''
    , (q.marks, logged_in[1], q_name))
con.commit()
if q.willexport:
    export()
con.close()
os._exit(1)
