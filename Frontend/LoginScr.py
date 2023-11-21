import tkinter
from Frontend import scrdir
from tkinter import *
from Backend import backenddir

def loginscr():
    scr = Tk()
    # gui
    scr.title('H&C HealthLink')
    scr.minsize(1280, 720)
    scr.maxsize(1280, 720)

    # Graphics
    windowBackground = PhotoImage(file=r"rsc\frameBG\login-bg.png")
    windowLogo = PhotoImage(file=r"rsc\AppLogo\app-logo.png")
    roundedEntryAsset = PhotoImage(file=r'rsc\Assets\username-entry.png')
    roundedButtonAsset = PhotoImage(file=r'rsc\Assets\login-btn.png')

    Label(scr, image=windowBackground).place(relheight=1, relwidth=1)
    scr.iconphoto(False, windowLogo)

    mainFrame = LabelFrame(scr, width=1280, height=720, bg='white', border=0)
    mainFrame.pack(padx=40, anchor=W)

    titleF = Frame(mainFrame, bg='#9FE2BF')
    Label(titleF, text='H&C HealthLink', bg='#9FE2BF', font='Roboto 54 bold', fg='#F0347B').pack(anchor=W, pady=(25, 0))
    Label(titleF, text='Integrating Services For A Better Community', bg='#9FE2BF', font='Roboto 12', fg='#F0347B').pack(anchor=W, pady=(0, 5))

    titleF.grid(row=0, column=0)

    # FUNCTIONS
    backendCmd = backenddir.backendCommands()
    frontendCmd = scrdir.ScrPages()
    name_var = tkinter.StringVar()
    passw_var = tkinter.StringVar()
    def submit():
        name = name_var.get()
        password = passw_var.get()

        print("The name is : " + name)
        print("The password is : " + password)

        if bool(backendCmd.passwordCheck(name, password)):
            print("Login Success")
            scr.destroy()
            frontendCmd.patientscr()

        name_var.set("")
        passw_var.set("")

    '''
        LOGIN CREDENTIALS FRAME
    '''
    loginCredF = Frame(mainFrame, bg='white')

    # USERNAME
    Label(loginCredF, text="Username", font="Roboto 11", bg='white').grid(row=0, column=0, sticky=W, pady=2)
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=1, column=0, pady=2)
    usernameEntry = Entry(loginCredF, textvariable=name_var, font=("Arial", 14), border=0, justify=LEFT, bg='#F5F4EC', width=40)
    usernameEntry.grid(row=1, column=0, pady=2, sticky=W, padx=(10, 0))

    # PASSWORD
    Label(loginCredF, text="Password", font="Roboto 11", bg='white').grid(row=2, column=0, sticky=W, pady=2)
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=3, column=0, pady=(0, 5))
    passwordEntry = Entry(loginCredF, textvariable=passw_var, font=("Arial", 14), border=0, justify=LEFT, bg='#F5F4EC', show='*', width=40)
    passwordEntry.grid(row=3, column=0, pady=10, sticky=W, padx=(10, 0))

    Button(loginCredF, image=roundedButtonAsset, border=0, bg='white', command=submit).grid(row=4, column=0, padx=(330, 0), pady=5)

    loginCredF.grid(row=1, column=0, pady=(100, 30))

    '''
            LOGIN LABEL FRAME
    '''
    loginLabelF = Frame(mainFrame, bg='white')
    Label(loginLabelF, text="Login  | ", font=("Arial", 11), bg='white').grid(row=0, column=0)
    Button(loginLabelF, text="Forgot Password", font=("Arial", 11), bg='white', border=0, fg='blue').grid(row=0, column=1)

    loginLabelF.grid(row=2, column=0, padx=50, pady=(0, 100))




    scr.mainloop()