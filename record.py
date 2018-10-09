class Record:

    def __init__(self):
        self.first_name = input('First name: ')
        self.last_name = input('Last name: ')
        self.phone_number = input('Number: ')
        self.email = input('E-mail: ')

    def change_name(self):
        new_name = input('New name: ')
        if new_name:
            self.name = new_name
        else:
            print('Invalid input!')

    def change_number(self):
        new_number = input('New number: ')
        if new_number:
            self.number = new_number
        else:
            print('Invalid input!')

    def change_email(self):
        new_email = input('New e-mail: ')
        if new_email:
            self.email = new_email
        else:
            print('Invalid input!')

    def update(self, choice):
        if choice == 1:
            self.change_name()
        elif choice == 2:
            self.change_number()
        elif choice == 3:
            self.change_email()
