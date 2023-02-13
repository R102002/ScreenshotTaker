import pyscreenshot
from tkinter import *

def takeScreenShot():
    pyscreenshot.grab().save('My_Screen.png')

root = Tk()
root.title("My Screenshot App")
canvas = Canvas(root, width=300, height=300)
canvas.pack()

btn = Button(root, text="Take Screenshot", command=takeScreenShot, font=10)
canvas.create_window(150, 150, window=btn)

root.mainloop()
