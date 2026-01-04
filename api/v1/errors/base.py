class BaseError:
    def __init__(self, status_code, msg, additional_data = None):
        self.status_code = status_code
        self.msg = msg
        self.additional = additional_data

    def __str__(self):
        return f" CELL ERROR status code: {self.status_code}, msg: {self.msg}, additional: {self.additional}"

