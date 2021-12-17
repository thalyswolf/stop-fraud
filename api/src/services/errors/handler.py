class GenericErrorException(Exception):

    """ Exception raised when an some occures error """

    def __init__(self, message='An error occures'):
        self.message = message
        super().__init__(self.message)

class InvalidAmountErrorException(Exception):

    """ Exception raised when an invalid value is informed """

    def __init__(self, message='invalid value is informed'):
        self.message = message
        super().__init__(self.message)


class InvalidRecommendationErrorException(Exception):

    """ Exception raised when an invalid recommendation is informed """

    def __init__(self, message='invalid value is informed'):
        self.message = message
        super().__init__(self.message)


class InvalidDataErrorException(Exception):

    """ Exception raised when an some occures error """

    def __init__(self, message='An error occures'):
        self.message = message
        super().__init__(self.message)


class NotFoundDBErrorException(Exception):
    """ Exception raised when an db query return is empty """

    def __init__(self, message='Not Found in DB...'):
        self.message = message
        super().__init__(self.message)