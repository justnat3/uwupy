# Pronerd Jay -> uh-owopy
class Oops(Exception):
    """Generic Exception Raised by the user.

        Attributes:
            Name: Program, function, service, return values. etc
    """

    def __init__(self, Name, message="made a fucky wucky."):
        self.Name = Name
        self.message = message
        super().__init__(self.message)

    def __repr__(self):
        repr('UwU Exception')

    def __str__(self):
        return f"oopsie woopsie! {self.Name} -> {self.message})"


class CustomUwU(Exception):

    """Generic Custom Exception Raised by the user

        Attributes:
            ObjectName: Program, function, service, return value. etc
            Start: Start of message
            Message: is the error end
    """

    def __init__(self, ObjectName, start=str, message=str):
        self.ObjectName = ObjectName
        self.message = message
        self.start = start
        super().__init__(self.message)

    def __repr__(self):
        return 'UwU Exception'

    def __str__(self):
        return f'{self.start}! {self.ObjectName} -> {self.message}'


if __name__ == "__main__":
    raise Oops("postgreSQL")
