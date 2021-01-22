"""
THis program allows the user to select a text file from his/her device.
Then the program will read out the contents of the file.
"""

# Libraries Required
import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import pyttsx3 as tts

# Button Parameters
btn_params = {
    'bg': 'gainsboro',
    'fg': 'black',
    'activebackground': 'yellow',
    'font': ('arial', 20, 'bold'),
    'padx': 5,
    'pady': 10,
    'bd': 4
}

# Function Definitions
def speak(text):
    engine = tts.init("sapi5")
    engine.say(text)
    engine.runAndWait()

def open_file():
    file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')]) 
    if file is not None:
        text = file.read()
        speak(text)

# GUI
app = tk.Tk()
app.title('File Reader - reads files literally')
app.resizable(0, 0)

# Creating Taskbar
menubar = tk.Menu(app)
app.config(menu=menubar)

ExitMenu = tk.Menu(menubar)
ExitMenu.add_command(label="Exit", command=app.destroy)

# Adding items to Taskbar
menubar.add_cascade(label="Exit", menu=ExitMenu)

# Accepting file
lbl = tk.Label(app, font=('arial', 20, 'bold') ,text='Choose file here: ').grid(row=0, column=0)
btn_open = tk.Button(app, **btn_params, text='  Open  ', command=open_file).grid(row=0, column=1)

# Keeping GUI window open
app.mainloop()
