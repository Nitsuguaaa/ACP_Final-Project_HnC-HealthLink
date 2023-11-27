from pathlib import Path
from tkinter import *

ASSETS_PATH = Path(r"rsc\FormAssets(Delete)")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def PatientDeleteScr():
    window = Tk()
    window.title("H&C HealthLink")
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
        26.0,
        333.0,
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

    canvas.create_text(
        26.0,
        225.0,
        anchor="nw",
        text="Full Name",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        26.0,
        243.0,
        501.0,
        273.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        26.0,
        116.0,
        anchor="nw",
        text="Patient’s I.D",
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
        command=lambda: print("button_2 clicked"),
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
        x=27.0,
        y=619.0,
        width=220.0,
        height=40.0
    )

    canvas.create_text(
        26.0,
        279.0,
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

    canvas.create_rectangle(
        158.0,
        297.0,
        273.0,
        327.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        292.0,
        296.0,
        502.0,
        326.0,
        fill="#FFFFFF",
        outline="")

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

    canvas.create_text(
        27.0,
        453.0,
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

    canvas.create_rectangle(
        157.0,
        473.0,
        272.0,
        503.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        291.0,
        473.0,
        501.0,
        503.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        27.0,
        519.0,
        anchor="nw",
        text="Patient out",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        25.0,
        539.0,
        140.0,
        569.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        157.0,
        539.0,
        272.0,
        569.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_rectangle(
        291.0,
        539.0,
        501.0,
        569.0,
        fill="#FFFFFF",
        outline="")
    window.resizable(False, False)
    window.mainloop()
