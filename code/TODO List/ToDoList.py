"""
Instructions:
- This is is a To-Do list made with tkinter.
- The code for To-Do List which will create a tasks.dat file after running for the first time.
- The "load" button will load details from the tasks.dat file to the program and the "save" button will upload it.
"""

# Libraries required
import tkinter
import tkinter.messagebox
import pickle

def App():
    # Adding Task
    def add_task():
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Warning!", "You must enter a task")

    # Deleting Task
    def delete_task():
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning("Warning!", "You must select a task")

    # Lodaing tasks from binary fle
    def load_tasks():
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                listbox_tasks.insert(tkinter.END, task)
        except:
            tkinter.messagebox.showwarning("Warning!", "Cannot find tasks.dat")

    # Saving tasks to binary file
    def save_tasks():
        try:
            tasks = listbox_tasks.get(0, listbox_tasks.size())
            pickle.dump(tasks, open("tasks.dat", "wb"))
        except:
            pass
    
    # GUI
    root = tkinter.Tk()
    root.title("To-Do List")
    frame_tasks = tkinter.Frame(root)
    frame_tasks.pack()
    
    listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
    listbox_tasks.pack(side=tkinter.LEFT)
    
    scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    listbox_tasks.configure(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.configure(command=listbox_tasks.yview)

    entry_task = tkinter.Entry(root, width=50)
    entry_task.pack()
    
    button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
    button_add_task.pack()
    
    button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
    button_delete_task.pack()
    
    button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
    button_load_tasks.pack()
    
    button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
    button_save_tasks.pack()

    root.mainloop()

# Driver program
if __name__ == "__main__":
    App()
