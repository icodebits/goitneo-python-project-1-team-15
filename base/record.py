from base.email import Email
from base.name import Name
from base.phone import Phone
from base.birthday import Birthday
from base.address import Address


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        idx_num = self.phones.index(Phone(phone_number))
        self.phones.pop(idx_num)
        return self.phones

    def edit_phone(self, edit_number, new_number):
        for p in self.phones:
            if p.value == edit_number:
                idx_num = self.phones.index(p)

                self.phones[idx_num] = Phone(new_number)

        return self.phones

    def find_phone(self, searh_number):
        find_phone = ""
        for phone in self.phones:
            if str(phone) == str(searh_number):
                find_phone = str(phone)

        if find_phone:
            return find_phone
        else:
            return f"Search phone {searh_number} does not exist in AddressBook"

    def add_birthday(self, date):
        if self.birthday is not None:
            raise ValueError("Field birthday has value")

        self.birthday = Birthday(date)

    def add_address(self, address):
        if self.address is not None:
            self.address.value = address
        else:
            self.address = Address(address)

    def add_email(self, email):
        self.emails.append(Email(email))

    def edit_email(self, old, new):
        self.emails = [new if str(i) == old else i for i in self.emails]

    def __str__(self):
        name = self.name.value.title()
        phones = "; ".join(p.value for p in self.phones) if self.phones else "empty"
        birthday = self.birthday if self.birthday else "empty"
        address = self.address if self.address else "empty"
        email = "; ".join(str(p) for p in self.emails) if self.emails else "empty"

        return f"""
        📱 Contact info:
            ● name: {name}
            ● phones: {phones}
            ● birthday: {birthday}
            ● address: {address}
            ● email: {email}

        """
