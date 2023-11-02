import re
from simple_term_menu import TerminalMenu

def main():
    keywords = [
        "Add contact",
        "Show contact",
        "Show contacts",
        "Edit contact",
        "Remove contact",
        "Add birthday",
        "Search for birthday people",
        "Edit birthday",
        "Delete birthday",
    ]

    while True:
        user_input = input("Enter a sentence: ")

        found_commands = []
        contacts_commands = []
        notes_commands = []

        for keyword in keywords:
            keyword_parts = keyword.split()
            matched = False

            for keyword_part in keyword_parts:
                if re.search(r'\b' + re.escape(keyword_part.lower()) + r'\b', user_input.lower()):
                    matched = True
                    break

            if matched:
                found_commands.append(keyword)

        if "contact" in user_input.lower():
            print("Running the analysis from Analysis.py...")
            print("Possible commands for Contacts menu:")
            contacts_commands = [cmd for cmd in found_commands if "contact" in cmd.lower()]
            contacts_menu = TerminalMenu(contacts_commands, title="Contacts menu", cycle_cursor=True)
            contacts_sel = contacts_menu.show()

            if contacts_sel is not None:
                handle_contacts_command(contacts_commands[contacts_sel])
        else:
            print("No matching commands for Contacts menu.")

        if "note" in user_input.lower():
            print("Possible commands for Notes menu:")
            notes_commands = [cmd for cmd in found_commands if "note" in cmd.lower()]
            notes_menu = TerminalMenu(notes_commands, title="Notes menu", cycle_cursor=True)
            notes_sel = notes_menu.show()

            if notes_sel is not None:
                handle_notes_command(notes_commands[notes_sel])
        else:
            print("No matching commands for Notes menu.")

        restart = input("Start over? (yes/no): ")
        if restart.lower() != "yes":
            return

def handle_contacts_command(command):
    print(f"You selected: {command}")
    # Додайте логіку для обробки команд для Contacts menu тут

def handle_notes_command(command):
    print(f"You selected: {command}")
    # Додайте логіку для обробки команд для Notes menu тут

if __name__ == "__main__":
    main()
