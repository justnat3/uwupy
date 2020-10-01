class UwUFilePathFucked(self):
    """Exception thrown when host cant be reached
        Attr: objName
    """

    def __init__(self, objName, message=''):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'