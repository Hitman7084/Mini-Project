import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game- Made by Atul Updadhyay")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")
        
        self.random_number = random.randint(1, 1000)
        self.tries = 0
        
        self.style_label = {"bg": "#282c34", "fg": "#61dafb", "font": ("Helvetica", 14)}
        self.style_entry = {"font": ("Helvetica", 12), "justify": "center"}
        self.style_button = {"bg": "#61dafb", "fg": "#282c34", "font": ("Helvetica", 12), "activebackground": "#21a1f1"}

        self.label = tk.Label(root, text="Guess a number between 1 and 1000:", **self.style_label)
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, **self.style_entry)
        self.entry.pack(pady=10, ipady=5, ipadx=20)

        self.button = tk.Button(root, text="Guess", command=self.check_guess, **self.style_button)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text="", **self.style_label)
        self.result_label.pack(pady=20)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.tries += 1

            if guess < 1 or guess > 1000:
                self.result_label.config(text="Please enter a number between 1 and 1000.")
            elif guess < self.random_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.random_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You've guessed the number in {self.tries} tries.")
                messagebox.showinfo("Number Guessing Game", f"Correct! The number was {self.random_number}. You guessed it in {self.tries} tries.")
                self.reset_game()
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.random_number = random.randint(1, 1000)
        self.tries = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
