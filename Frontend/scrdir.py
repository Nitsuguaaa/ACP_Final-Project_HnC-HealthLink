from Frontend import LoginScr, HomeScr, PatientFormadd, Emailform

class ScrPages:
    def loginscr(self):
        LoginScr.loginscr()
    def homescr(self):
        HomeScr.homescr()
    def patientaddscr(self):
        PatientFormadd.PatientFormAdd()
    def patientupdatescr(self):
        PatientFormUpdate.PatientFormUpdate()
    def emailscr(self):
        Emailform.EmailForm()
