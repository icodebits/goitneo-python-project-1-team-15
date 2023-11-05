from base.record import Record
from helpers.weekdays import WEEKDAYS, CURRENT_DATE

import re
from datetime import datetime, timedelta
from collections import UserDict, defaultdict


class AddressBook(UserDict):
    def add_record(self, name):
        contact = Record(name)
        self.data[contact.name.value] = contact
        print("\n🟢 Contact added")
            

    def edit(self, old_name, new_name):
        if old_name.lower() in self.data:
            contact = self.data[old_name.lower()]
        if not contact:
            print(f"\n❌ Contact {old_name} not found")
        else:
            contact.edit_name(new_name)
            print("\n🟢 Contact updated")
            

    def find(self, key):
        key = key.lower()
        contact = self.data.get(key)
        if not contact:
            print(f"\n❌ Contact {key} not found")
        else:
            print(self.data.get(key))           
    

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            print(f"\n🟢 Contact '{key}' deleted")
        else:
            print(f"\n❌ Contact '{key}' not found")
            

    def display_contacts(self):
        contacts = "\n📱 All contacts:"
        for contact in self.data.values():
            contacts += f"\n{contact}"
        return contacts

    # Phone methods
    # def add_phone(self, name, phones):
    #     if name.lower() in self.data:
    #         contact = self.data[name.lower()]
    #         contact.add_phone(phones)
    #         print("\n✅ Phone added")
    #     else:
    #         print(f"\n❌ Contact '{name}' not found")

    def add_phone(self, name, phones):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            
            stripped_phones = ''.join(filter(str.isdigit, phones))

            if len(stripped_phones) == 10:
                contact.add_phone(phones)
                print("\n✅ Phone added")
            else:
                print("\n❌ Phone should contain 10 consecutive digits.")
        else:
            return f"\n❌ Contact '{name}' not found"


    def edit_phone(self, name, old_value, new_value):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if old_value not in [str(p) for p in contact.phones]:
                print(f"\n❌ Phone number {old_value} not found")
            else:
                contact.edit_phone(old_value, new_value)
                print("\n📒 Contact updated")
        else:
            print(f"\n❌ Contact {name} not found")

    def show_phone(self, search_query):
        contact = self.find(search_query)
        if contact:
            phone_list = "; ".join(str(p) for p in contact.phones)
            return f"\n✅ Contact phones: {phone_list}"
        else:
            return f"\n❌ Contact '{search_query}' not found\n"

    def delete_phone(self, name, phone):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if phone not in [str(p) for p in contact.phones]:
                print(f"\n❌ Phone number {phone} not found")
            else:
                contact.remove_phone(phone)
                print(f"\n🟢 Contact phone deleted\n")
        else:
            print(f"\n❌ Contact {name} not found\n")

    # Address methods
    def add_address(self, name, address):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            address = " ".join(address).strip()
            contact.add_address(address)
            print("\n🏠 Address added")
        else:
            print(f"\n❌ Contact '{name}' not found")
        

    def edit_address(self, name, new_address):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact.address:
                if new_address:
                    contact.address = " ".join(new_address).strip()
                    print(f"\n🏠 Address updated for {name}")
                else:
                    print("❌ The address is incorrect")
            else:
                print("❌ No address to edit")
        else:
            print(f"\n❌ Contact '{name}' not found")

    def show_address(self, name):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                if contact.address:
                    print(f"\n🏠 Address for {name}: {contact.address}")
                else:
                    print(f"\n❌ Address not found for {name}")
        else:
            print(f"\n❌ Contact '{name}' not found")

    def delete_address(self, name):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                if contact.address:
                    contact.address = None
                    print(f"\n🏠 Address deleted for {name}\n")
                else:
                    print("❌ No address to delete")
        else:
            print(f"\n❌ Contact '{name}' not found")


    # Email methods
    def add_email(self, name, email):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            contact.add_email(email)
            print("\n✅ Email added")
        else:
            print(f"\n❌ Contact '{name}' not found")
        

    def edit_email(self, name, old_email, new_email):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                if old_email in [str(i) for i in contact.emails]:
                    pattern = re.compile(r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}")
                    if re.match(pattern, new_email):
                        contact.edit_email(old_email, new_email)
                        print("✅ Email updated")
                    else:
                        print("❌ Wrong email format")
                else:
                    print(f"❌ Email {old_email} not found")
        else:
            print(f"\n❌ Contact '{name}' not found")

    def show_email(self, name):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                if contact.emails:
                    email_list = "; ".join(str(p) for p in contact.emails)
                    print(f"\n✅ Contact emails: {email_list}")
                else:
                    print("❌ Email not found")
        else:
            print(f"\n❌ Contact '{name}' not found\n")
        

    def delete_email(self, name, email_to_remove):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                emails = contact.emails
                for em in emails:
                    if str(em) == email_to_remove:
                        contact.emails.remove(em)
                        print(f"\n🟢 Email deleted\n")
                print(f"❌ Email '{email_to_remove}' not found")
        else:
            print(f"\n❌ Contact {name} not found\n")


    # Birthday methods
    def add_birthday(self, contact_name, birthday):
        if contact_name.lower() in self.data:
            contact = self.data[contact_name.lower()]
            contact.add_birthday(birthday)
            print(f"\n🎂 Birthday added for {contact_name}")
        else:
            print(f"\n❌ Contact '{contact_name}' not found")


    def edit_birthday(self, contact_name, new_birthday):
        if contact_name.lower() in self.data:
            contact = self.data[contact_name.lower()]
            if contact.birthday:
                if new_birthday:
                    contact.birthday.value = new_birthday
                    print(f"\n🎂 Birthday updated for {contact_name}")
                else:
                    print("❌ The birthday is incorrect")
            else:
                print("❌ No birthday to edit")
        else:
            print(f"\n❌ Contact {contact_name} not found")


    def show_birthday(self, name):
        if name.lower() in self.data:
            contact = self.data[name.lower()]
            if contact:
                if contact.birthday:
                    print(f"\n🎂 Birthday for {name}: {contact.birthday.value}")
                else:
                    print(f"\n❌ Birthday not found for {name}")
        else:
            print(f"\n❌ Contact '{name}' not found")


    def delete_birthday(self, contact_name):
        if contact_name.lower() in self.data:
            contact = self.data[contact_name.lower()]
            if contact:
                if contact.birthday:
                    contact.birthday = None
                    print(f"\n🎂 Birthday removed for {contact_name}")
                else:
                    print("❌ No birthday to delete")
        else:
            print(f"\n❌ Contact '{contact_name}' not found")


    def next_birthdays(self, days=7):
        today = datetime.now().date()
        upcoming_birthdays = defaultdict(list)

        for name, record in self.data.items():
            if record.birthday:
                bday = datetime.strptime(record.birthday.value, "%d.%m.%Y").date()
                next_birthday = datetime(today.year, bday.month, bday.day).date()

                if today <= next_birthday <= today + timedelta(days=days):
                    upcoming_birthdays[next_birthday].append(name)

        if not upcoming_birthdays:
            return f"No upcoming birthdays in the next {days} days."
        else:
            desc = f"Upcoming birthdays in the next {days} days:"
            for next_birthday, names in sorted(upcoming_birthdays.items()):
                day_of_week = WEEKDAYS[next_birthday.weekday()]
                formatted_names = ", ".join(
                    [f"{name} ({next_birthday.strftime('%d.%m.%Y')})" for name in names]
                )
                desc += f"\n{day_of_week}: {formatted_names}"
            return desc
