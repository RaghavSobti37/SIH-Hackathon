import tkinter as tk
import random
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

# Function to generate a random math problem
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(["+", "-", "x"])  # Addition, Subtraction, Multiplication
    if operator == "+":
        answer = num1 + num2
        operator_image = create_image("+")
    elif operator == "-":
        answer = num1 - num2
        operator_image = create_image("-")
    else:
        answer = num1 * num2
        operator_image = create_image("x")
    return f"{num1} {operator} {num2}", answer, operator_image

# Function to check the user's answer and handle button switching
def submit_or_next():
    global score, question_count
    if submit_button.cget("text") == "Submit":
        user_answer = entry.get()
        try:
            user_answer = int(user_answer)
            if user_answer == answer:
                result_label.config(text="Correct!", fg="green")
                score += 1
            else:
                result_label.config(text="Incorrect!", fg="red")
            question_count += 1
            if question_count < 5:
                submit_button.config(text="Next")
            else:
                submit_button.config(text="Finish", state="active")
            entry.config(state="disabled")
            entry.delete(0, "end")  # Clear the answer after submission
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
    else:
        if question_count < 5:
            next_problem()
        else:
            finish_game()

# Function to generate a new problem
def next_problem():
    global answer, operator_image
    problem, answer, operator_image = generate_problem()
    problem_label.config(text=problem)
    operator_label.config(image=operator_image)
    entry.delete(0, "end")  # Clear the answer field
    result_label.config(text="", fg="black")
    submit_button.config(text="Submit", state="active")
    entry.config(state="normal")

# Function to finish the game and show the score
def finish_game():
    result_label.config(text=f"Game over! Your score is {score}/5", fg="blue")
    submit_button.config(state="disabled")

# Function to create an operator image
def create_image(operator):
    image = Image.new("RGBA", (50, 50), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.text((15, 15), operator, fill="black", font=None)
    return ImageTk.PhotoImage(image)

# Create the main window
window = tk.Tk()
window.title("Math Learning Game")

score = 0
question_count = 0

# Create a label for the problem
problem_label = tk.Label(window, text="", font=("Arial", 24))
problem_label.pack(pady=20)

# Create an image label for the operator
operator_image = create_image("")
operator_label = tk.Label(window, image=operator_image)
operator_label.pack(pady=20)

# Create an entry for the user's answer
entry = tk.Entry(window, font=("Arial", 20))
entry.pack()

# Create a single button for Submit/Next
submit_button = tk.Button(window, text="Submit", command=submit_or_next)
submit_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(window, text="", font=("Arial", 20))
result_label.pack(pady=10)

# Start the game
next_problem()

# Run the GUI
window.mainloop()
