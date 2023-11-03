import re
from base.field import Field


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validated_email()

    def validated_email(self):
        pattern = re.compile(r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,}")
        if not re.match(pattern, self.value):
            raise ValueError(print("Wrong email format"))
