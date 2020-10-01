class UwUPacketLoss(Exception):
    """Exception thrown when Packet Loss is detected
        Attr: objName
    """

    def __init__(self, objName, message=''):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'

class UwUICMPFucked(self):
    """Exception thrown when host cant be reached
        Attr: objName
    """

    def __init__(self, objName, message=''):
        self.objName = objName
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.objName} -> {self.message}'
