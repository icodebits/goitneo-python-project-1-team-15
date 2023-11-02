from field import Field


class Address(Field):
    def __init__(self, value):
        super().__init__(value)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        is_string = isinstance(value, str)

        if not is_string :
            raise ValueError("Address is incorrect")

        self.__value = value