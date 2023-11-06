# CLI Contact List and Notes App
## GoIT Neo Project 1 - Team 15
    CommandCraft: Where teams become reality

## Description

The CLI Contact List and Notes App is a command-line tool designed to help you manage your contacts and take notes efficiently. It provides a simple and intuitive interface to add, view, update, and delete contacts, as well as create and organize notes.

## Features

- Manage your contact list:
  - Add new contacts with name, phone number, email, address and birthday.
  - View a list of all your contacts.
  - Update existing contacts' information.
  - Delete contacts from your list.
  - View list of contacts that have birthday for the next N days.

- Create and manage notes:
  - Create and save notes.
  - List all your notes.
  - Read and edit individual notes.
  - Delete notes when they are no longer needed.
  - Find notes by a keyword.
  - Add and remove tags to the individual notes.
  - Perform filtering based on tags.
  - Sort notes by tag.

- Local storage
    - App saves the data in a file on the user's hard drive.
    - Saved data is retrieved on the restarting of the app.

## Installation

To use the CLI Contact List and Notes App, you'll need to follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/icodebits/project-pyteam15.git
   ```

2. **Install dependences:**

    ```bash
    cd project-pyteam15
    python3 -m pip install colorama
    python3 -m pip install termcolor
    ```

3. **Run the App:**

    ```bash
    cd project-pyteam15
    python3 main.py
    ```

## Usage

The app provides a set of commands to interact with your contact list and notes.   
App has an interactive menu that helps you write correct commands:

### Contacts commands
| Command                                               | Description                                               |
| ---                                                   | ---                                                       |
| 🗂️ __Contact Commands__                               |                                                           |
| `add <name>`                                          | Add a new contact to your list.                           |
| `edit <name> <new_name>`                              | Edit name of the contact.                                 |
| `delete <name>`                                       | Delete a contact from your list.                          |
| `find <name>`                                         | Search a contact from your list.                          |
| `show-all`                                            | View a list of all your contacts.                         |
| ☎️ __Phone Commands__                                  |                                                           |
| `add-phone <name> <phone>`                            | Add a phone number(s) to the contact.                     | 
| `edit-phone <name> <old_phone> <new_phone>`           | Change a phone number(s) for a contact.                   |
| `show-phone <name>`                                   | Show a phone number(s) of a contact.                      |
| `delete-phone <name> <phone>`                         | Delete a phone number from a contact.                     | 
| 🏠 __Address Commands__                               |                                                           |
| `add-address <name> <address>`                        | Add an address to the contact.                            |
| `edit-address <name> <old_address> <new_address>`     | Change the address of the contact.                        |
| `show-address <name>`                                 | Show the address of the contact.                          |
| `delete-address <name> <address>`                     | Delete the address of the contcat.                        |
| ✉️ __Email Commands__                                  |                                                           |
| `add-email <name> <email>`                            | Add an e-mail to the contact.                             |
| `edit-email <name> <old_email> <new_email>`           | Change the e-mail of the contact.                         |
| `show-email <name>`                                   | Show the e-mail of the contact.                           |
| `delete-email <name> <email>`                         | Delete the address of the contcat.                        |
| 🎂 __Birthday Commands__                              |                                                           |
| `add-birthday <name> <birthday>`                      | Add a birthday of the contact.                            |
| `edit-birthday <name> <old_birthday> <new_birthday>`  | Change the birthday of the contact.                       |
| `show-birthday <name>`                                | Show the birthday of the contact.                         |
| `delete-birthday <name> <birthday>`                   | Delete the birthday of the contcat.                       |
| `next-birthdays <days>`                               | Show contacts that have their birthday within next N days |
| 🤔 __Menu Analyze__                                   |                                                           |   
| `analyze`                                             | Helps users determine relevant commands based on their input within the Contact   |
| 📋 __Menu Commands__                                  |                                                           |
| `back`                                                | Go back to previouse menu.                                |

### Notes commands
| Command                                               | Description                                               |
| ---                                                   | ---                                                       |
| 📝 __Notes Commands__                                 |                                                           |
| `add <note>`                                          | Create and save a new note.                               |
| `edit <note_number> <new_text>`                       | Edit the content of a specific note.                      | 
| `delete <note_number>`                                | Delete a note from your notes.                            | 
| `show <note_keyword>`                                 | Find the notes by the keyword.                            | 
| `show-all`                                            | Show all notes                                            | 
| `add-tags <note_number> <tag_names>`                  | Add tags to a specific note.                              | 
| `search-tags <note_keywords>`                         | Find the notes by the tag.                                | 
| `sort-tags`                                           | Sort notes by a tag.                                      | 
| 🤔 __Menu Analyze__                                   |                                                           |
| `analyze`                                             | Helps users determine relevant commands based on their input within the Notes |
| 📋 __Menu Commands__                                  |                                                           |
| `back`                                                | Go back to previouse menu.                                |

## Examples
*   In contacts menu
    ```
    add John
    add-phone John 1234567890
    show-all

    >>> 
    ```
*   In notes menu
    ```
    add Buy milk
    add-tags 1 shopping
    show-all

    >>> All notes:
    >>> 1. Buy milk - Tags: shopping
    ```
*   In analytics
    ```
     >>> analyze
     >>> I met a wonderful guy today, and he gave me his phone number
    Possible commands with the maximum number of matches:
    add-phone <name> <phone>
    edit-phone <name> <old_phone> <new_phone>
    show-phone <name>
    delete-phone <name> <phone>
    Do you see the command you wanted to use?
    If not, please copy your text and the desired command, and describe what you wanted or the command.
    If you want to add information for a new user, start by using the command 'add'.
    We will be waiting for your response via email at helpapplicationmc3@gmail.com
     >>> add Igor

    🟢 Contact added
     >>> add-phone Igor 0948767780

    ✅ Phone added
     >>>  show-all  
     ```
## Support and Contribution

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/icodebits/project-pyteam15/issues).  
Contributions are also welcome via [pull requests](https://github.com/icodebits/project-pyteam15/pulls).  
You can write an [email](mailto:helpapplicationmc3@gmail.com) to address support issues.

## License

This CLI Contact List and Notes App is open-source software licensed under the [MIT License](./LICENSE).

## Acknowledgements

Special thanks to the CommandCraft Team for making this app possible.
<br>
<br>
<br>
__Happy managing your contacts and notes with the CLI Contact List and Notes App!__ 📝 ☎️