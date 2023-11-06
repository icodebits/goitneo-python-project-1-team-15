def handler_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Unsupported operation type"

    return wrapper


def contacts_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AttributeError as e:
            print(
                "\n❌ User with the name not found or phone should contain 10 consecutive digits with no spaces or other characters."
            )
        except Exception as e:
            print(f"\n❌ User with the name not found. Cannot use. Start again.\r\n")

    return wrapper


def date_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\n❌ Date must be in the format DD.MM.YYYY\r\n")

    return wrapper


def notes_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"\n❌ Notes with the title not found. Cannot use. Start again.\r\n")

    return wrapper
