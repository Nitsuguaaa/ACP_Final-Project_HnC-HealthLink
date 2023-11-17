from Backend import passwordChecker

class backendCommands:
    def passwordCheck(self, username, password):
        return passwordChecker.passwordCheck(username, password)