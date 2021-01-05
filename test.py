import tkinter
import tkinter.messagebox
import pickle

def App():
    root = tkinter.Tk()
    root.title("To-Do List")

    def add_task():
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Warning!", "You must enter a task")

    def delete_task():
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning("Warning!", "You must select a task")

    def load_tasks():
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                listbox_tasks.insert(tkinter.END, task)
        except:
            tkinter.messagebox.showwarning("Warning!", "Cannot find tasks.dat")

    def save_tasks():
        try:
            tasks = listbox_tasks.get(0, listbox_tasks.size())
            pickle.dump(tasks, open("tasks.dat", "wb"))
        except:
            pass

    frame_tasks = tkinter.Frame(root).pack()
    listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50).pack(side=tkinter.LEFT)
    scrollbar_tasks = tkinter.Scrollbar(frame_tasks).pack(side=tkinter.RIGHT, fill=tkinter.Y)

    listbox_tasks.configure(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.configure(command=listbox_tasks.yview)

    entry_task = tkinter.Entry(root, width=50).pack()
    button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task).pack()
    button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task).pack()
    button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks).pack()
    button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks).pack()

    root.mainloop()

if __name__ == "__main__":
    App()