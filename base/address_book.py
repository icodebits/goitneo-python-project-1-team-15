from base.record import Record
from helpers.weekdays import WEEKDAYS, CURRENT_DATE

import re
from datetime import datetime, timedelta
from collections import UserDict, defaultdict


class AddressBook(UserDict):
    def add_record(self, name):
        contact = Record(name)
        self.data[contact.name.value] = contact

    def edit(self, old_name, new_name):
        contact = self.find(old_name)
        contact.edit_name(new_name)
        return "\n🟢 Contact updated"

    def find(self, key):
        key = key.lower()
        return self.data.get(key)

    def delete(self, key):
        del self.data[key]

    def display_contacts(self):
        contacts = "\n📱 All contacts:"
        for contact in self.data.values():
            contacts += f"\n{contact}"
        return contacts

    # Phone methods
    def add_phone(self, name, phones):
        contact = self.find(name)
        res = contact.add_phone(phones)
        return res

    def edit_phone(self, name, old_value, new_value):
        contact = self.find(name)
        if contact:
            contact.edit_phone(old_value, new_value)
            return "\n📒 Contact updated"
        else:
            return f"\n❌ Contact {name} not found"

    def show_phone(self, search_query):
        contact = self.find(search_query)
        if contact:
            phone_list = "; ".join(str(p) for p in contact.phones)
            return f"\n✅ Contact phones: {phone_list}"
        else:
            return f"\n❌ Contact '{search_query}' not found\n"

    def delete_phone(self, name, phone):
        contact = self.find(name)
        if contact:
            res = contact.remove_phone(phone)
            if res:
                return f"\n🟢 Contact phone deleted\n"
            else:
                return f"\n❌ Contact phone not found\n"
        else:
            return f"\n❌ Contact {name} not found\n"

    # Address methods
    def add_address(self, name, address):
        contact = self.find(name)
        if contact:
            address = " ".join(address).strip()
            contact.add_address(address)
            return "The address is added"
        else:
            return f"\n❌ Contact {name} not found\n"

    def edit_address(self, name, new_address):
        contact = self.find(name)
        if contact:
            if contact.address:
                if new_address.strip():
                    contact.address = new_address
                    return f"\n✅ Address updated for {name}"
                else:
                    return "❌ The address is incorrect"
            else:
                return "❌ No address to edit"
        else:
            return "❌ User not found"

    def show_address(self, name):
        contact = self.find(name)
        if contact:
            if contact.address:
                return f"\n✅ Address for {name}: {contact.address}"
            else:
                return f"\n❌ Address not found for {name}"
        else:
            return "❌ User not found"

    def delete_address(self, name):
        contact = self.find(name)
        if contact:
            if contact.address:
                contact.address = None
                return f"\n✅ Address removed for {name}\n"
            else:
                return "❌ No address to remove"
        else:
            return "❌ User not found"

    # Email methods
    def add_email(self, name, email):
        contact = self.find(name)
        if contact:
            res = contact.add_email(email)
            return res
        else:
            return "❌ User not found"

    def edit_email(self, name, old_email, new_email):
        contact = self.find(name)
        if contact:
            if old_email in [str(i) for i in contact.emails]:
                pattern = re.compile(r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}")
                if re.match(pattern, new_email):
                    contact.edit_email(old_email, new_email)
                    return "✅ Email updated"
                else:
                    return "❌ Wrong email format"
            else:
                return f"❌ Email {old_email} not found"
        else:
            return "❌ User not found"

    def show_email(self, name):
        contact = self.find(name)
        if contact:
            if contact.emails:
                email_list = "; ".join(str(e) for e in contact.emails)
                return f"✅ Email is: {email_list}"
            else:
                return "❌ Email not found"
        else:
            return "❌ User not found"

    def delete_email(self, name, email_to_remove):
        contact = self.find(name)
        if contact:
            emails = contact.emails
            for em in emails:
                if str(em) == email_to_remove:
                    contact.emails.remove(em)
                    return f"✅ Email removed from the contact"
            return f"❌ Email '{email_to_remove}' not found"
        else:
            return "❌ User not found"

    # Birthday methods
    def add_birthday(self, contact_name, birthday):
        contact = self.find(contact_name)
        if contact:
            contact.add_birthday(birthday)
            return f"\n🎂 Birthday added for {contact_name}"
        else:
            return f"\n❌ Contact {contact_name} not found"

    def edit_birthday(self, contact_name, new_birthday):
        contact = self.find(contact_name)
        if contact:
            contact.birthday.value = new_birthday
            return f"\n🎂 Birthday updated for {contact_name}"
        else:
            return f"\n❌ Contact {contact_name} not found"

    def show_birthday(self, name):
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
            return f"\n🎂 Birthday removed for {contact_name}"
        else:
            return f"\n❌ Contact {contact_name} not found"

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
