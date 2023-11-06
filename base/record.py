from base.name import Name
from base.phone import Phone
from base.email import Email
from base.address import Address
from base.birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []

    def edit_name(self, new_name):
        self.name = Name(new_name)
        return self

    def add_phone(self, phones):
        found = {}
        for ph in phones:
            found[str(ph)] = False
            for p in self.phones:
                if str(p) == str(ph):
                    found[str(ph)] = True

        for key, value in found.items():
            if value is False:
                try:
                    next_phone = Phone(key)
                    self.phones.append(next_phone)
                    print(f"\n✅ Phone {key} added\n")
                except ValueError as error:
                    return error
            else:
                print(f"\n❌ Number {key} is already in the list\n")
        
        return True

    def edit_phone(self, edit_number, new_number):
        idx_num = None

        try:
            new_phone = Phone(new_number)
        except ValueError as error:
            return error
        
        for p in self.phones:
            if p.value == edit_number:
                idx_num = self.phones.index(p)
                self.phones[idx_num] = new_phone
                idx_num = True
                break

        return True if idx_num else False

    def find_phone(self):
        return "; ".join(str(phone) for phone in self.phones)

    def remove_phone(self, phone_number):
        idx_num = None

        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                idx_num = True
                break

        return True if idx_num else False

    def add_birthday(self, date):
        self.birthday = Birthday(date)
    
    def edit_birthday(self, date):
        self.birthday = Birthday(date)

    def add_address(self, address):
        address = " ".join(address)
        if self.address is not None:
            self.address.value = address
        else:
            self.address = Address(address)

    def add_email(self, emails):
        for email in emails:
            if email in self.emails:
                continue

            next_email = Email(email)
            self.emails.append(next_email)

    def edit_email(self, old, new):
        new_email = Email(new)
        old_email = Email(old)
        self.emails = [new_email.value if str(i) == old_email.value else i for i in self.emails]

    def __str__(self):
        name = self.name.value.title()
        phones = "; ".join(p.value for p in self.phones) if self.phones else "empty"
        birthday = self.birthday if self.birthday else "empty"
        address = self.address.value.title() if self.address else "empty"
        email = "; ".join(str(p) for p in self.emails) if self.emails else "empty"

        return f"""
        📱 Contact info:
            ● name: {name}
            ● phones: {phones}
            ● birthday: {birthday}
            ● address: {address}
            ● email: {email}
        """
