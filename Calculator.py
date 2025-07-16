import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg="#2e2e2e")

# Entry widget to display expressions
expression = ""
entry_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text, font=("Consolas", 24), bg="#1e1e1e", fg="#00ffcc", bd=0, relief=tk.FLAT, justify='right')
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=20)

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        entry_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        entry_text.set("")
        expression = ""

# Function to clear entry
def clear():
    global expression
    expression = ""
    entry_text.set("")

# Button configuration
button_font = ("Consolas", 18)
button_bg = "#3e3e3e"
button_fg = "#ffffff"
active_bg = "#555555"

# Frame for buttons
button_frame = tk.Frame(root, bg="#2e2e2e")
button_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+')
]

# Create buttons in grid
for row_idx, row in enumerate(buttons):
    for col_idx, char in enumerate(row):
        if char == 'C':
            action = clear
        else:
            action = lambda x=char: press(x)
        b = tk.Button(
            button_frame, text=char, font=button_font, width=5, height=2,
            bg=button_bg, fg=button_fg, activebackground=active_bg,
            relief=tk.RAISED, bd=3, command=action
        )
        b.grid(row=row_idx, column=col_idx, padx=5, pady=5)

# Equals button spanning full width
equal_button = tk.Button(
    root, text='=', font=("Consolas", 20), bg="#00cc99", fg="#ffffff",
    activebackground="#00b386", relief=tk.RAISED, bd=3, height=2,
    command=equalpress
)
equal_button.pack(fill="both", padx=10, pady=10)

# Start the app
root.mainloop()
