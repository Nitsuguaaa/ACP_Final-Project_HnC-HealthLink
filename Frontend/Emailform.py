from pathlib import Path
from tkinter import *

ASSETS_PATH = Path(r"rsc\EmailAssets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def EmailForm():
    window = Tk()
    window.title("H&C HealthLink")
    window.geometry("700x545")
    window.configure(bg = "#FFFFFF")

    canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 545,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        25.0,
        137.0,
        529.0,
        221.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        38.0,
        167.0,
        513.0,
        197.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        38.0,
        147.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Inter Bold", 12 * -1)
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        100.0,
        fill="#355E3B",
        outline="")

    canvas.create_text(
        95.0,
        30.0,
        anchor="nw",
        text="H&C HealthLink",
        fill="#FFFFFF",
        font=("Inter Bold", 32 * -1)
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        50.0,
        50.0,
        image=image_image_1
    )

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
        x=250.0,
        y=456.0,
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
        x=544.0,
        y=136.0,
        width=127.48846435546875,
        height=85.94444274902344
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
        x=554.0,
        y=252.0,
        width=119.1950912475586,
        height=134.84613037109375
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
        x=25.0,
        y=244.0,
        width=504.0,
        height=150.0
    )
    window.resizable(False, False)
    window.mainloop()
