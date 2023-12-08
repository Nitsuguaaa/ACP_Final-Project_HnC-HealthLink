import tkinter
from pathlib import Path
from tkinter import *
from Frontend import scrdir
from MySQL03 import sqldir
import datetime

ASSETS_PATH = Path(r"rsc\FormAssets(Update)")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PatientUpdateScr():
    window = Tk()
    window.title("H&C HealthLink  |  Update Patient Information")
    window.geometry("530x700")
    window.configure(bg = "#FFFFFF")

    windowLogo = PhotoImage(file=r"rsc\AppLogo\app-logo.png")
    window.iconphoto(False, windowLogo)

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 530,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    #Functions
    sql = sqldir.SqlCommands()
    scr = scrdir.ScrPages()
    searchName = tkinter.StringVar()
    EntryPatientDay = tkinter.StringVar()
    EntryPatientMonth = tkinter.StringVar()
    EntryPatientYear = tkinter.StringVar()
    def patientList(name):
        if name[0:3] == "PT-":
            return sql.select("patienttbl", constraints=f"WHERE patientID='{name}'", fetchOne=True)
        else:
            return sql.select("patienttbl", constraints=f"WHERE patientName LIKE '%{name}%'", fetchOne=True)

    def patientInfo(name):
        return sql.select("patientinfotbl", column="patientDisease, patientIn", constraints=f"WHERE patientID='{name}'", fetchOne=True)

    def showPatientInfo(patientTable, patientInfoTable):
        canvas.itemconfig(patientName, text=patientTable[1])
        canvas.itemconfig(patientIdentification, text=patientTable[0])
        birthdate = patientTable[2]
        canvas.itemconfig(patientBirthDay, text=birthdate.strftime("%d"))
        canvas.itemconfig(patientBirthMonth, text=birthdate.strftime("%b"))
        canvas.itemconfig(patientBirthYear, text=birthdate.strftime("%Y"))
        canvas.itemconfig(patientAddress, text=f"{patientTable[3]}, {patientTable[4]}, {patientTable[5]}, {patientTable[6]}")
        canvas.itemconfig(patientDisease, text=patientInfoTable[0])
        patientInDate = patientInfoTable[1]
        canvas.itemconfig(patientInDay, text=patientInDate.strftime("%d"))
        canvas.itemconfig(patientInMonth, text=patientInDate.strftime("%b"))
        canvas.itemconfig(patientInYear, text=patientInDate.strftime("%Y"))


    def searchPatient(event):
        name = searchName.get()
        entry_1.focus_set()

        patientTable = patientList(name)
        patientInfoTbl = patientInfo(patientTable[0])

        showPatientInfo(patientTable, patientInfoTbl)

        # Might slow the program since it calls the databse mutiple times
        # patientInfo = lambda name: sql.select("patienttbl", constraints=f"WHERE patientID='{name}'", fetchOne=True) if name[0:3] == "PT-" else sql.select("patienttbl", constraints=f"WHERE patientName LIKE '%{name}%'", fetchOne=True)

    def updatePatient():
        if canvas.itemcget(patientName, 'text') == '':
            canvas.itemconfig(error, text="No patient searched ⚠︎")
        else:
            if EntryPatientDay.get() == '' or EntryPatientMonth.get() == '' or EntryPatientYear.get() == '':
                canvas.itemconfig(error, text="fields left blank ⚠︎")
            else:
                print("dd/mm/yyyy:", EntryPatientDay.get(), EntryPatientMonth.get(), EntryPatientYear.get())
                canvas.itemconfig(error, text="")

                patientOut = EntryPatientYear.get() + "-" + EntryPatientMonth.get() + "-" + EntryPatientDay.get()
                sql.update("patientinfotbl", "patientOut", patientOut, "patientID", canvas.itemcget(patientIdentification, 'text'))
                button_1.configure(state="disabled")
                canvas.itemconfig(success, text="Patient updated, returning to home")
                window.after(3000, homeScr)

    def addScr():
        window.destroy()
        scr.patientaddscr()
    def homeScr():
        window.destroy()
        scr.homescr()

    window.bind('<Return>', lambda event: searchPatient(event))

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        530.0,
        70.0,
        fill="#355E3B",
        outline="")

    canvas.create_rectangle(
        13.0,
        104.0,
        517.0,
        188.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        13.0,
        215.0,
        517.0,
        592.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        25.0,
        339.0,
        anchor="nw",
        text="Address ",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        27.0,
        358.0,
        501.0,
        388.0,
        fill="#FFFFFF",
        outline="")
    patientAddress = canvas.create_text(
        27.0,
        358.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )


    canvas.create_text(
        27.0,
        225.0,
        anchor="nw",
        text="Full Name",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        25.0,
        115.0,
        anchor="nw",
        text="Search",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        243.0,
        273.0,
        273.0,
        fill="#FFFFFF",
        outline="")

    patientName = canvas.create_text(
        26.0,
        243.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1),
        width=280

    )

    canvas.create_text(
        292.0,
        225.0,
        anchor="nw",
        text="Patient’s I.D",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        263.5,
        149.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=searchName
    )
    entry_1.place(
        x=32.0,
        y=134.0,
        width=475.0,
        height=28.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=updatePatient,
        relief="flat"
    )
    button_1.place(
        x=273.0,
        y=620.0,
        width=220.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=addScr,
        relief="flat"
    )
    button_2.place(
        x=44.0,
        y=46.0,
        width=78.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=131.0,
        y=42.0,
        width=70.0,
        height=30.0
    )

    '''button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=413.0,
        y=21.0,
        width=95.0,
        height=35.0
    )'''

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=homeScr,
        relief="flat"
    )
    button_5.place(
        x=27.0,
        y=619.0,
        width=220.0,
        height=40.0
    )

    canvas.create_text(
        27.0,
        277.0,
        anchor="nw",
        text="Date of birth",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        297.0,
        141.0,
        327.0,
        fill="#FFFFFF",
        outline="")
    patientBirthDay = canvas.create_text(
        26.0,
        297.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        158.0,
        297.0,
        273.0,
        327.0,
        fill="#FFFFFF",
        outline="")
    patientBirthMonth = canvas.create_text(
        158.0,
        297.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        292.0,
        296.0,
        502.0,
        326.0,
        fill="#FFFFFF",
        outline="")
    patientBirthYear = canvas.create_text(
        292.0,
        296.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        291.0,
        243.0,
        501.0,
        273.0,
        fill="#FFFFFF",
        outline="")
    patientIdentification = canvas.create_text(
        291.0,
        243.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        26.0,
        396.0,
        anchor="nw",
        text="Disease",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        416.0,
        501.0,
        446.0,
        fill="#FFFFFF",
        outline="")
    patientDisease = canvas.create_text(
        26.0,
        416.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        25.0,
        452.0,
        anchor="nw",
        text="Patient In",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        25.0,
        473.0,
        140.0,
        503.0,
        fill="#FFFFFF",
        outline="")
    patientInDay = canvas.create_text(
        25.0,
        473.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        157.0,
        473.0,
        272.0,
        503.0,
        fill="#FFFFFF",
        outline="")
    patientInMonth = canvas.create_text(
        157.0,
        473.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_rectangle(
        291.0,
        473.0,
        501.0,
        503.0,
        fill="#FFFFFF",
        outline="")
    patientInYear = canvas.create_text(
        291.0,
        473.0,
        anchor="nw",
        text="",
        fill="#000000",
        font=("Inter Bold", 16 * -1)
    )

    canvas.create_text(
        25.0,
        520.0,
        anchor="nw",
        text="Patient out",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    error = canvas.create_text(
        275.0,
        600.0,
        anchor="nw",
        text="",
        fill="RED",
        font=("Inter Bold", 12 * -1)
    )
    success = canvas.create_text(
        275.0,
        600.0,
        anchor="nw",
        text="",
        fill="GREEN",
        font=("Inter Bold", 12 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        82.5,
        554.0,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=EntryPatientDay
    )
    entry_2.place(
        x=32.0,
        y=539.0,
        width=115.0,
        height=28.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        214.5,
        554.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=EntryPatientMonth
    )
    entry_3.place(
        x=162.0,
        y=539.0,
        width=115.0,
        height=28.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        396.0,
        554.0,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=EntryPatientYear
    )
    entry_4.place(
        x=296.0,
        y=539.0,
        width=210.0,
        height=28.0
    )
    window.resizable(False, False)
    window.mainloop()
