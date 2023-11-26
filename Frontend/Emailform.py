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
        95.0,
        137.0,
        599.0,
        221.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        108.0,
        167.0,
        583.0,
        197.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        108.0,
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
        x=246.0,
        y=479.0,
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
        x=75.0,
        y=244.0,
        width=260.0,
        height=212.0
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
        x=371.0,
        y=244.0,
        width=260.0,
        height=212.0
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
        x=567.0,
        y=35.0,
        width=95.0,
        height=33.0
    )
    window.resizable(False, False)
    window.mainloop()
