from pathlib import Path
from tkinter import *

ASSETS_PATH = Path(r"rsc\FormAssets(Add)")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PatientFormAdd():
    window = Tk()
    window.title('H&C HealthLink')
    window.geometry("530x700")
    window.configure(bg = "#FFFFFF")


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
        text="Address Line 1",
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
        text="Patient In",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        27.0,
        498.0,
        anchor="nw",
        text="(If others, please specify)",
        fill="#000000",
        font=("Inter Regular", 12 * -1)
    )

    canvas.create_text(
        268.0,
        338.0,
        anchor="nw",
        text="State",
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
        273.0,
        273.0,
        anchor="nw",
        text="Address Line 2",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_text(
        26.0,
        169.0,
        anchor="nw",
        text="Date of birth",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        134.0,
        501.0,
        164.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        26.0,
        460.0,
        501.0,
        490.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        28.0,
        518.0,
        503.0,
        548.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        27.0,
        293.0,
        257.0,
        323.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        27.0,
        357.0,
        257.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        268.0,
        357.0,
        398.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        408.0,
        357.0,
        501.0,
        387.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        273.0,
        293.0,
        503.0,
        323.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        26.0,
        187.0,
        141.0,
        217.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        26.0,
        576.0,
        141.0,
        606.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        158.0,
        576.0,
        273.0,
        606.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        158.0,
        187.0,
        273.0,
        217.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        292.0,
        186.0,
        502.0,
        216.0,
        fill="#FFFFFF",
        outline="")

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
        command=lambda: print("button_1 clicked"),
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
        command=lambda: print("button_2 clicked"),
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
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=132.0,
        y=46.0,
        width=70.0,
        height=30.0
    )

    button_image_4 = PhotoImage(
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
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
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
