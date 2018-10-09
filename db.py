import sqlite3
from sqlite3 import Error


class Database:

    db_file = 'E:\\Coding\\Python\\Phonebook\\db\\pb.db'

    def __init__(self):
        create_table_sql = """

            CREATE TABLE IF NOT EXISTS Contacts (
            id integer PRIMARY KEY AUTOINCREMENT, 
            first_name varchar, 
            last_name varchar, 
            phone_number varchar, 
            email varchar
            );

            """
        try:
            self.connection = sqlite3.connect(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(create_table_sql)
            self.connection.close()
        except Error as e:
            print(e)

    def insert_into_db(self, f_name, l_name, num, e_mail):
        sql = "INSERT INTO Contacts (first_name, last_name, phone_number, email) VALUES (?, ?, ?, ?);"
        try:
            self.connection = sqlite3.connect(self.db_file)
            cursor = self.connection.cursor()
            data = (f_name, l_name, num, e_mail,)
            cursor.execute(sql, data)
            self.connection.commit()
            self.connection.close()
            print()
            print('Record added.')
        except Error as e:
            print(e)

    def show_records(self):
        sql = "SELECT * FROM Contacts;"
        try:
            self.connection = sqlite3.connect(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print('{}. {} {} {} {}'.format(row[0], row[1], row[2], row[3], row[4]))
            else:
                print('Phonebook is empty!')
            self.connection.close()
        except Error as e:
            print(e)

    def update_record(self, contact_id, condition):
        sql = ""
        data_to_insert = ""
        if condition == 1:
            data = input('Enter the new first name: ')
            sql = "UPDATE Contacts SET first_name = ? WHERE id = %s" % contact_id
            data_to_insert = (data,)
        elif condition == 2:
            data = input('Enter the new last name: ')
            sql = "UPDATE Contacts SET last_name = ? WHERE id = %s" % contact_id
            data_to_insert = (data,)
        elif condition == 3:
            data = input('Enter the new phone number: ')
            sql = "UPDATE Contacts SET phone_number = ? WHERE id = %s" % contact_id
            data_to_insert = (data,)
        elif condition == 4:
            data = input('Enter the new e-mail: ')
            sql = "UPDATE Contacts SET email = ? WHERE id = %s" % contact_id
            data_to_insert = (data,)
        try:
            self.connection = sqlite3.connect(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(sql, data_to_insert)
            self.connection.commit()
            print('Record updated.')
            self.connection.close()
        except Error as e:
            print(e)
        
    def delete_record(self, contact_id):
        sql = "DELETE FROM Contacts WHERE id = %s" % contact_id
        try:
            self.connection = sqlite3.connect(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.connection.close()
        except Error as e:
            print(e)
