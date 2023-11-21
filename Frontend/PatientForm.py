from tkinter import *

def patientscr():
    scr = Tk()
    # gui
    scr.title('H&C HealthLink')
    scr.minsize(1280, 720)
    scr.maxsize(1280, 720)
    # Graphics
    windowBackground = PhotoImage(file=r"rsc\frameBG\login-bg.png")
    windowLogo = PhotoImage(file=r"rsc\AppLogo\app-logo.png")
    scr.iconphoto(False, windowLogo)

    mainFrame = LabelFrame(scr, width=1280, height=720, bg='white', border=0)
    mainFrame.pack(padx=40, anchor=W)

    titleF = Frame(mainFrame, bg='#9FE2BF')
    Label(titleF, text='Patient Database Form', bg='#9FE2BF', font='Roboto 54 bold', fg='#F0347B').pack(anchor=W, pady=(25, 0))

    titleF.grid(row=0, column=0)

    scr.mainloop()