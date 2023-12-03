from pathlib import Path
from tkinter import *

ASSETS_PATH = Path(r"rsc\HomescrAssets")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def HomeScr():

    window = Tk()
    window.title('H&C HealthLink')
    window.geometry("700x560")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 560,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        36.0,
        330.0,
        image=image_image_1
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

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        50.0,
        50.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        385.0,
        196.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        34.0,
        158.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        241.0,
        405.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        529.0,
        405.0,
        image=image_image_6
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
        x=9.0,
        y=211.0,
        width=54.0,
        height=50.0
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
        x=9.0,
        y=307.0,
        width=54.0,
        height=50.0
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
        x=9.0,
        y=493.0,
        width=54.0,
        height=50.0
    )
    window.resizable(False, False)
    window.mainloop()
