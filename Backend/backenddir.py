from Backend import passwordChecker, EmailingSystem, dataAnalytics

class backendCommands:
    dataAnalysis = dataAnalytics.dataAnalysis()
    def passwordCheck(self, username, password):
        return passwordChecker.passwordCheck(username, password)
    def sendEmail(self):
        EmailingSystem.sendEmail()