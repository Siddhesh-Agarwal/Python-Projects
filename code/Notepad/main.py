# Required Imports
import tkinter as tk
from tkinter import filedialog, font

#####################################
##     App  Class  Declaration     ##
#####################################
class App:
    def __init__(self, root):
        self.FileOpen = False

        # Text Area
        self.textarea = tk.Text(root)
        self.textarea.pack(fill=tk.BOTH)

        # Taskbar
        self.menubar = tk.Menu(root, tearoff=0)
        root.config(menu=self.menubar)

        # File Cascade
        self.FileMenu = tk.Menu(self.menubar, tearoff=0)
        self.FileMenu.add_command(label='New', command=self.New)
        self.FileMenu.add_command(label='Open', command=self.Open)
        self.FileMenu.add_command(label='Save', command=self.Save) 
        self.FileMenu.add_command(label='Save as', command=self.SaveAs)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label='Exit', command=root.destroy)

        # adding Cascades to Taskbar
        self.menubar.add_cascade(label='File', menu=self.FileMenu)

    def New(self):
        self.textarea.clear()
        self.FileOpen = False

    def Open(self):
        path = filedialog.askopenfilename(filetypes=[('All Files', '*.*')])
        self.FileOpen = path
        f = open(path, 'r+')
        text = f.read()
        self.textarea.insert(1.0, text)
        f.close()

    def Save(self):
        text = self.textarea.get("1.0", "end-1c")
        if not self.FileOpen:
            path = filedialog.asksaveasfile()
        else:
            path = self.FileOpen
        f = open(path, 'w+')
        f.write(text)
        f.close()

    def SaveAs(self):
        text = self.textarea.get("1.0", "end-1c")
        path = filedialog.asksaveasfilename()
        f = open(path, 'w+')
        f.write(text)
        f.close()

##########################
##        Driver        ##
##########################
if __name__ == '__main__':
    root = tk.Tk()
    master = App(root)
    root.title('Notepad using Python')
    root.geometry('400x400')
    root.resizable()
    root.mainloop()
