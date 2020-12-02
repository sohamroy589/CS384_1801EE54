import os
import sqlite3
import time

con = sqlite3.connect('test.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS project1_registration
(name TEXT NOT NULL,
roll TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
whatsapp_no INT UNIQUE);
''')

def register():
    os.system('cls')
    name = input('Enter your name--')
    roll = input('Enter your Roll No.--')
    password = input('Enter your password--')
    whatsapp = input('Enter your WhatsApp No.--')
    os.system('cls')
    try:
        cur.execute('''INSERT INTO project1_registration
        VALUES (?, ?, ?, ?);
        ''', (name, roll, password, whatsapp))
        con.commit()
        print('You have successfully registered for the quiz. Now login using your Roll No. and password.')
        time.sleep(3)
    except:
        print('Could not register probably because your Roll No. or WhatsApp No. already exists')
        time.sleep(3)

def login():
    pass

logged_in = False
while not logged_in:
    os.system('cls')
    resp = input('Press 1 to register\nPress 2 to login if you are already registered\nPress q to exit')
    if resp == '1':
        register()
    elif resp == '2':
        login()
    elif resp == 'q':
        break
