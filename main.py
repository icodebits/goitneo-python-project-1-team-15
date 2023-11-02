from simple_term_menu import TerminalMenu
import time
from base.Analysis import main as analysis_main


def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Contatcs", "Notes", "Smart terminal", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

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
                elif edit_sel == 1:
                    contact_name = input("Show contact by name: ")
                    print("name: ", contact_name)
                    # Add your handler for show-name operation
                    time.sleep(5)
                elif edit_sel == 2:
                    print("Show all contacts")
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
        elif main_sel == 2:
            print("Running the analysis from Analysis.py...")
            found_commands = analysis_main() 
            if found_commands:
                if "Contacts" in main_menu_items:
                    smart_menu_items_contacts = [btn for btn in contacts_menu_items if any(keyword in btn for keyword in found_commands)]
                    if smart_menu_items_contacts:
                        smart_menu_contacts = TerminalMenu(
                            menu_entries=smart_menu_items_contacts,
                            title="Contacts menu",
                            menu_cursor=main_menu_cursor,
                            menu_cursor_style=main_menu_cursor_style,
                            menu_highlight_style=main_menu_style,
                            cycle_cursor=True,
                            clear_screen=True,
                        )
                        selected_contacts = smart_menu_contacts.show()
                if "Notes" in main_menu_items:
                    smart_menu_items_notes = [btn for btn in notes_menu_items if any(keyword in btn for keyword in found_commands)]
                    if smart_menu_items_notes:
                        smart_menu_notes = TerminalMenu(
                            menu_entries=smart_menu_items_notes,
                            title="Notes menu",
                            menu_cursor=main_menu_cursor,
                            menu_cursor_style=main_menu_cursor_style,
                            menu_highlight_style=main_menu_style,
                            cycle_cursor=True,
                            clear_screen=True,
                        )
                        selected_notes = smart_menu_notes.show()
            else:
                print("No matching commands found in Smart menu.")
            time.sleep(2)
        elif main_sel == 3 or main_sel == None:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()
