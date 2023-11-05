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
    add                <name>
    edit               <name> <new_name>
    delete             <name>
    find               <name>
    show-all           # show all contacts

    add-phone          <name> <phone>
    edit-phone         <name> <old_phone> <new_phone>
    show-phone         <name>
    delete-phone       <name> <phone>

    add-address        <name> <address>
    edit-address       <name> <old_address> <new_address>
    show-address       <name>
    delete-address     <name> <address>

    add-email          <name> <email>
    edit-email         <name> <old_email> <new_email>
    show-email         <name>
    delete-email       <name> <email>

    add-birthday       <name> <birthday>
    edit-birthday      <name> <old_birthday> <new_birthday>
    show-birthday      <name>
    delete-birthday    <name>
    next-birthdays     <days>

    analyze            # open analyze menu

    back               # back to prev menu
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

    analyze      # open analyze menu

    back         # back to prev menu
"""

back = "↵ Back selected"

error = "🔴 Invalid command"
empty_params = "🟡 Please select an option"
