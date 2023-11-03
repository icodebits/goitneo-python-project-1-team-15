from collections import UserDict, defaultdict
from datetime import datetime, timedelta
from base.record import Record
from helpers.weekdays import WEEKDAYS, CURRENT_DATE
import os

class AddressBook(UserDict):
    def add_record(self, contact: dict) -> None:
        self.data[contact.name.value] = contact

    def find(self, key: str) -> object:
        res = self.data.get(key)
        return res

    def delete(self, key: str) -> None:
        del self.data[key]

    def set_birthday(self, name: str, date: str) -> None:
        contact = self.find(name)
        contact.add_birthday(date)

    def show_birthday(self, name: str) -> str:
        contact = self.find(name)

        if contact.birthday:
            return contact.birthday.value
        else:
            raise AttributeError(
                f"The birthday field is missing from {contact.name.value}'s contact"
            )

    def get_birthdays_per_week(self) -> str:
        birthday_dict = defaultdict(list)
        birthdays_info = ""

        for info in self.data.values():
            name = info.name.value.title()
            birthday = datetime.strptime(str(info.birthday), "%d %B %Y")
            birthday = birthday.date()
            birthday_this_year = birthday.replace(year=CURRENT_DATE.year)

            if birthday_this_year < CURRENT_DATE:
                birthday_this_year = birthday.replace(year=CURRENT_DATE.year + 1)

            delta_days = (birthday_this_year - CURRENT_DATE).days

            if delta_days < 7:
                if birthday_this_year.weekday() >= 5:
                    birthday_dict[WEEKDAYS[0]].append(name)
                else:
                    birthday_dict[WEEKDAYS[birthday_this_year.weekday()]].append(name)

        for day, users_list in birthday_dict.items():
            birthdays_info += f"{day}: {', '.join(list(users_list))}\n"

        return birthdays_info

    def add_contact(self, name: str, tags: list):
        contact = Record(name)
        self.add_record(contact)
        print("\n🟢 Contact added\n")


    def search_contact(self, search_query: str):
        contact = self.find(search_query)
        if contact:
            print("\n✅ Contact found:")
            print(contact)
        else:
            print(f"\n❌ Contact '{search_query}' not found\n")
            
    def edit_contact(self, name, field, old_value, new_value):
        contact = self.find(name)
        if contact:
            if field == "name":
                contact.name.value = new_value
            elif field == "phone":
                contact.edit_phone(old_value, new_value)
            else:
                print(f"\n❌ Invalid field: {field}")
                return
            print("\n📒 Contact updated:")
            print(contact)
        else:
            print(f"\n❌ Contact {name} not found\n")

    def delete_contact(self, name):
        contact = self.find(name)
        if contact:
            self.delete(name)
            print(f"\n❌ Contact {name} deleted\n")
        else:
            print(f"\n❌ Contact {name} not found\n")

    def display_contacts(self):
        print("\n📱 All contacts:")
        for contact in self.data.values():
            print(contact)

    def add_birthday(self, contact_name, birthday):
        contact = self.find(contact_name)
        if contact:
            contact.add_birthday(birthday) 
            print(f"\n🎂 Birthday added for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")

    def show_birthdays(self, args):
        if len(args) == 0:
            days = 7
        else:
            try:
                days = int(args[0])
            except ValueError:
                print("Invalid number of days. Please provide a valid integer.")
                return

        today = datetime.now().date()
        upcoming_birthdays = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, '%d.%m.%Y').date()
                next_birthday = datetime(today.year, bday.month, bday.day).date()

                if today <= next_birthday <= today + timedelta(days=days):
                    upcoming_birthdays[next_birthday].append(name)

        if not upcoming_birthdays:
            print(f"No upcoming birthdays in the next {days} days.")
        else:
            print(f"Upcoming birthdays in the next {days} days:")
            for next_birthday, names in sorted(upcoming_birthdays.items()):
                day_of_week = WEEKDAYS[next_birthday.weekday()]
                formatted_names = ", ".join([f"{name} ({next_birthday.strftime('%d.%m.%Y')})" for name in names])
                print(f"{day_of_week}: {formatted_names}")

    def remove_birthday(self, contact_name):
        contact = self.find(contact_name)
        if contact:
            contact.birthday = None 
            print(f"\n🎂 Birthday removed for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")

    def edit_birthday(self, contact_name, new_birthday):
        contact = self.find(contact_name)
        if contact:
            contact.birthday.value = new_birthday 
            print(f"\n🎂 Birthday updated for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")
