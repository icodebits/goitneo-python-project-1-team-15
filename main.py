from base.address_book import AddressBook
from base.notes import Notes
from helpers.cli_parser import parse_input

import templates.messages as msg
import time
from colorama import just_fix_windows_console, Fore, Style

just_fix_windows_console()  # execute for Windows OS compability


# =====================
# | CONTATCS HANDLERS |
# =====================
def add_contact(args, book):
    name, *tags = args
    # add method from book obj
    print("\n🟢 Contact added\n")


def search_contact(args, book):
    search_query = args[0]
    # search method from book obj
    print("\n✅ Contact finded\n")


def edit_contact(args, book):
    name, field, old_value, new_value = args
    # edit method from book obj
    print("\n📒 Contact updated\n")


def delete_contact(args, book):
    position = args[0]
    # delete method from book obj
    print("\n❌ Contact deleted\n")


def display_contacts(args, book):
    # show_all method from book obj
    print("\n📱 All contatcs\n")


# ==================
# | NOTES HANDLERS |
# ==================
def add_note(args, notes):
    note_name, *tags = args
    notes.add_note(note_name, tags)
    print("Added")


def search_notes_by_tag(args, notes):
    search_tag = args[0]
    search_tag_results = notes.search_notes_by_tag(search_tag)
    print(f"\nNotes that contain tag '{search_tag}':")
    for note in search_tag_results:
        print(note)


def edit_note(args, notes):
    position, text, *tags = args
    edit_result = notes.edit_note(int(position), text, tags=None)
    print(f"\n {edit_result}")


def delete_note(args, notes):
    position = args[0]
    delete_result = notes.delete_note(int(position))
    print(f"\n {delete_result}")


def sort_notes(args, notes):
    sort_results = notes.sort_notes_by_tag()
    print(f"\nSorted notes by tags:")
    for note in sort_results:
        print(note)


def display_notes(args, notes):
    notes.display_notes()


CONTACTS_OPERATIONS = {
    "add": add_contact,
    "search": search_contact,
    "edit": edit_contact,
    "delete": delete_contact,
    "show-all": display_contacts,
}

NOTES_OPERATIONS = {
    "add": add_note,
    "search": search_notes_by_tag,
    "edit": edit_note,
    "delete": delete_note,
    "sort": sort_notes,
    "show-all": display_notes,
}


def contacts_handler(operator):
    return CONTACTS_OPERATIONS[operator]


def notes_handler(operator):
    """
    написати перевірки для невалідних команд
    """
    if operator in NOTES_OPERATIONS.key():
        return NOTES_OPERATIONS[operator]
    else:
        return NOTES_OPERATIONS[operator]


def main():
    book = AddressBook()
    notes = Notes()

    main_menu_exit = False
    contacts_menu_back = False
    notes_menu_back = False

    print(msg.welcome)

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
                contacts_handler(command)(args, book)

        elif command == "notes":  # notes menu
            print(msg.notes_menu)
            time.sleep(0.6)  # wait 600ms after printing menu
            while not notes_menu_back:
                user_input = input("Enter a command: ").strip().lower()
                command, *args = parse_input(user_input)

                if command == "back":
                    notes_menu_back = True
                    print(Fore.YELLOW + msg.back)  # set color to cli
                    print(Style.RESET_ALL)  # reset colors
                    break

                notes_handler(command)(args, notes)

        else:
            print(Fore.RED + msg.error)
            print(Style.RESET_ALL)


if __name__ == "__main__":
    main()
