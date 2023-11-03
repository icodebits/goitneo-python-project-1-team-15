welcome = """
=============================
| Welcome to assistant bot: |
=============================
Enter next command to start bot:
    Contacts
    Notes

Enter [exit or close] to finish
"""

leave = """
=========================
| Tnx for using our bot |
=========================
"""

main_menu = """
==============
| Main menu: |
==============
Enter command:
    Contacts
    Notes

Enter [exit or close] to finish
"""


contacts_menu = """
=============================
| Welcome to contacts menu: |
=============================
Usage: COMMAND [ARGS]...
Commands:
    add             <name> or <name> <field> or <name> <field> <value>
    edit            <name> or <name> <field> or <name> <field> <value>
    search          <keywords>
    edit            <name> <field> <old value> <new value>
    delete          <name> or <name> <field>
    show-all        # show all contacts
    add-birthday    <name> <birthday>
    show-birthdays  <days>
    remove-birthday <name>
    edit-birthday   <name> <new_birthday>

    back            # back to prev menu
"""

notes_menu = """
==========================
| Welcome to notes menu: |
==========================
Usage: COMMAND [ARGS]...
Commands:
    add          <note>
    edit         <note_number> <new_text>
    delete       <note_number>
    show         <note_keyword>
    show-all     # show all notes
    add-tags     <note_number> <tag_names>
    search-tags  <note_keywords>
    sort-tags    # sort notes by tag

    back         # back to prev menu
"""

back = "↵ Back selected"

error = "🔴 Invalid command"
