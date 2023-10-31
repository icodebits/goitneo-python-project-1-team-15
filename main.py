import click
from helpers.note_priority import PRIORITIES


@click.group()
def cli_commands():
    ...


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}")


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
            f"{name}: {desc} [Priority: {PRIORITIES[priority]}]"
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

if __name__ == "__main__":
    cli_commands()
