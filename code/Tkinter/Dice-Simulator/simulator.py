import tkinter as tk
from PIL import Image, ImageTk
from random import choice

root = tk.Tk()
root.title('Dice Simulator')
root.resizable(0, 0)

dice = ['die1.jpg', 'die2.jpg', 'die3.jpg', 'die4.jpg', 'die5.jpg', 'die6.jpg']
resized_dice = [Image.open(x).resize((500, 400),Image.ANTIALIAS) for x in dice]

DiceImage = ImageTk.PhotoImage(choice(resized_dice))

ImageLabel = tk.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

def roll():
    DiceImage = ImageTk.PhotoImage(choice(resized_dice))
    ImageLabel.configure(image=DiceImage)
    ImageLabel.image = DiceImage
    
RollBtn = tk.Button(root, text='Roll', font=('helvetica', 26, 'bold'), bg='red', fg='yellow', padx=205, command=roll)
RollBtn.pack(expand=True)

root.mainloop()
