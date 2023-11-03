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
    print("Added record")


def find_record(args, book):
    print("Edited record")


def delete_record(args, book):
    print("Deleted record")


# Address
def add_address(args, book):
    print("Added address")


def edit_address(args, book):
    print("Edited address")


def show_address(args, book):
    print("Showed address")


def delete_address(args, book):
    print("Deleted address")


# Email
def add_email(args, book):
    print("Added email")


def edit_email(args, book):
    print("Edited email")


def show_email(args, book):
    print("Showed email")


def delete_email(args, book):
    print("Deleted email")


# Contacts
def add_contact(args, book):
    name, *tags = args
    book.add_contact(name, tags)


def edit_contact(args, book):
    name, field, old_value, new_value = args
    book.edit_contact(name, field, old_value, new_value)


def show_contact(args, book):
    search_query = args[0].lower()
    book.search_contact(search_query)


def delete_contact(args, book):
    name = args[0]
    book.delete_contact(name)


def display_contacts(args, book):
    book.display_contacts()


# Birthday
def add_birthday(args, book):
    contact_name, birthday = args
    book.add_birthday(contact_name, birthday)


def edit_birthday(args, book):
    contact_name, new_birthday = args
    book.edit_birthday(contact_name, new_birthday)


def show_birthday(args, book):
    book.show_birthdays(args)


def delete_birthday(args, book):
    contact_name = args[0]
    book.remove_birthday(contact_name)


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
    "find": find_record,
    "delete": delete_record,
    "show-all": display_contacts,
    # Phone
    "add-phone": add_phone,  # See to add_phone method
    "edit-phone": edit_phone,
    "show-phone": show_phone,  # ?
    "delete-phone": delete_phone,
    # Address
    "add-address": add_address,
    "edit-address": edit_address,
    "show-address": show_address,  # ?
    "delete-address": delete_address,
    # Email
    "add-email": add_email,
    "edit-email": edit_email,
    "show-email": show_email,  # ?
    "delete-email": delete_email,
    # Birthday
    "add-birthday": add_birthday,
    "edit-birthday": edit_birthday,
    "show-birthday": show_birthday,  # ?
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
