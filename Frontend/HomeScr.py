import tkinter as tk

def homescr():
    r = tk.Tk()

    #gui
    r.geometry("400x400")
    r.minsize(400, 400)
    r.title('Home Screen')

    #modules
    btn1 = tk.Button(r, text='Stop', width=25, command=r.destroy)
    btn1.place(x=100, y=100, anchor="nw")


    r.mainloop()