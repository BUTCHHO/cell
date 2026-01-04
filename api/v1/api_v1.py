from api.v1.errors.code_400 import InvalidCommandError

class CellAPI:
    def __init__(self, app):
        self.commands = {"delete_cell": app.cell_deleter,
                       "create_cell": app.cell_creator,}

    def accept_request(self, request: dict):
        command = request["command"]
        command_handler = self.commands.get(command)
        if not command_handler:
            return InvalidCommandError()
        return command_handler.handle(request)



