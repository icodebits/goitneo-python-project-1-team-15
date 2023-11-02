from simple_term_menu import TerminalMenu
import time
import pickle
import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
    return None

def save_data(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Contacts", "Notes", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    data_file = "address_book_data.pkl"
    address_book = load_data(data_file)

    if address_book is None:
        address_book = {"contacts": {}, "notes": []}

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    contacts_menu_title = "  Contacts menu.\n  Press Q or Esc to back to main menu. \n"
    contacts_menu_items = [
        "Add contact",
        "Show contact",
        "Show contacts",
        "Edit contact",
        "Remove contact",
    ]
    contacts_menu_back = False
    contacts_menu = TerminalMenu(
        menu_entries=contacts_menu_items,
        title=contacts_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    notes_menu_title = "  Nones menu.\n  Press Q or Esc to back to main menu. \n"
    notes_menu_items = [
        "Add note",
        "Show note",
        "Show notes",
        "Edit note",
        "Remove note",
    ]
    notes_menu_back = False
    notes_menu = TerminalMenu(
        menu_entries=notes_menu_items,
        title=notes_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    while not main_menu_exit:
        # main_sel -> main selection
        main_sel = main_menu.show()

        if main_sel == 0:
            print("Welcome to CONTACTS menu")
            time.sleep(2)
            while not contacts_menu_back:
                edit_sel = contacts_menu.show()
                if edit_sel == 0:
                    contact_name = input("Add contact name: ")
                    print("name: ", contact_name)
                    # Add your handler for add-name operation
                    time.sleep(5)  # Wait 5 sec before return to menu
                if edit_sel == 1:
                    contact_name = input("Enter contact name to show: ")
                    contact_data = address_book["contacts"].get(contact_name)
                    if contact_data:
                        print("Contact data:")
                        print(contact_data)
                    else:
                        print(f"Contact '{contact_name}' not found.")
                    time.sleep(5)
                if edit_sel == 2:
                    print("Show all contacts")
                    for contact_name, contact_data in address_book["contacts"].items():
                        print(contact_name)
                        print("Contact data:", contact_data)
                    time.sleep(5)
                    # Add your handler for show-all operation
                    time.sleep(5)
                elif edit_sel == 3:
                    contact_name = input("Edit contact by name: ")
                    print("name: ", contact_name)
                    # Add your handler for edit-name operation
                    time.sleep(5)
                elif edit_sel == 4:
                    contact_name = input("Remove contact by name: ")
                    print("name: ", contact_name)
                    # Add your handler for remove-name operation
                    time.sleep(5)
                elif edit_sel == 5 or edit_sel == None:
                    contacts_menu_back = True
                    print("Back selected")
            contacts_menu_back = False
        elif main_sel == 1:
            print("Welcome to NOTES menu")
            time.sleep(2)
            while not notes_menu_back:
                edit_sel = notes_menu.show()
                if edit_sel == 0:
                    note = input("Add note")
                    print("note: ", note)
                    # Add your handler for add-note operation
                    time.sleep(5)
                elif edit_sel == 1:
                    note_name = input("Show note")
                    print("note: ", note_name)
                    # Add your handler for show-note operation
                    time.sleep(5)
                elif edit_sel == 2:
                    print("Show all notes")
                    # Add your handler for show-all operation
                    time.sleep(5)
                elif edit_sel == 3:
                    note = input("Edit note")
                    print("note: ", note)
                    # Add your handler for adit-note operation
                    time.sleep(5)
                elif edit_sel == 4:
                    note = input("Remove note")
                    print("note: ", note)
                    # Add your handler for remove-note operation
                    time.sleep(5)
                elif edit_sel == 5 or edit_sel == None:
                    contacts_menu_back = True
                    print("Back selected")
            notes_menu_back = False
        elif main_sel == 2 or main_sel == None:
            main_menu_exit = True
            print("Quit Selected")
    save_data(address_book, data_file)


if __name__ == "__main__":
    main()
