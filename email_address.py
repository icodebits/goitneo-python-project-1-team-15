from collections import UserDict, defaultdict
import re
from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Address(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validated_phone()

    def validated_phone(self):
        pattern = re.compile(r'\d{10}$')
        if not re.match(pattern, self.value):
            raise ValueError(print("Phone number must have 10 digits in format 0501111111"))


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validated_birthday()

    def validated_birthday(self):
        try:
            datetime.strptime(self.value, "%d.%m.%Y")
        except ValueError:
            raise ValueError(print("Wrong format, must be DD.MM.YYYY"))


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validated_email()

    def validated_email(self):
        pattern = re.compile(r'[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}')
        if not re.match(pattern, self.value):
            raise ValueError(print("Wrong email format"))


class Record:
    def __init__(self, name):
        self.name = Name(name.lower())
        self.phones = []
        self.birthday = None
        self.emails = []
        self.address = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_email(self, email):
        self.emails.append(Email(email))

    def add_address(self, address):
        self.address = Address(address)

    def edit_phone(self, old, new):
        self.phones = [new if str(i) == old else i for i in self.phones]

    def edit_email(self, old, new):
        self.emails = [new if str(i) == old else i for i in self.emails]

    def remove_phone(self, phone):
        for i in self.phones:
            if str(i) == phone:
                return self.phones.remove(i)

    def find_phone(self, phone):
        for i in self.phones:
            if str(i) == phone:
                return i
        return "The phone is not found"

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}, birthday: {self.birthday}, email: {'; '.join(str(p) for p in self.emails)}, address: {self.address}"


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        lower_name = name.lower()
        if lower_name in self.data:
            return self.data[lower_name]
        return "The user is not found"

    def delete(self, name):
        lower_name = name.lower()
        if lower_name in self.data:
            return self.data.pop(lower_name)

    def get_birthdays_per_week(self):
        today = datetime.today().date()
        next_week_birthdays = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday is not None:
                birthday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                this_year_birthdays = birthday.replace(year=today.year)
                if this_year_birthdays < today:
                    this_year_birthdays = this_year_birthdays.replace(year=today.year + 1)

                delta_days = (this_year_birthdays - today).days
                weekdays = this_year_birthdays.strftime("%A")

                if delta_days <= 7 and (weekdays == "Saturday" or weekdays == "Sunday"):
                    weekdays = "Monday"
                    next_week_birthdays[weekdays].append(name)
                elif delta_days <= 7 and weekdays in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
                    next_week_birthdays[weekdays].append(name)
                else:
                    return "No birthdays next week"
            else:
                return "No birthdays next week"

        result = ''
        for weekdays, names in next_week_birthdays.items():
            result += f"{weekdays}: {', '.join(names)}\n"

        return result


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me the correct data"

    return wrapper


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone = args
    if name.lower() in book.data:
        return ("Contact already exists")
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

@input_error
def change_username_phone(args, book):
    name, new_phone = args
    pattern = re.compile(r'\d{10}$')
    if not re.match(pattern, new_phone):
        raise ValueError(print("Phone number must have 10 digits in format 0501111111"))
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact updated."
    else:
        return "No such username"

@input_error
def phone_username(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            return record.phones[0]
        else:
            return "No such username"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: phone <name>"))

@input_error
def all(book):
    if book.data:
        result = ''
        for _, value in book.data.items():
            result += str(value) + "\n"
        return result
    else:
        raise ValueError(print("The list of contacts is empty, please enter add <name> <phone>"))
    
@input_error
def name(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            for _, i in book.data.items():
                return(i)

@input_error
def add_birthday(args, book):
    name, birthday = args
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.add_birthday(birthday)
        return "Birthday added"
    else:
        return "No such username"
    
@input_error
def add_address(args, book):
    if len(args) < 2:
        return "Please enter a name and an address to add."
    name, address = args[0], ' '.join(args[1:])
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.add_address(address)
        return "Address added"
    else:
        return "No such username"
    
@input_error
def change_address(args, book):
    if len(args) < 2:
        return "Please enter a name and a new address to change."
    name, new_address = args[0], ' '.join(args[1:])
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.address.value = new_address
        return "Address updated."
    else:
        return "No such username"
    
@input_error
def show_address(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            return record.address.value
        else:
            return "No such username"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: show-address <name>"))
    
@input_error
def delete_address(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            if record.address:
                record.address = "-"
                return "Address deleted"
            else:
                return "No address to delete"
        else:
            return "No such username"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: delete-address <name>"))

@input_error
def show_birthday(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            return record.birthday
        else:
            return "User is missing"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: show-birthday <name>"))

@input_error
def birthdays(book):
    birthdays = book.get_birthdays_per_week()
    if birthdays:
        return birthdays
    else:
        return "No birthdays next week"
    
@input_error
def add_email(args, book):
    name, email = args
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.add_email(email)
        return "Email added"
    else:
        return "No such username"
    
@input_error
def change_email(args, book):
    name, new_email = args
    if name.lower() not in book.data:
        return "No such username"
    pattern = re.compile(r'[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}')
    if not re.match(pattern, new_email):
        raise ValueError(print("Wrong email format"))
    if name.lower() in book.data:
        record = book.data[name.lower()]
        record.edit_email(record.emails[0].value, new_email)
        return "Email updated."
    
@input_error
def show_email(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            return record.emails[0]
        else:
            return "No such username"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: show-email <name>"))
    
@input_error
def delete_email(args, book):
    if args:
        name = args[0]
        if name.lower() in book.data:
            record = book.data[name.lower()]
            if record.emails:
                record.emails.pop(0)
                record.emails.append("-")
                return "Email deleted"
            else:
                return "No email to delete"
        else:
            return "No such username"
    else:
        raise ValueError(print("Wrong format, please enter the data in format: delete-email <name>"))
    
def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("""How can I help you?
                For adding the contact please enter the data in format: add <name> <phone> (10 digits in format 0501111111)
                For changing the contact please enter the data in format: change <name> <new phone> (10 digits in format 0501111111)
                For getting a phone number please enter the data in format: phone <name>
                For adding a birthday please enter the data in format: add-birthday <name> birthday (in format DD.MM.YYYY)
                For getting user's birthday please enter the data in format: show-birthday <name>
                For getting list of birthdays next week enter <birthdays>
                For getting the list of all contacts enter: <all>
                For exit please enter: <close> or <exit> """)
        elif command in ["add"]:
            print(add_contact(args, book))
        elif command in ["change"]:
            print(change_username_phone(args, book))
        elif "phone" in command:
            print(phone_username(args, book))
        elif "all" in command:
            print(all(book))
        elif command in ["add-birthday"]:
            print(add_birthday(args, book))
        elif command in ["show-birthday"]:
            print(show_birthday(args, book))
        elif command in ["birthdays"]:
            print(birthdays(book))
        elif command in ["add-email"]:
            print(add_email(args, book))
        elif command in ["change-email"]:
            print(change_email(args, book))
        elif command in ["show-email"]:
            print(show_email(args, book))
        elif command in ["delete-email"]:
            print(delete_email(args, book))
        elif command in ["name"]:
            print(name(args, book))
        elif command in ["add-address"]:
            print(add_address(args, book))
        elif command in ["change-address"]:
            print(change_address(args, book))
        elif command in ["show-address"]:
            print(show_address(args, book))
        elif command in ["delete-address"]:
            print(delete_address(args, book))
        else:
            print("Invalid command. Please verify the command and try again")


if __name__ == "__main__":
    main()








