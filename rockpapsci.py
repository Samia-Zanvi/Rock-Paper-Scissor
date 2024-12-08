from tkinter import *
import random

def play(user_pick):
    global user_score, comp_score, draw_score
    
    # Choices and computer's pick
    ch = ["rock", "paper", "scissor"]
    comp_pick = random.choice(ch)
    
    # Determine the result
    if user_pick == comp_pick:
        result.set("It's a draw!")
        draw_score += 1
    elif (user_pick == "rock" and comp_pick == "scissor") or \
         (user_pick == "scissor" and comp_pick == "paper") or \
         (user_pick == "paper" and comp_pick == "rock"):
        result.set("You win this round!")
        user_score += 1
    else:
        result.set("Computer wins this round!")
        comp_score += 1
    
    # Update computer's choice and scores
    comp_choice.set(f"Computer chose: {comp_pick}")
    scores.set(f"User: {user_score} | Computer: {comp_score} | Draws: {draw_score}")

def reset_game():
    global user_score, comp_score, draw_score
    user_score = comp_score = draw_score = 0
    result.set("Let's Play!")
    comp_choice.set("")
    scores.set("User: 0 | Computer: 0 | Draws: 0")

# Initialize the main window
root = Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")
root.configure(bg="pink")

# Variables for game state
user_score, comp_score, draw_score = 0, 0, 0
result = StringVar(value="Let's Play!")
comp_choice = StringVar(value="")
scores = StringVar(value="User: 0 | Computer: 0 | Draws: 0")

# Title Label
Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="pink").pack(pady=10)

# Result Display
Label(root, textvariable=result, font=("Arial", 14), bg="lightblue").pack(pady=10)
Label(root, textvariable=comp_choice, font=("Arial", 12), bg="pink").pack(pady=5)

# Buttons for user choices
frame = Frame(root, bg="pink")
frame.pack(pady=10)
Button(frame, text="Rock", font=("Arial", 14), command=lambda: play("rock")).grid(row=0, column=0, padx=10)
Button(frame, text="Paper", font=("Arial", 14), command=lambda: play("paper")).grid(row=0, column=1, padx=10)
Button(frame, text="Scissor", font=("Arial", 14), command=lambda: play("scissor")).grid(row=0, column=2, padx=10)

# Score Display
Label(root, textvariable=scores, font=("Arial", 12), bg="pink").pack(pady=10)

# Reset Button
Button(root, text="Reset Game", font=("Arial", 14), command=reset_game).pack(pady=20)

# Run the game
root.mainloop()
