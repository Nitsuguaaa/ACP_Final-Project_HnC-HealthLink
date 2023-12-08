from Backend import passwordChecker, EmailingSystem, dataAnalytics, idGenerator

class backendCommands:
    dataAnalysis = dataAnalytics.dataAnalysis()
    def passwordCheck(self, username, password):
        return passwordChecker.passwordCheck(username, password)
    def sendEmail(self, email=None, sendType="all"):
        EmailingSystem.sendEmail(email, sendType)
    def generatePatientID(self):
        return idGenerator.patientIDGenerator()
    def generateNewUser(self, username, password):
        passwordChecker.generateUser(username, password)