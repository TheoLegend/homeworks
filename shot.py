import tkinter as tk
import random

# Game logic
def play(choice):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    if choice == computer_choice:
        result = f"Draw! Both chose {choice}."
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = f"You Win! {choice} beats {computer_choice}."
        scores["player"] += 1
    else:
        result = f"You Lose! {computer_choice} beats {choice}."
        scores["computer"] += 1

    result_var.set(result)
    score_var.set(f"Player: {scores['player']}  |  Computer: {scores['computer']}")

# Setup window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

# Score tracker
scores = {"player": 0, "computer": 0}

# Labels
tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold")).pack(pady=10)

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var, font=("Arial", 12)).pack(pady=10)

score_var = tk.StringVar(value="Player: 0  |  Computer: 0")
tk.Label(root, textvariable=score_var, font=("Arial", 12)).pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock ✊", font=("Arial", 12), width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper ✋", font=("Arial", 12), width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors ✌", font=("Arial", 12), width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Run app
root.mainloop()
