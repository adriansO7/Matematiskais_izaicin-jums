
import tkinter as tk
import random

# Krāsu palete
BG_COLOR = "#1A1A2E"
TEXT_COLOR = "#E94560"
BUTTON_COLOR = "#0F3460"
BUTTON_HOVER = "#16213E"

# Spēles sākotnējie dati
score = 0
time_left = 60
current_question = None

# Jauns jautājums
def generate_question():
    global current_question
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "/":
        num1 *= num2  # Nodrošina, ka dalīšana ir vesela
    current_question = (num1, operation, num2)
    
    question_label.config(text=f"{num1} {operation} {num2} = ?")

# Pārbauda atbildi
def check_answer():
    global score, time_left
    user_answer = answer_entry.get().strip()
    
    if not user_answer.isdigit():
        result_label.config(text="Ievadi skaitli!", fg="yellow")
        return
    
    user_answer = int(user_answer)
    num1, operation, num2 = current_question
    
    correct_answer = eval(f"{num1} {operation} {num2}")
    
    if user_answer == correct_answer:
        score += 1
        result_label.config(text="Pareizi!", fg="green")
    else:
        time_left -= 5
        result_label.config(text=f"Nepareizi! Pareizā atbilde: {correct_answer}", fg="red")
    
    answer_entry.delete(0, tk.END)
    generate_question()

# Atjauno laiku
def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Atlikušais laiks: {time_left} sek.")
        root.after(1000, update_timer)
    else:
        question_label.config(text="Spēle beigusies!")
        result_label.config(text=f"Tavs rezultāts: {score} punkti!", fg="gold")
        answer_entry.config(state="disabled")
        submit_button.config(state="disabled")

# Sāk spēli
def start_game():
    global score, time_left
    score = 0
    time_left = 60
    answer_entry.config(state="normal")
    submit_button.config(state="normal")
    generate_question()
    update_timer()

# Galvenais logs
root = tk.Tk()
root.title("Matemātikas izaicinājums")
root.geometry("500x400")
root.configure(bg=BG_COLOR)

# Virsraksts
title_label = tk.Label(root, text="Matemātikas izaicinājums", font=("Arial", 18, "bold"), bg=BG_COLOR, fg=TEXT_COLOR)
title_label.pack(pady=10)

# Taimeris
timer_label = tk.Label(root, text=f"Atlikušais laiks: {time_left} sek.", font=("Arial", 14), bg=BG_COLOR, fg="white")
timer_label.pack()

# Jautājums
question_label = tk.Label(root, text="", font=("Arial", 20, "bold"), bg=BG_COLOR, fg="white")
question_label.pack(pady=20)

# Ievades lauks
answer_entry = tk.Entry(root, font=("Arial", 16), width=10)
answer_entry.pack()

# Pogu sadaļa
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

submit_button = tk.Button(button_frame, text="Iesniegt", font=("Arial", 14, "bold"), bg=BUTTON_COLOR, fg="white", width=10, command=check_answer)
submit_button.grid(row=0, column=0, padx=5)

restart_button = tk.Button(button_frame, text="Sākt no jauna", font=("Arial", 14, "bold"), bg=BUTTON_COLOR, fg="white", width=12, command=start_game)
restart_button.grid(row=0, column=1, padx=5)

# Rezultāts
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg=BG_COLOR, fg="yellow")
result_label.pack(pady=10)

# Sāk spēli
start_game()

root.mainloop()