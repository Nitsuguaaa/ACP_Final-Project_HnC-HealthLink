import tkinter
from tkinter import *
from Frontend import scrdir
from Backend import backenddir

def loginscr():
    scr = Tk()
    # gui
    scr.title('H&C HealthLink')
    scr.minsize(700, 545)
    scr.maxsize(700, 545)

    # Graphics
    windowBackground = PhotoImage(file=r"rsc\frameBG\login-bg.png")
    windowLogo = PhotoImage(file=r"rsc\AppLogo\app-logo.png")
    roundedEntryAsset = PhotoImage(file=r'rsc\Assets\username-entry.png')
    roundedButtonAsset = PhotoImage(file=r'rsc\Assets\login-btn.png')

    Label(scr, image=windowBackground).place(relheight=1, relwidth=1)
    scr.iconphoto(False, windowLogo)

    mainFrame = LabelFrame(scr, width=700, height=545, bg='white', border=0)
    mainFrame.pack(anchor=W)

    titleF = Frame(mainFrame, bg='#9FE2BF', padx=70)
    Label(titleF, text='H&C HealthLink', bg='#9FE2BF', font='Roboto 30 bold', fg='#F0347B').pack(anchor=W, pady=(27.2, 0))
    Label(titleF, text='Integrating Services For A Better Community', bg='#9FE2BF', font='Roboto 8', fg='#F0347B').pack(anchor=W, pady=(0, 5))

    titleF.grid(row=0, column=0, pady=(0,40))

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
            frontendCmd.patientaddscr()
            
        name_var.set("")
        passw_var.set("")

    '''
        LOGIN CREDENTIALS FRAME
    '''
    loginCredF = Frame(mainFrame, bg='white')

    # USERNAME
    Label(loginCredF, text="Username", font="Roboto 8", bg='white').grid(row=0, column=0, sticky=W, pady=1, padx=(20,0))
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=1, column=0, pady=2, padx=(20, 80))
    usernameEntry = Entry(loginCredF, textvariable=name_var, font=("Arial", 8), border=0, justify=LEFT, bg='#F5F4EC', width=20)
    usernameEntry.grid(row=1, column=0, pady=2, sticky=W, padx=(27, 0))

    # PASSWORD
    Label(loginCredF, text="Password", font="Roboto 8", bg='white').grid(row=2, column=0, sticky=W, pady=1, padx=(20,0))
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=3, column=0, pady=(0, 5), padx=(20,80))
    passwordEntry = Entry(loginCredF, textvariable=passw_var, font=("Arial", 8), border=0, justify=LEFT, bg='#F5F4EC', show='*', width=20)
    passwordEntry.grid(row=3, column=0, pady=10, sticky=W, padx=(27, 0))

    Button(loginCredF, image=roundedButtonAsset, border=0, bg='white', command=submit).grid(row=4, column=0, padx=(90, 0), pady=5)

    loginCredF.grid(row=1, column=0, pady=(0, 0))

    '''
            LOGIN LABEL FRAME
    '''
    loginLabelF = Frame(mainFrame, bg='white')
    Label(loginLabelF, text="Login  | ", font=("Arial", 8), bg='white').grid(row=0, column=0)
    Button(loginLabelF, text="Forgot Password", font=("Arial", 8), bg='white', border=0, fg='blue').grid(row=0, column=1)

    loginLabelF.grid(row=2, column=0, padx=0)




    scr.mainloop()