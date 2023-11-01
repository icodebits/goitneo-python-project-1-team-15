import click
from helpers.note_priority import PRIORITIES


@click.group()
def cli_commands():
    ...


@click.command()
def hello():
    click.echo("Welcome to the assistant bot!")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=0)
@click.option(
    "-n", "--name", prompt="Enter the note name", help="The name of the note item"
)
@click.option(
    "-d", "--desc", prompt="Describe the note", help="The description of the note item"
)
def add_note(name, desc, priority, todofile):
    filename = todofile if todofile is not None else "mynotes.txt"
    with open(filename, "a+") as file:
        file.write(
            f"{name}: {desc} [Priority: {PRIORITIES[priority]}]\n"
        )  # format output if needed


@click.command()
@click.argument("idx", type=int, required=1)
def delete_note(idx):
    with open("mynotes.txt", "r") as file:
        notes_list = file.read().splitlines()
        notes_list.pop(idx)
    with open("mynotes.txt", "w") as file:
        file.write("\n".join(notes_list))
        file.write("\n")


@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=False), required=0)
def list_notes(
    priority,
    todofile,
):
    filename = todofile if todofile is not None else "mynotes.txt"
    with open(filename, "r") as file:
        notes_list = file.read().splitlines()

        if priority is None:
            for idx, note in enumerate(notes_list):
                print(f"{idx} - {note}")
        else:
            for idx, note in enumerate(notes_list):
                if f"[Priority: {PRIORITIES[priority]}]" in note:
                    print(f"{idx} - {note}")  # format output if needed


cli_commands.add_command(hello)
cli_commands.add_command(add_note)
cli_commands.add_command(delete_note)
cli_commands.add_command(list_notes)

"""
CLI menu interface
"""

from simple_term_menu import TerminalMenu
import time


def main():
    main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
    main_menu_items = ["Contatcs", "Notes", "Quit"]
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
        elif main_sel == 2 or main_sel == None:
            main_menu_exit = True
            print("Quit Selected")
