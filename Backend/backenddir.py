from Backend import passwordChecker, EmailingSystem

class backendCommands:
    def passwordCheck(self, username, password):
        return passwordChecker.passwordCheck(username, password)
    def sendEmail(self):
        EmailingSystem.sendEmail()