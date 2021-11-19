# QUESTÃO 5 - AV2 PYTHON

import sqlite3
conn = sqlite3.connect("school.db")

#--------------------------------------------------------------------------------------------

def create_table():
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS school(
                        id_student INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        grade FLOAT)''')
    except Exception as e:
        print("Error on table creating: ", e

#--------------------------------------------------------------------------------------------

def add_student(name, grade):
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO school (name, grade) VALUES (?, ?)',(name, grade))
        conn.commit()
    except sqlite3.Error as e:
        print("Error on student insertion: ", e)
    finally:
        cursor.close()

#--------------------------------------------------------------------------------------------

def get_student():
    try:
        return conn.execute('SELECT id_student, name, grade FROM school')
    except sqlite3.Error as e:
        print("Error to find a student: ", e)

#--------------------------------------------------------------------------------------------

def delete_student(id_student):
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM school WHERE id_student = ?',(id_student, ))
        conn.commit()
        conn.execute('VACUUM')
    except sqlite3.Error as e:
        print('Cannot delete student: ', e)
    finally:
        cursor.close()

#--------------------------------------------------------------------------------------------

def update_student(id_student, name):
    try:
        cursor = conn.cursor()
        update_query = '''UPDATE school set name = ? WHERE id_student = ?'''
        data = (name, id_student)
        cursor.execute(update_query, data)
        conn.commit()
        print('Updated successfully.')
    except sqlite3.Error as e:
        print('Error when update student: ', e
    finally:
        cursor.close()