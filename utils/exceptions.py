class UserError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class MissingInputError(Exception):
    def __init__(self, value="Missing input data"):
        self.value = value

    def __str__(self):
        return self.value


class GeneralError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class AlreadyExistError(Exception):
    def __init__(self, value="Object already exist"):
        self.value = value

    def __str__(self):
        return self.value
