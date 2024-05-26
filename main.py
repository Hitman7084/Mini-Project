from tkinter import *
import random
import os
from tkinter import messagebox

def run_game(game_number):
    game_file = f'game{game_number}.py'
    if os.path.isfile(game_file):
        os.system(f'python {game_file}')
    else:
        messagebox.showerror("Error", f"{game_file} does not exist.")

def roll_dices():
    dice_dots = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    roll_result = random.randint(1, 6)
    label.configure(text=dice_dots[roll_result - 1])
    label.pack()

    if roll_result in [1, 2, 3, 4]:
        run_game(roll_result)
    else:
        while roll_result > 4:
            roll_result = random.randint(1, 6)
            label.configure(text=dice_dots[roll_result - 1])
            label.pack()
        run_game(roll_result)

window = Tk()
window.configure(bg="black")
window.geometry("400x400")
window.title("Rolling Dice made by Himanshu and Arpit")
window.resizable(0, 0)

roll_button = Button(window, text="Roll!", width=10, height=2, font=15, bg="aqua", bd=2, command=roll_dices)
roll_button.pack(padx=10, pady=15)

label = Label(window, font=("times", 250), bg="black", fg="white")

window.mainloop()
