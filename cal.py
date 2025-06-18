import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Full-Screen Calculator")
window.configure(bg="#f0f0f0")  # Light grey background
window.state('zoomed')  # Fullscreen for Windows

# Configure grid layout for responsiveness
for i in range(6):  # 1 row for entry + 5 rows for buttons
    window.rowconfigure(i, weight=1)
for j in range(4):  # 4 columns for buttons
    window.columnconfigure(j, weight=1)

# Style configuration for buttons using ttk
style = ttk.Style()
style.configure("Calc.TButton",
                font=("Arial", 28),
                padding=10,
                relief="flat",
                background="#ffffff")
style.map("Calc.TButton",
          background=[('active', '#e6e6e6')],
          relief=[('pressed', 'sunken')])

# Entry field
entry = tk.Entry(window, font=('Arial', 40), borderwidth=0, relief="flat",
                 justify='right', bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=20, pady=20)

# Backend Functions
def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        ttk.Button(window, text=text, style="Calc.TButton", command=button_equal)\
            .grid(row=row, column=col, sticky='nsew', padx=10, pady=10)
    else:
        ttk.Button(window, text=text, style="Calc.TButton", command=lambda t=text: button_click(t))\
            .grid(row=row, column=col, sticky='nsew', padx=10, pady=10)

# Clear button at the bottom
ttk.Button(window, text='C', style="Calc.TButton", command=button_clear)\
    .grid(row=5, column=0, columnspan=4, sticky='nsew', padx=20, pady=20)

# Start the GUI event loop
window.mainloop()
