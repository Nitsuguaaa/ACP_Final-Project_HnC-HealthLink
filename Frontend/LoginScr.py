import tkinter
from tkinter import *

def loginscr():
    scr = Tk()
    #gui
    scr.title('Hospital Aid System')
    scr.minsize(1280, 720)
    scr.maxsize(1280, 720)

    imgpath = PhotoImage(file=r"rsc\login-bg.png")
    tkinter.Label(scr, image=imgpath).place(relheight=1, relwidth=1)



    scr.mainloop()