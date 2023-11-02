import datetime
import click
from helpers.note_priority import PRIORITIES
from base.record import Record
from base.address_book import AddressBook 


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

birthdays_dict = {}

@click.group()
def cli_commands():
    pass

@click.command()
@click.option("--name", prompt="Name", help="Name of the contact")
@click.option("--birthday", prompt="Birthday (DD.MM.YYYY)", help="Birthday of the contact in format 'DD.MM.YYYY'")
def add_birthday(name, birthday):
    try:
        birthday_date = datetime.datetime.strptime(birthday, "%d.%m.%Y")
        birthdays_dict[name] = birthday_date
        click.echo(f"Birthday added for {name}")
    except ValueError:
        click.echo("Invalid date format. Please use 'DD.MM.YYYY' format for the birthday.")

@click.command()
@click.option("--days", type=int, prompt="Days", help="Number of days")
def birthdays(days):
    today = datetime.datetime.now()
    upcoming_birthdays = []
    
    for name, birthday_date in birthdays_dict.items():
        days_until_birthday = (birthday_date - today).days
        if 0 < days_until_birthday <= days:
            upcoming_birthdays.append(f"{name}: {birthday_date.strftime('%d.%m.%Y')}")
    
    if upcoming_birthdays:
        click.echo(f"Upcoming birthdays in the next {days} days:")
        for birthday_entry in upcoming_birthdays:
            click.echo(birthday_entry)
    else:
        click.echo(f"No upcoming birthdays found in the next {days} days.")

@click.command()
@click.option("--name", prompt="Name", help="Name of the contact")
def remove_birthday(name):
    if name in birthdays_dict:
        del birthdays_dict[name]
        click.echo(f"Birthday removed for {name}")
    else:
        click.echo(f"No birthday found for {name}.")

@click.command()
@click.option("--name", prompt="Name", help="Name of the contact")
@click.option("--new_birthday", prompt="New Birthday (DD.MM.YYYY)", help="New Birthday of the contact in format 'DD.MM.YYYY'")
def edit_birthday(name, new_birthday):
    if name in birthdays_dict:
        try:
            birthday_date = datetime.datetime.strptime(new_birthday, "%d.%m.%Y")
            birthdays_dict[name] = birthday_date
            click.echo(f"Birthday edited for {name}: {birthday_date.strftime('%d.%m.%Y')}.")
        except ValueError:
            click.echo("Invalid date format. Please use 'DD.MM.YYYY' format for the birthday.")
    else:
        click.echo(f"No birthday found for {name}.")
        
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
cli_commands.add_command(add_birthday)
cli_commands.add_command(birthdays)
cli_commands.add_command(remove_birthday)
cli_commands.add_command(edit_birthday)