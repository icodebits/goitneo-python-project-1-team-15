from base.address_book import AddressBook
from base.notes import Notes
from helpers.cli_parser import parse_input

import time
import templates.messages as msg


def add_note(args, notes):
    note, *tags = args
    notes.add_note(note, tags)


def display_notes(args, notes):
    notes.display_notes()


def sort_notes(args, notes):
    sort_results = notes.sort_notes_by_tag()
    print(f"\nSorted notes by tags:")
    for note in sort_results:
        print(note)


def search_notes_by_tag(args, notes):
    search_tag = args[0]
    search_tag_results = notes.search_notes_by_tag(search_tag)
    print(f"\nNotes that contain tag '{search_tag}':")
    for note in search_tag_results:
        print(note)


def edit_note(args, notes):
    position, keywords = args
    edit_result = notes.edit_note(position, keywords)
    print(f"\n {edit_result}")


def delete_note(args, notes):
    position = args[0]
    delete_result = notes.delete_note(position)
    print(f"\n {delete_result}")


CONTACTS_OPERATIONS = {
    "add": "add_contact",
    "show-all": "display_contacts",
    "search": "search_contact",
    "edit": "edit_contact",
    "delete": "delete_contact",
}
NOTES_OPERATIONS = {
    "add": add_note,
    "show-all": display_notes,
    "sort": sort_notes,
    "search": search_notes_by_tag,
    "edit": edit_note,
    "delete": delete_note,
}


def contacts_handler(operator):
    return CONTACTS_OPERATIONS[operator]


def notes_handler(operator):
    return NOTES_OPERATIONS[operator]


def main():
    book = AddressBook()
    notes = Notes()

    main_menu_exit = False
    contacts_menu_back = False
    notes_menu_back = False

    while not main_menu_exit:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  # exit from cli
            print("Good bye!")
            main_menu_exit = True

        if command == "hello":  # main menu
            print(msg.welcome)

        if command == "contatcs":  # contacts menu
            print(msg.contacts_menu)
            time.sleep(2)
            user_input = input("Enter a command: ").strip().lower()
            command, *args = parse_input(user_input)
            while not contacts_menu_back:
                if command == "back":
                    print("Back selected")
                    contacts_menu_back = True
                contacts_handler(command)(args)
            contacts_menu_back = True

        if command == "notes":  # notes menu
            print(msg.notes_menu)
            time.sleep(2)
            user_input = input("Enter a command: ").strip().lower()
            command, *args = parse_input(user_input)
            while not notes_menu_back:
                if command == "back":
                    print("Back selected")
                    notes_menu_back = True
                notes_handler(command)(args)
            notes_menu_back = False


if __name__ == "__main__":
    main()
