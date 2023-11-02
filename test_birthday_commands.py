import datetime
import pytest
from click.testing import CliRunner
from cli import add_birthday, birthdays, remove_birthday, edit_birthday

test_birthday_data = [
    ("John", "03.11.2000"),
    ("Max", "05.11.1995"),
    ("Alice", "10.11.1980"),
]

def test_add_birthday():
    runner = CliRunner()
    for name, birthday in test_birthday_data:
        result = runner.invoke(add_birthday, input=f"{name}\n{birthday}\n", catch_exceptions=False)
        assert result.exit_code == 0
        assert f"Birthday added for {name}" in result.output

def test_birthdays():
    runner = CliRunner()
    with runner.isolated_filesystem():
        today = datetime.datetime(2023, 11, 2)
        with open("birthdays.txt", "w") as file:
            for name, birthday in test_birthday_data:
                file.write(f"{name}: {birthday}\n")

        result = runner.invoke(birthdays, ["3"], catch_exceptions=False)
        assert result.exit_code == 0
        assert "Upcoming birthdays in the next 3 days:" in result.output
        assert "John: 03.11.2000" in result.output
        assert "Max: 05.11.1995" in result.output
        assert "Alice: 10.11.1980" not in result.output

def test_remove_birthday():
    runner = CliRunner()
    for name, _ in test_birthday_data:
        result = runner.invoke(remove_birthday, [name], catch_exceptions=False)
        assert result.exit_code == 0
        assert f"Birthday removed for {name}" in result.output

def test_edit_birthday():
    runner = CliRunner()
    new_birthday = "02.11.1990"
    for name, _ in test_birthday_data:
        result = runner.invoke(edit_birthday, [name, new_birthday], catch_exceptions=False)
        assert result.exit_code == 0
        assert f"Birthday edited for {name}: {new_birthday}" in result.output
