#########################
#   Required Libraries  #
#########################
from os import error
import time
from random import choice
import tkinter as tk

##############
#  Varibles  #
##############
string = choice(open('Strings.txt').readlines()) # Text Line
started = False

######################
#  GUI Window Setup  #
######################
root = tk.Tk()
root.title('Typing Speed Test')
root.geometry('500x400')
root.resizable(0, 0)
root.config(bg='black')

############
#  Labels  #
############
lbl1 = tk.Label(root, text='Typing Speed Test', bg='black', fg='yellow', font=('book antiqua', 30, 'bold'))
lbl1.pack(fill=tk.X)

lbl2 = tk.Label(root, text='Text: ', bg='black', fg='snow', font=('helvetica', 18))
lbl2.pack(anchor=tk.NW)

lbl3 = tk.Label(root, text=string, bg='yellow', fg='black', justify=tk.LEFT , font=('Times New Roman', 22), wraplength=500)
lbl3.pack(fill=tk.X)

entry = tk.Entry(root, font=('Times New Roman', 22))
entry.pack(fill=tk.X)

####################################
#   Required Function Definitions  #
####################################
# FUnction to find the number of errors
def Errors(string, text):
    errors = 0
    for index, i in enumerate(text.split()):
        if string[index].lower() != i.lower():
            errors += 1
    return errors

# Function to display details as labels
def DisplayInfo(TimeTaken):
    text = entry.get()
    TimeTaken /= 60
    errors = Errors(string, text) # Number of wrong words
    gross_WPM = (len(text) / 5) / TimeTaken
    net_WPM = (len(text)/5 - errors) / TimeTaken
    if net_WPM < 0: net_WPM = 0
    Accuracy = net_WPM * 100 / gross_WPM

    Time_Label = tk.Label(root, text=f'Time Taken: {round(TimeTaken, 3)}', bg='black', fg='yellow', font=('arial', 18))
    GrossWPN_Label = tk.Label(root, text=f'Gross words per minute: {round(gross_WPM, 3)}', bg='black', fg='yellow', font=('arial', 18))
    NetWPM_Label = tk.Label(root, text=f'Net words per minute: {round(net_WPM, 3)}', bg='black', fg='yellow', font=('arial', 18))
    Accuracy_Label = tk.Label(root, text=f'Accuracy: {round(Accuracy, 3)}', bg='black', fg='yellow', font=('arial', 18))

    # Positions
    Accuracy_Label.pack(side=tk.BOTTOM, anchor=tk.W)
    NetWPM_Label.pack(side=tk.BOTTOM, anchor=tk.W)
    GrossWPN_Label.pack(side=tk.BOTTOM, anchor=tk.W)
    Time_Label.pack(side=tk.BOTTOM, anchor=tk.W)

# Function to start timer
def StartTimer(event):
    global started
    if not started:
        global t1
        t1 = time.time()
        started = True

# Function to stop timer and call DisplayInfo
def StopTimer(event):
    global t2
    t2 = time.time()

    global TimeTaken
    TimeTaken = t2 - t1
    
    DisplayInfo(TimeTaken)

#############
#  Binding  #
#############
root.bind_all(f'{string[0].upper()}', StartTimer)
root.bind_all(f'{string[0].lower()}', StartTimer)
root.bind_all('.', StopTimer)

root.mainloop()