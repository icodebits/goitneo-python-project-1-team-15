from base.record import Record
from helpers.weekdays import WEEKDAYS, CURRENT_DATE

import re
from datetime import datetime, timedelta
from collections import UserDict, defaultdict


class AddressBook(UserDict):
    def add_record(self, name):
        try:
            contact = Record(name)
            self.data[contact.name.value] = contact
            print("\n🟢 Contact added\n")
        except ValueError as error:
            print(error)

    def edit(self, old_name, new_name):
        if old_name in self.data.keys():
            upd_contact = self.data[old_name].edit_name(new_name)
            self.delete(old_name)
            self.data[new_name] = upd_contact
            print("\n🟢 Contact updated\n")
        else:
            print(f"\n❌ Contact {old_name} not found\n")

    def show(self, name):
        contact = self.find(name)
        print(contact)

    def find(self, name):
        try:
            contact = self.data[name]
            return contact
        except KeyError:
            return f"\n❌ Contact {name.title()} not found\n"

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            return f"\n🟢 Contact '{key}' deleted\n"
        else:
            return f"\n❌ Contact '{key}' not found\n"

    def display_contacts(self):
        contacts = "\n📱 All contacts:"
        for contact in self.data.values():
            contacts += f"\n{contact}\n"
        print(contacts)

    # Phone methods
    def add_phone(self, name, phones):
        contact = self.find(name)
        if isinstance(contact, Record):
            res = contact.add_phone(phones)
            if res is not True:
                print(f"\n{res}\n")
        else:
            print(contact)

    def edit_phone(self, name, old_value, new_value):
        contact = self.find(name)
        if isinstance(contact, Record):
            is_edited = contact.edit_phone(old_value, new_value)
            if is_edited == True:
                print("\n📒 Contact updated\n")
            elif is_edited == False:
                print(f"\n❌ Phone number {old_value} not found\n")
            else:
                print(is_edited)
        else:
            print(contact)

    def show_phone(self, name):
        contact = self.find(name)
        if isinstance(contact, Record):
            phones_list = contact.find_phone()
            print(f"\n✅ Contact phones: {phones_list}\n")
        else:
            print(contact)

    def delete_phone(self, name, phone):
        contact = self.find(name)
        if isinstance(contact, Record):
            is_deleted = contact.remove_phone(phone)
            if is_deleted:
                print(f"\n🟢 Phone number deleted\n")
            else:
                print(f"\n❌ Phone number {phone} not found\n")
        else:
            print(contact)

    # Address methods
    def add_address(self, name, address):
        contact = self.find(name)
        if isinstance(contact, Record):
            contact.add_address(address)
            print("\n🏠 Address added\n")
        else:
            print(contact)

    def edit_address(self, name, new_address):
        contact = self.find(name)
        if isinstance(contact, Record):
            if contact.address:
                if new_address:
                    contact.address.value = " ".join(new_address).strip()
                    print(f"\n🏠 Address updated for {name.title()}\n")
                else:
                    print("\n❌ The address is incorrect\n")
            else:
                print("\n❌ No address to edit\n")
        else:
            print(contact)

    def show_address(self, name):
        contact = self.find(name)
        if isinstance(contact, Record):
            if contact.address:
                print(f"\n🏠 Address for {name.title()}: {contact.address.value.title()}\n")
            else:
                print(f"\n❌ Address not found for {name.title()}\n")
        else:
            print(contact)

    def delete_address(self, name):
        contact = self.find(name)
        if isinstance(contact, Record):
            if contact.address:
                contact.address = None
                print(f"\n🏠 Address deleted for {name.title()}\n")
            else:
                print("\n❌ No address to delete\n")
        else:
            print(contact)

    # Email methods
    def add_email(self, name, email):
        contact = self.find(name)
        if isinstance(contact, Record):
            try:
                contact.add_email(email)
                print("\n✅ Email added\n")
            except ValueError as error:
                print(error)
        else:
            print(contact)

    def edit_email(self, name, old_email, new_email):
        contact = self.find(name)
        if isinstance(contact, Record):
            if old_email in [str(i) for i in contact.emails]:
                try:
                    contact.edit_email(old_email, new_email)
                    print("\n✅ Email updated\n")
                except ValueError as error:
                    print(error)
            else:
                print(f"\n❌ Email {old_email} not found\n")
        else:
            print(contact)

    def show_email(self, name):
        contact = self.find(name)
        if isinstance(contact, Record):
            if contact.emails:
                email_list = "; ".join(str(p) for p in contact.emails)
                print(f"\n✅ Contact emails: {email_list}\n")
            else:
                print("\n❌ Email not found\n")
        else:
            print(contact)

    def delete_email(self, name, email_to_remove):
        contact = self.find(name)
        if isinstance(contact, Record):
            for em in contact.emails:
                if str(em) == email_to_remove:
                    contact.emails.remove(em)
                    print(f"\n🟢 Email deleted\n")
                    return

            print(f"\n❌ Email '{email_to_remove}' not found\n")
        else:
            print(contact)

    # Birthday methods
    def add_birthday(self, name, birthday):
        contact = self.find(name)
        contact.add_birthday(birthday)
        print(f"\n🎂 Birthday added for {name}\n")

    def edit_birthday(self, name, new_birthday):
        contact = self.find(name)
        if contact.birthday:
            if new_birthday:
                contact.birthday.value = new_birthday
                print(f"\n🎂 Birthday updated for {name}\n")
            else:
                print("\n❌ The birthday is incorrect\n")
        else:
            print("\n❌ No birthday to edit\n")

    def show_birthday(self, name):
        contact = self.find(name)
        if contact.birthday:
            print(f"\n🎂 Birthday for {name}: {contact.birthday.value}\n")
        else:
            print(f"\n❌ Birthday not found for {name}\n")

    def delete_birthday(self, name):
        contact = self.find(name)
        if contact.birthday:
            contact.birthday = None
            print(f"\n🎂 Birthday removed for {name}")
        else:
            print("\n❌ No birthday to delete\n")

    def next_birthdays(self, days=7):
        upcoming_birthdays = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                next_birthday = datetime(CURRENT_DATE.year, bday.month, bday.day).date()

                if CURRENT_DATE <= next_birthday <= CURRENT_DATE + timedelta(days=days):
                    upcoming_birthdays[next_birthday].append(name)

        if not upcoming_birthdays:
            print(f"No upcoming birthdays in the next {days} days.")
        else:
            desc = f"Upcoming birthdays in the next {days} days:"
            for next_birthday, names in sorted(upcoming_birthdays.items()):
                day_of_week = WEEKDAYS[next_birthday.weekday()]
                formatted_names = ", ".join(
                    [f"{name} ({next_birthday.strftime('%d.%m.%Y')})" for name in names]
                )
                desc += f"\n{day_of_week}: {formatted_names}"
            print(desc)
