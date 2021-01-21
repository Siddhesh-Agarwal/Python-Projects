from tkinter import *
from time import strftime 

root = Tk()
root.title('Digital Clock')
root.resizable(0, 0)

def time(): 
    string = strftime('%H:%M:%S') 
    lbl.config(text = string) 
	lbl.after(1000, time)

lbl = Label(root, font = ('arial', 50), bg = 'black', fg = 'red')
lbl.pack() 
time()

root.mainloop()
