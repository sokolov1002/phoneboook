class Phonebook:

    def __init__(self):
        self.storage = []

    def update(self, record):
        if record:
            self.storage.append(record)
        else:
            print('Invalid input!')

    def show(self):
        if len(self.storage) != 0:
            for record in self.storage:
                print('Name: {0}, Number: {1}, E-mail: {2}'.format(record.name, record.number, record.email))
        else:
            print('Phone book empty!')

    def search(self):
        if len(self.storage) != 0:
            name = input('Name: ')
            for record in self.storage:
                if name == record.name:
                    print('Name: {0}, Number: {1}, E-mail: {2}'.format(record.name, record.number, record.email))
                else:
                    continue
        else:
            print('Phone book empty!')

    def get(self, name):
        if len(self.storage) != 0:
            for record in self.storage:
                if name == record.name:
                    return record
                else:
                    continue
        else:
            print('Phone book empty!')

    def delete(self, record):
        if record in self.storage:
            self.storage.remove(record)
            print('Record deleted!')
        else:
            print('Record not found!')