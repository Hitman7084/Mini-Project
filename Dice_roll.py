from tkinter import *
import random

window = Tk() 
 
window.configure(bg="black") 

window.geometry("500x500") 

window.title("Rolling The Dice") 

window.resizable(0, 0) 

def roll_dices(): 
    dice_dots = ['\u2680', '\u2681', 
                 '\u2682', '\u2683', 
                 '\u2684', '\u2685']
    label.configure( 
        text=f'{random.choice(dice_dots)}') 
    label.pack() 

  
roll_button = Button(window, text="Roll!", 
                     width=10, height=2, 
                     font=15, bg="aqua", 
                     bd=2, command=roll_dices) 

roll_button.pack(padx=10, pady=15)   

label = Label(window, font=("times", 250), 
              bg="black", fg="white") 
  
window.mainloop() 