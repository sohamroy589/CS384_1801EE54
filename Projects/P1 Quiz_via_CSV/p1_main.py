import os
import sqlite3
import time
import hashlib

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS project1_registration
(name TEXT NOT NULL,
roll TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
whatsapp_no INT UNIQUE,
salt NOT NULL);
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

logged_in = None
while not logged_in:
    os.system('cls')
    resp = input('Press 1 to register\nPress 2 to login if you are already registered\nPress q to exit\n')
    if resp == '1':
        register()
    elif resp == '2':
        logged_in = login()
    elif resp == 'q':
        break

print(logged_in)