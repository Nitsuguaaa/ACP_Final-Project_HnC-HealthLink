from tkinter import *

def loginscr():
    scr = Tk()
    # gui
    scr.title('Hospital Aid System')
    scr.minsize(1280, 720)
    scr.maxsize(1280, 720)

    imgpath = PhotoImage(file=r"rsc\frameBG\login-bg.png")
    Label(scr, image=imgpath).place(relheight=1, relwidth=1)

    Label(scr, text='Hospital Aid System', bg='#9FE2BF', font='Roboto 28 bold').place(x=40, y=75)
    mainFrame = LabelFrame(scr, width=1280, height=720, bg='white', border=0)
    mainFrame.pack(padx=40, pady=200, anchor=W)



    '''
        LOGIN CREDENTIALS FRAME
    '''
    loginCredF = Frame(mainFrame, bg='white')
    roundedEntryAsset = PhotoImage(file=r'rsc\Assets\username-entry.png')
    roundedButtonAsset = PhotoImage(file=r'rsc\Assets\login-btn.png')

    # USERNAME
    Label(loginCredF, text="Username", font="Roboto 11", bg='white').grid(row=0, column=0, sticky=W, pady=2)
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=1, column=0, pady=2)
    usernameEntry = Entry(loginCredF, font=("Arial", 14), border=0, justify=LEFT, bg='#F5F4EC', width=40)
    usernameEntry.grid(row=1, column=0, pady=2, sticky=W, padx=(10, 0))

    # PASSWORD
    Label(loginCredF, text="Password", font="Roboto 11", bg='white').grid(row=2, column=0, sticky=W, pady=2)
    Label(loginCredF, image=roundedEntryAsset, border=0, bg='white').grid(row=3, column=0, pady=(0, 5))
    passwordEntry = Entry(loginCredF, font=("Arial", 14), border=0, justify=LEFT, bg='#F5F4EC', show='*', width=40)
    passwordEntry.grid(row=3, column=0, pady=10, sticky=W, padx=(10, 0))

    Button(loginCredF, image=roundedButtonAsset, border=0, bg='white').grid(row=4, column=0, padx=(330, 0), pady=5)


    loginCredF.grid(row=0, column=0, pady=30)

    '''
            LOGIN LABEL FRAME
    '''
    loginLabelF = Frame(mainFrame, bg='white')
    Label(loginLabelF, text="Login  | ", font=("Arial", 11), bg='white').grid(row=0, column=0)
    Button(loginLabelF, text="Forgot Password", font=("Arial", 11), bg='white', border=0, fg='blue').grid(row=0, column=1)

    loginLabelF.grid(row=1, column=0, padx=50, pady=('0', '100'))



    scr.mainloop()