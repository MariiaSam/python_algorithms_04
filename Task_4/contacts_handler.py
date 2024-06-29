''''

def add_contact(): "add [ім'я] [номер телефону]"


def change_contact(): "change [ім'я] [новий номер телефону]"

def show_phone(): "phone [ім'я]"

 show_all "all"
 усі збережені контакти з номерами телефонів
'''

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(contacts, name, phone):
    if name not in contacts:
        return f'Contact with this {name} was not found.'
    contacts[name] = phone
    return 'Contact updated.'


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    else:
        return f'Contact with this {name} was not found.'


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            return f'{name}: {phone}'
    else:
        return 'Contact was not found.'