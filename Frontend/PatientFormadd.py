import tkinter
from pathlib import Path
from tkinter import *
from Frontend import scrdir
from MySQL03 import sqldir
from Backend import backenddir

ASSETS_PATH = Path(r"rsc\FormAssets(Add)")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PatientFormAdd():
    window = Tk()
    window.title('H&C HealthLink  |  Add Patient')
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
        234.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        13.0,
        262.0,
        517.0,
        407.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        13.0,
        435.0,
        517.0,
        625.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        26.0,
        116.0,
        anchor="nw",
        text="Full Name",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        27.0,
        273.0,
        anchor="nw",
        text="Barangay",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        27.0,
        339.0,
        anchor="nw",
        text="City",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        26.0,
        440.0,
        anchor="nw",
        text="Disease",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        28.0,
        556.0,
        anchor="nw",
        text="Patient In  |  day/month/year",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    error = canvas.create_text(
        280.0,
        625.0,
        anchor="nw",
        text="",
        fill="RED",
        font=("Inter Bold", 12 * -1)
    )

    success = canvas.create_text(
        280.0,
        625.0,
        anchor="nw",
        text="",
        fill="GREEN",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        27.0,
        498.0,
        anchor="nw",
        text="(If other, please specify)",
        fill="#000000",
        font=("Inter Regular", 12 * -1)
    )

    canvas.create_text(
        268.0,
        338.0,
        anchor="nw",
        text="Province",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        408.0,
        338.0,
        anchor="nw",
        text="Zip Code",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        26.0,
        169.0,
        anchor="nw",
        text="Date of birth  |  day/month/year",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    # Functions
    sql = sqldir.SqlCommands()
    backend = backenddir.backendCommands()

    patientID = backend.generatePatientID()
    name = tkinter.StringVar()
    barangay = tkinter.StringVar()
    city = tkinter.StringVar()
    province = tkinter.StringVar()
    zipCode = tkinter.StringVar()
    disease = tkinter.StringVar()
    otherDisease = tkinter.StringVar()

    day = tkinter.StringVar()
    month = tkinter.StringVar()
    year = tkinter.StringVar()
    patientDayIn = tkinter.StringVar()
    patientMonthIn = tkinter.StringVar()
    patientYearIn = tkinter.StringVar()


    scr = scrdir.ScrPages()
    def updateScr():
        window.destroy()
        scr.patientupdatescr()
    def homeScr():
        window.destroy()
        scr.homescr()
    def addPatient():
        getDay = day.get()
        getMonth = month.get()
        getYear = year.get()
        getPatientDay = patientDayIn.get()
        getPatientMonth = patientMonthIn.get()
        getPatientYear = patientYearIn.get()

        birthdate = getYear + "-" + getMonth + "-" + getDay
        patientIn = getPatientYear + "-" + getPatientMonth + "-" + getPatientDay
        if name.get() == '' or day.get() == '' or month.get() == '' or year.get() == '' or barangay.get() == '' or city.get() == '' or province.get() == '' or zipCode.get() == '' or disease.get() == '' or patientDayIn.get() == '' or patientMonthIn.get() == '' or patientYearIn.get() == '':
            canvas.itemconfig(error, text="fields left blank ⚠︎")
        else:
            print(birthdate, patientIn)
            sql.insert("patientinfotbl", ("patientID", "patientDisease", "patientIn"), (patientID, disease.get(), patientIn))
            sql.insert("patienttbl", ("patientID", "patientName", "patientBirthdate","patientBarangay", "patientCity", "patientProvince", "patientZipCode"), (patientID, name.get(), birthdate, barangay.get(), city.get(), province.get(), zipCode.get()))
            button_1.configure(state="disabled")
            canvas.itemconfig(error, text="")
            canvas.itemconfig(success, text="Patient added, returning to home")
            window.after(2000, homeScr)


    # Name
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=name
    ).place(
        x=26,
        y=134,
        width=450,
        height=30
    )

    canvas.create_rectangle(
        26.0,
        134.0,
        501.0,
        164.0,
        fill="#FFFFFF",
        outline="")

    # Disease
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=disease
    ).place(
        x=26,
        y=460,
        width=450,
        height=30
    )

    canvas.create_rectangle(
        26.0,
        460.0,
        501.0,
        490.0,
        fill="#FFFFFF",
        outline="")

    # Other Disease
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=otherDisease
    ).place(
        x=26,
        y=518,
        width=450,
        height=30
    )

    canvas.create_rectangle(
        28.0,
        518.0,
        503.0,
        548.0,
        fill="#FFFFFF",
        outline="")

    # Barangay
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=barangay
    ).place(
        x=27,
        y=293,
        width=450,
        height=30
    )

    canvas.create_rectangle(
        27.0,
        293.0,
        501.0,
        323.0,
        fill="#FFFFFF",
        outline="")

    # City
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=city
    ).place(
        x=27,
        y=357,
        width=200,
        height=30
    )

    canvas.create_rectangle(
        27.0,
        357.0,
        257.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    # Province
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=province
    ).place(
        x=268,
        y=357,
        width=100,
        height=30
    )

    canvas.create_rectangle(
        268.0,
        357.0,
        398.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    # Zipcode
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=zipCode
    ).place(
        x=408,
        y=357,
        width=90,
        height=30
    )

    canvas.create_rectangle(
        408.0,
        357.0,
        501.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    # day
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=day
    ).place(
        x=26,
        y=187,
        width=90,
        height=30
    )

    canvas.create_rectangle(
        26.0,
        187.0,
        141.0,
        217.0,
        fill="#FFFFFF",
        outline="")

    # patient day in
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=patientDayIn
    ).place(
        x=26,
        y=576,
        width=90,
        height=30
    )

    canvas.create_rectangle(
        26.0,
        576.0,
        141.0,
        606.0,
        fill="#FFFFFF",
        outline="")

    # patient month in
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=patientMonthIn
    ).place(
        x=158,
        y=576,
        width=90,
        height=30
    )

    canvas.create_rectangle(
        158.0,
        576.0,
        273.0,
        606.0,
        fill="#FFFFFF",
        outline="")

    # month
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=month
    ).place(
        x=158,
        y=187,
        width=100,
        height=30
    )

    canvas.create_rectangle(
        158.0,
        187.0,
        273.0,
        217.0,
        fill="#FFFFFF",
        outline="")

    # year
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=year
    ).place(
        x=292,
        y=186,
        width=150,
        height=30
    )

    canvas.create_rectangle(
        292.0,
        186.0,
        502.0,
        216.0,
        fill="#FFFFFF",
        outline="")

    # patient year in
    Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable=patientYearIn
    ).place(
        x=292,
        y=576,
        width=150,
        height=30
    )

    canvas.create_rectangle(
        292.0,
        576.0,
        502.0,
        606.0,
        fill="#FFFFFF",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=addPatient,
        relief="flat"
    )
    button_1.place(
        x=281.0,
        y=641.0,
        width=220.0,
        height=40.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=addPatient,
        relief="flat"
    )
    button_2.place(
        x=41.0,
        y=40.0,
        width=78.0,
        height=31.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=updateScr,
        relief="flat"
    )
    button_3.place(
        x=132.0,
        y=46.0,
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
        x=26.0,
        y=641.0,
        width=220.0,
        height=40.0
    )
    window.resizable(False, False)
    window.mainloop()
