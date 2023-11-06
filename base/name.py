from base.field import Field


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        is_string = isinstance(value, str)
        is_empty = len(value.strip()) < 0
        has_numbers = any(char.isdigit() for char in value)

        if not is_string or is_empty or has_numbers:
            raise ValueError("Field name is incorrect\n")
        else:
            self.__value = value.lower()
