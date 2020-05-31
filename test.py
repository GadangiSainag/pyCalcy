from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk()

root.geometry("500x300")
canvas =Canvas(root,width=500 , height= 300)
canvas.pack()
black=canvas.create_line(0,0,40,50, fill= 'skyblue')

root.mainloop()