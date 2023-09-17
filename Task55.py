from pathlib import Path

FILE_PATH = Path('Task.py', 'phonebook', 'phonebook.txt')
print(FILE_PATH)

def count_id():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        contact_id = 1
        for line in file:
            contact_id += 1
        return contact_id

def add_contact():
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info = input('Enter data according to the sample - Last name First name; phone number: ')
        contact_id = count_id()
        file.write(f'\n{contact_id}. {info}')

def show_contact():
    with open(FILE_PATH, 'r', encoding = 'utf8') as file:
        # print([lines for lines in file])
        print(*[line for line in file])
        # print(file.readlines())

def find_contact():
    list_1 = []
    search = input("Enter contact: ").strip()
    with open(FILE_PATH, 'r', encoding = 'utf8') as file:
        for contact in file:
            if search in contact:
                list_1.append(contact)