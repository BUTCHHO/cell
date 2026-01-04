from api.v1.errors.base import BaseError

class InvalidCommandError(BaseError):
    def __init__(self)
        msg = "Command does not exist"
        super().__init__(400, msg)