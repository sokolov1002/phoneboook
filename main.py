from phonebook import Phonebook
from record import Record


def run():

    pb = Phonebook()

    running = True

    while running:
        print('(1)Add record (2)Show records (3)Search (4)Update (5)Delete (6)Quit')
        choice = int(input())
        if choice == 1:
            record = Record()
            pb.update(record)
        elif choice == 2:
            pb.show()
        elif choice == 3:
            pb.search()
        elif choice == 4:
            if len(pb.storage) != 0:
                current = pb.get(input('Name: '))
                if current:
                    print('Name: {0}, Number: {1}, E-mail: {2}'.format(current.name, current.number, current.email))
                    print('(1)Change name (2)Change number (3)Change e-mail')
                    current.update(int(input('1, 2 or 3: ')))
                    current = ''
            else:
                print('Phone book empty!')
        elif choice == 5:
            if len(pb.storage) != 0:
                current = pb.get(input('Name: '))
                if current:
                    confirm = input('Confirm deletion of {} (y/n): '.format(current.name))
                    if confirm == 'y':
                        pb.delete(current)
                    else:
                        continue
            else:
                print('Phone book empty!')
        elif choice == 6:
            print('Goodbye!')
            running = False

if __name__ == '__main__':
    run()