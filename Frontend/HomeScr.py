from tkinter import *

def homescr():
    scr = Tk()
    # gui
    scr.title('H&C HealthLink')
    scr.minsize(1280, 720)
    scr.maxsize(1280, 720)
    # Graphics
    windowBackground = PhotoImage(file=r"rsc\frameBG\login-bg.png")
    windowLogo = PhotoImage(file=r"rsc\AppLogo\app-logo.png")
    scr.iconphoto(False, windowLogo)


    scr.mainloop()