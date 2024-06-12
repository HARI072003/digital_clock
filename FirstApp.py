from tkinter import Tk
from tkinter import Label
import time
root=Tk()
root.title("Digital Clock")
def presenttime():
    displaytime=time.strftime("%I:%M:%S %p")
    digiclock.config(text=displaytime)
    digiclock.after(200,presenttime)
digiclock=Label(root,font=("arial",150),bg="yellow",fg="black")
digiclock.pack()
presenttime()
root.mainloop()
