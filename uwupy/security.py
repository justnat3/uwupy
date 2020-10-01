class Fail_AuthUwU(Exception):
    """Thrown when when authentication fails
        Attrs: objName
    """

    def __init__(self, objName, message='sowwy {self.objName} has failed auwthenication..'):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'


class UwUNoAccess(Exception):
    """Thrown when when authentication fails
        Attrs: objName
    """

    def __init__(self, objName, message='sowwy {self.objName} Can not hit me here..'):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'


class UwUMemberAccessException(Exception):
    """Thrown when when authentication fails
        Attrs: objName
    """

    def __init__(self, objName, message='sowwy {self.objName} does not have access to this..'):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'


class UwUPolicies(Exception):
    """Thrown when when authentication fails
        Attrs: objName
    """

    def __init__(self, objName, message='sowwy {self.objName} our powicies do not permit this..'):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'
