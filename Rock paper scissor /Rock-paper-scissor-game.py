import random
import tkinter as tk
from tkinter import messagebox

# Global score values
score_user = 0
score_computer = 0


def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def choose_move(user_choice):
    global score_user, score_computer

    computer_choice = get_computer_choice()
    result = get_winner(user_choice, computer_choice)

    if result == "You win!":
        score_user += 1
    elif result == "Computer wins!":
        score_computer += 1

    user_label.config(text=f"You chose: {user_choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {score_user}  Computer: {score_computer}")


def reset_score():
    global score_user, score_computer
    score_user = 0
    score_computer = 0
    user_label.config(text="You chose: -")
    computer_label.config(text="Computer chose: -")
    result_label.config(text="Result: -")
    score_label.config(text="Score - You: 0  Computer: 0")


def quit_game():
    if messagebox.askyesno("Quit", "Do you want to quit the game?"):
        root.destroy()


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("320x280")
root.resizable(False, False)

header = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
header.pack(pady=10)

info = tk.Label(root, text="Choose your move below:", font=("Arial", 11))
info.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=8)

rock_button = tk.Button(button_frame, text="Rock", width=8, command=lambda: choose_move('rock'))
paper_button = tk.Button(button_frame, text="Paper", width=8, command=lambda: choose_move('paper'))
scissors_button = tk.Button(button_frame, text="Scissors", width=8, command=lambda: choose_move('scissors'))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="You chose: -", font=("Arial", 11))
user_label.pack(pady=4)

computer_label = tk.Label(root, text="Computer chose: -", font=("Arial", 11))
computer_label.pack(pady=4)

result_label = tk.Label(root, text="Result: -", font=("Arial", 12, "bold"))
result_label.pack(pady=6)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 11))
score_label.pack(pady=4)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

reset_button = tk.Button(control_frame, text="Reset Score", width=12, command=reset_score)
quit_button = tk.Button(control_frame, text="Quit", width=12, command=quit_game)

reset_button.grid(row=0, column=0, padx=5)
quit_button.grid(row=0, column=1, padx=5)

root.mainloop()

