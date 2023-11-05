from base.address_book import AddressBook
from base.notes import Notes
from helpers.cli_parser import parse_input
from helpers.storage import load_data, save_data

import templates.messages as msg

import time  # add timeouts for output
from colorama import just_fix_windows_console, Fore, Style  # add styles to cli output

just_fix_windows_console()  # execute for Windows OS compatibility


# =====================
# | CONTACTS HANDLERS |
# =====================
def add_record(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    contact = args[0]
    book.add_record(contact)


def edit_record(args, book):
    if len(args) < 2:
        print("\n❌ Please provide old and new names to edit")
        return
    old_name, new_name = args
    book.edit(old_name, new_name)


def find_record(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.find(name)


def delete_record(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.delete(name)


def display_contacts(args, book):
    res = book.display_contacts()
    print(res)


# Phones
def add_phone(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and phone number")
        return
    name, *phones = args
    book.add_phone(name, phones)


def edit_phone(args, book):
    if len(args) < 3:
        print("\n❌ Please provide name, old and new phone numbers")
        return
    name, old_value, new_value = args
    has_ten_symbols = len(new_value) == 10
    is_digit = new_value.isdigit()
    
    if not (has_ten_symbols and is_digit):
        print("\n❌ Field phone is incorrect")
        return
    book.edit_phone(name, old_value, new_value)


def show_phone(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.show_phone(name)


def delete_phone(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and phone to delete")
        return
    name, phone = args
    book.delete_phone(name, phone)
   


# Address
def add_address(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and address")
        return
    name, *address = args
    book.add_address(name, address)


def edit_address(args, book):
    if len(args) < 2:
        print("\n❌ Please provide old and new address to edit")
        return
    name, *address = args
    book.edit_address(name, address)


def show_address(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.show_address(name)


def delete_address(args, book):
    if len(args) < 1:
        print("\n❌ Please provide name")
        return
    name = args[0]
    book.delete_address(name)


# Email
def add_email(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and email")
        return
    name, *emails = args
    book.add_email(name, emails)


def edit_email(args, book):
    if len(args) < 3:
        print("\n❌ Please provide name, old and new email address")
        return
    name, old_email, new_email = args
    book.edit_email(name, old_email, new_email)


def show_email(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.show_email(name)


def delete_email(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and phone to delete")
        return
    name, email = args
    book.delete_email(name, email)


# Birthday
def add_birthday(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and date of birth")
        return
    contact_name, birthday = args
    book.add_birthday(contact_name, birthday)


def edit_birthday(args, book):
    if len(args) < 2:
        print("\n❌ Please provide name and new date of birth")
        return
    contact_name, new_birthday = args
    book.edit_birthday(contact_name, new_birthday)


def show_birthday(args, book):
    if len(args) == 0:
        print("\n❌ Please provide the name")
        return
    name = args[0]
    book.show_birthday(name)


def delete_birthday(args, book):
    if len(args) < 1:
        print("\n❌ Please provide name")
        return
    contact_name = args[0]
    book.delete_birthday(contact_name)


def next_birthdays(args, book):
    if len(args) == 0:
        res = book.next_birthdays()
    else:
        days = args[0]
        res = book.next_birthdays(int(days))

    print(res)


# ==================
# | NOTES HANDLERS |
# ==================
def add_note(args, notes):
    note_content = " ".join(args)
    res = notes.add_note(note_content)
    print(f"\n{res}\r\n")


def edit_note(args, notes):
    position = args[0]
    content = " ".join(args[1:])
    res = notes.edit_note(int(position), content)
    print(f"\n{res}\r\n")


def delete_note(args, notes):
    position = args[0]
    res = notes.delete_note(int(position))
    print(f"\n{res}\r\n")


def search_notes(args, notes):
    keyword = args[0]
    res = notes.search_notes(keyword)
    print(f"\nNotes that contain '{keyword}' keyword:")
    for note in res:
        print(note)


def display_notes(args, notes):
    print("\nAll notes:")
    notes.display_notes()


def add_tags(args, notes):
    note_idx = int(args[0])
    tags = args[1:]
    res = notes.add_tags(note_idx, tags)
    print(f"\n{res}\r\n")


def search_notes_by_tag(args, notes):
    search_tag = args[0]
    res = notes.search_notes_by_tag(search_tag)
    print(f"\nNotes that contain tag '{search_tag}':")
    for note in res:
        print(note)


def sort_notes_by_tag(args, notes):
    res = notes.sort_notes_by_tag()
    print(f"\nSorted notes by tags:")
    for note in res:
        print(note)


CONTACTS_OPERATIONS = {
    "add": add_record,
    "edit": edit_record,
    "find": find_record,
    "delete": delete_record,
    "show-all": display_contacts,
    # Phone
    "add-phone": add_phone,
    "edit-phone": edit_phone,
    "show-phone": show_phone,
    "delete-phone": delete_phone,
    # Address
    "add-address": add_address,
    "edit-address": edit_address,
    "show-address": show_address,
    "delete-address": delete_address,
    # Email
    "add-email": add_email,
    "edit-email": edit_email,
    "show-email": show_email,
    "delete-email": delete_email,
    # Birthday
    "add-birthday": add_birthday,
    "edit-birthday": edit_birthday,
    "show-birthday": show_birthday,
    "delete-birthday": delete_birthday,
    "next-birthdays": next_birthdays,
}

NOTES_OPERATIONS = {
    "add": add_note,
    "edit": edit_note,
    "delete": delete_note,
    "show": search_notes,
    "show-all": display_notes,
    "add-tags": add_tags,
    "search-tags": search_notes_by_tag,
    "sort-tags": sort_notes_by_tag,
}


def handler_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Unsupported operation type"

    return inner


@handler_error
def contacts_handler(operator):
    return CONTACTS_OPERATIONS[operator]


@handler_error
def notes_handler(operator):
    return NOTES_OPERATIONS[operator]


def main():
    book = AddressBook()
    notes = Notes()

    main_menu_exit = False
    contacts_menu_back = False
    notes_menu_back = False

    print(msg.welcome)

    data = load_data("data.pkl")
    book = data["contacts"]
    notes = data["notes"]

    while not main_menu_exit:
        if notes_menu_back or contacts_menu_back:  # main menu
            notes_menu_back = contacts_menu_back = False
            print(Fore.GREEN + msg.main_menu)  # set color to cli
            print(Style.RESET_ALL)  # reset colors
            time.sleep(1)  # wait 1000ms after printing menu
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  # exit from cli
            print(msg.leave)
            main_menu_exit = True

        elif command == "contacts":  # contacts menu
            print(msg.contacts_menu)
            time.sleep(0.6)  # wait 600ms after printing menu
            while not contacts_menu_back:
                user_input = input("Enter a command: ").strip().lower()
                command, *args = parse_input(user_input)

                if command == "back":
                    contacts_menu_back = True
                    print(Fore.YELLOW + msg.back)  # set color to cli
                    print(Style.RESET_ALL)  # reset colors
                    break

                try:
                    contacts_handler(command)(args, book)
                except TypeError:
                    print(Fore.RED + msg.error)
                    print(Style.RESET_ALL)

        elif command == "notes":  # notes menu
            print(msg.notes_menu)
            time.sleep(0.6)  # wait 600ms after printing menu
            while not notes_menu_back:
                user_input = input("Enter a command: ").strip()
                command, *args = parse_input(user_input)

                if command == "back":
                    notes_menu_back = True
                    print(Fore.YELLOW + msg.back)  # set color to cli
                    print(Style.RESET_ALL)  # reset colors
                    break

                try:
                    notes_handler(command)(args, notes)
                except TypeError:
                    print(Fore.RED + msg.error)
                    print(Style.RESET_ALL)
        else:
            print(Fore.RED + msg.error)
            print(Style.RESET_ALL)

    data["contacts"] = book
    data["notes"] = notes
    save_data(data, "data.pkl")


if __name__ == "__main__":
    main()
