import click
from helpers.note_priority import PRIORITIES
from main import address_book
from helpers.weekdays import CURRENT_DATE

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

@click.command()
@click.argument("name")
@click.argument("new_date")
def edit_birthday(name, new_date):
    address_book.edit_birthday(name, new_date)
    click.echo(f"The birthday for {name} has been updated to {new_date}")

@click.command()
@click.argument("name")
def delete_birthday(name):
    address_book.delete_birthday(name)
    click.echo(f"The birthday for {name} has been deleted")

@click.command()
@click.argument("days", type=int)
def birthdays(days):
    result = address_book.show_birthdays_in_next_days(days)
    click.echo(result)

@click.command()
@click.argument("name", prompt="Enter the contact's name")
@click.argument("birthday", prompt="Enter the birthday (DD.MM.YYYY)")
def add_birthday(name, birthday):
    contact = Record(name)
    contact.add_birthday(birthday)
    address_book.add_record(contact)
    click.echo(f"Birthday for {name} has been added.")

cli_commands.add_command(hello)
cli_commands.add_command(add_note)
cli_commands.add_command(delete_note)
cli_commands.add_command(list_notes)
cli_commands.add_command(birthdays)
cli_commands.add_command(edit_birthday)
cli_commands.add_command(delete_birthday)
cli_commands.add_command(add_birthday)
