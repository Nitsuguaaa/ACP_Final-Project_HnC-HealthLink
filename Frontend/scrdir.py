from Frontend import LoginScr, HomeScr, PatientFormadd, PatientFormUpdate, Emailform

class ScrPages:
    def loginscr(self):
        LoginScr.loginscr()
    def homescr(self):
        HomeScr.HomeScr()
    def patientaddscr(self):
        PatientFormadd.PatientFormAdd()
    def patientupdatescr(self):
        PatientFormUpdate.PatientUpdateScr()
    def emailscr(self):
        Emailform.EmailForm()
