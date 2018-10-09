from db import Database
from record import Record


def main():

	db = Database()

	running = True

	while running:
		print()
		print('(1)Add record (2)Show records (3)Update (4)Delete (5)Quit')
		print()
		choice = int(input('Please, choose a number: '))
		print()
		if choice == 1:
			record = Record()
			db.insert_into_db(record.first_name, record.last_name, record.phone_number, record.email)
		elif choice == 2:
			db.show_records()
		elif choice == 3:
			print()
			contact_id = int(input('Enter contact ID to update: '))
			print()
			print('(1) Change first name')
			print('(2) Change last name')
			print('(3) Change phone number')
			print('(4) Change e-mail')
			print()
			update_choice = int(input('Please, choose a number: '))
			db.update_record(contact_id, update_choice)
		elif choice == 4:
			print()
			contact_id = int(input('Enter contact ID to delete: '))
			db.delete_record(contact_id)
		elif choice == 5:
			print()
			print('Goodbye!')
			running = False


if __name__ == '__main__':
	main()
