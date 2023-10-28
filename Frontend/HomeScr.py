import tkinter as tk
import Backend.test as be

def homescr():
    r = tk.Tk()

    #gui
    r.geometry("400x400")
    r.minsize(400, 400)
    r.title('Home Screen')

    #modules
    btn1 = tk.Button(r, text='Stop', width=25, command=r.destroy)
    btn1.place(relx=1, x=-2, y=2, anchor="ne")

    btn2 = tk.Button(r, text='test', width=25, command=be.test)
    btn2.place(relx=0.5, rely=0.5, anchor="center")

    r.mainloop()