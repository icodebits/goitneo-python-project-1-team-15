from collections import UserDict, defaultdict
from datetime import datetime

from record import Record
#from helpers.weekdays import WEEKDAYS, CURRENT_DATE


class AddressBook(UserDict):
    def add_record(self, contact: dict) -> None:
        self.data[contact.name.value] = contact

    def find(self, key: str) -> object:
        res = self.data.get(key)
        return res

    def delete(self, key: str) -> None:
        del self.data[key]

    def add_address(self, name: str, address: str) -> None:
        contact = self.find(name)
        if contact:
            if address.strip():
                contact.add_address(address)
                return "The address is added"
            else:
                return "The address is incorrect"
        else: 
            return "The user is missing"

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
            return "The user is missing"

    def show_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                return f"The address is: {contact.address}"
            else:
                return "The address is missing"
        else: 
            return "The user is missing"

    def remove_address(self, name: str) -> None:
        contact = self.find(name)
        if contact:
            if contact.address:
                contact.address = None
                return "Address removed"
            else:
                return "No address to remove"
        else: 
            return "The user is missing"

    # def set_birthday(self, name: str, date: str) -> None:
    #     contact = self.find(name)
    #     contact.add_birthday(date)

    # def show_birthday(self, name: str) -> str:
    #     contact = self.find(name)

    #     if contact.birthday:
    #         return contact.birthday.value
    #     else:
    #         raise AttributeError(
    #             f"The birthday field is missing from {contact.name.value}'s contact"
    #         )

    # def get_birthdays_per_week(self) -> str:
    #     birthday_dict = defaultdict(list)
    #     birthdays_info = ""

    #     for info in self.data.values():
    #         name = info.name.value.title()
    #         birthday = datetime.strptime(str(info.birthday), "%d %B %Y")
    #         birthday = birthday.date()
    #         birthday_this_year = birthday.replace(year=CURRENT_DATE.year)

    #         if birthday_this_year < CURRENT_DATE:
    #             birthday_this_year = birthday.replace(year=CURRENT_DATE.year + 1)

    #         delta_days = (birthday_this_year - CURRENT_DATE).days

    #         if delta_days < 7:
    #             if birthday_this_year.weekday() >= 5:
    #                 birthday_dict[WEEKDAYS[0]].append(name)
    #             else:
    #                 birthday_dict[WEEKDAYS[birthday_this_year.weekday()]].append(name)

    #     for day, users_list in birthday_dict.items():
    #         birthdays_info += f"{day}: {', '.join(list(users_list))}\n"

    #     return birthdays_info

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)
print("John is added")
for name, record in book.data.items():
    print(record)

print("The address is added")
book.add_address("John", "Kyiv")
for name, record in book.data.items():
    print(record)

print("The address is edited")
book.edit_address("John", "Lviv")
for name, record in book.data.items():
    print(record)

john = book.show_address("John")
print(john)
john1 = book.remove_address("John")
print(john1)
for name, record in book.data.items():
    print(record)

print("New address is added")
book.add_address("John", "Poltava")
for name, record in book.data.items():
    print(record)