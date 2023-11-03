from base.record import Record
from helpers.weekdays import WEEKDAYS, CURRENT_DATE

import re
from datetime import datetime, timedelta
from collections import UserDict, defaultdict


class AddressBook(UserDict):
    def add_record(self, contact: dict) -> None:
        self.data[contact.name.value] = contact

    def find(self, key: str) -> object:
        key = key.lower()
        res = self.data.get(key)
        return res

    def delete(self, key: str) -> None:
        del self.data[key]

    # Contacts methods
    def add_contact(self, name: str, tags: list):
        contact = Record(name)
        self.add_record(contact)
        print("\n🟢 Contact added\n")

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

    def show_contact(self, search_query: str):
        contact = self.find(search_query)
        if contact:
            print("\n✅ Contact found:")
            print(contact)
        else:
            print(f"\n❌ Contact '{search_query}' not found\n")

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

    # Address methods
    def add_address(self, name: str, address: str) -> None:
        contact = self.find(name)
        if contact:
            if address.strip():
                contact.add_address(address)
                return "The address is added"
            else:
                return "The address is incorrect"
        else:
            return "User not found"

    def edit_address(self, name: str, new_address: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                if new_address.strip():
                    contact.address = new_address
                else:
                    return "The address is incorrect"
            else:
                return "No address to edit"
        else:
            return "User not found"

    def show_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                return f"The address is: {contact.address}"
            else:
                return "Address not found"
        else:
            return "User not found"

    def delete_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                contact.address = None
                return "Address removed"
            else:
                return "No address to remove"
        else:
            return "User not found"

    # Email methods
    def add_email(self, name: str, email: str) -> None:
        contact = self.find(name)
        if contact:
            if email.strip():
                contact.add_email(email)
                return "Email is added"
            else:
                return "Empty value, give me email"
        else:
            return "User not found"

    def edit_email(self, name: str, old_email: str, new_email: str) -> None:
        contact = self.find(name)
        if contact:
            if old_email in [str(i) for i in contact.emails]:
                pattern = re.compile(r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}")
                if re.match(pattern, new_email):
                    contact.edit_email(old_email, new_email)
                    return "Email updated"
                else:
                    return "Wrong email format"
            else:
                return f"Email {old_email} not found"
        else:
            return "User not found"

    def show_email(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.emails:
                email_str = [str(email) for email in contact.emails]
                return f"Email is: {email_str}"
            else:
                return "Email not found"
        else:
            return "User not found"

    def delete_email(self, name: str, email_to_remove: str) -> None:
        contact = self.find(name)
        if contact:
            emails = contact.emails
            for em in emails:
                if str(em) == email_to_remove:
                    contact.emails.remove(em)
                    return f"Email removed from the contact"
            return f"Email '{email_to_remove}' not found"
        else:
            return "User not found"

    # Birthday methods
    def add_birthday(self, name: str, date: str) -> None:
        contact = self.find(name)
        contact.add_birthday(date)

    def add_birthday(self, contact_name, birthday):
        contact = self.find(contact_name)
        if contact:
            contact.add_birthday(birthday)
            print(f"\n🎂 Birthday added for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")

    def edit_birthday(self, contact_name, new_birthday):
        contact = self.find(contact_name)
        if contact:
            contact.birthday.value = new_birthday
            print(f"\n🎂 Birthday updated for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")

    def show_birthday(self, name: str) -> str:
        contact = self.find(name)

        if contact.birthday:
            return contact.birthday.value
        else:
            raise AttributeError(
                f"The birthday field is missing from {contact.name.value}'s contact"
            )

    def delete_birthday(self, contact_name):
        contact = self.find(contact_name)
        if contact:
            contact.birthday = None
            print(f"\n🎂 Birthday removed for {contact_name}\n")
        else:
            print(f"\n❌ Contact {contact_name} not found\n")

    def get_birthdays_per_week(self) -> str:
        birthday_dict = defaultdict(list)
        birthdays_info = ""

    def edit_address(self, name: str, new_address: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                if new_address.strip():
                    contact.address = new_address
                    print(f"\n✅ Address updated for {name}\n")
                else:
                    print("❌ The address is incorrect")
            else:
                print("❌ No address to edit")
        else:
            print("❌ User not found")

    def show_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                print(f"\n✅ Address for {name}: {contact.address}")
            else:
                print(f"\n❌ Address not found for {name}")
        else:
            print("❌ User not found")

    def remove_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                contact.address = None
                print(f"\n✅ Address removed for {name}\n")
            else:
                print("❌ No address to remove")
        else:
            print("❌ User not found")

    def add_email(self, name: str, email: str) -> None:
        contact = self.find(name)
        if contact:
            if email.strip():
                contact.add_email(email)
                print(f"\n✅ Email added for {name}\n")
            else:
                print("❌ Empty value, please provide an email")
        else:
            print("❌ User not found")

    def edit_email(self, name: str, old_email: str, new_email: str) -> None:
        contact = self.find(name)
        if contact:
            if old_email in [str(i) for i in contact.emails]:
                pattern = re.compile(r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}")
                if re.match(pattern, new_email):
                    contact.edit_email(old_email, new_email)
                    print(f"\n✅ Email updated for {name}\n")
                else:
                    print("❌ Wrong email format")
            else:
                print(f"❌ Email '{old_email}' not found for {name}")
        else:
            print("❌ User not found")

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
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                next_birthday = datetime(today.year, bday.month, bday.day).date()

                if today <= next_birthday <= today + timedelta(days=days):
                    upcoming_birthdays[next_birthday].append(name)

        if not upcoming_birthdays:
            print(f"No upcoming birthdays in the next {days} days.")
        else:
            print(f"Upcoming birthdays in the next {days} days:")
            for next_birthday, names in sorted(upcoming_birthdays.items()):
                day_of_week = WEEKDAYS[next_birthday.weekday()]
                formatted_names = ", ".join(
                    [f"{name} ({next_birthday.strftime('%d.%m.%Y')})" for name in names]
                )
                print(f"{day_of_week}: {formatted_names}")


# book = AddressBook()

# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)
# book.add_address("john", "Kyiv")
# print(book.add_email("John", "hh@kk.co"))
# book.add_email("John", "ww@rr.co")

# book.edit_email("John","hh@kk.co", "pp@uiu.co")
# book.show_email("John")
# book.remove_email("John", "pp@uiu.co")
# for name, record in book.data.items():
#     print(record)

# print("The address is edited")
# book.edit_address("John", "Lviv")
# for name, record in book.data.items():
#     print(record)

# john = book.show_address("John")
# print(john)
# john1 = book.remove_address("John")
# print(john1)
# for name, record in book.data.items():
#     print(record)

# print("New address is added")
# book.add_address("John", "Poltava")
# for name, record in book.data.items():
#     print(record)
