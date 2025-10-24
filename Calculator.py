import tkinter as tk

calculation = ""

# --- Functions ---
def calculate():
    global calculation
    try:
        result = str(eval(calculation))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
        calculation = result
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
        calculation = ""

def clear():
    global calculation
    calculation = ""
    entry.delete(0, tk.END)

def button_click(value):
    global calculation
    calculation += str(value)
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# --- Color Scheme ---
BG_COLOR = "#1e1e1e"      # window background
ENTRY_BG = "#2d2d2d"      # entry background
BTN_COLOR = "#3c3c3c"     # button background
TEXT_COLOR = "#ff8c00"    # dark orange for text
ACCENT_COLOR = "#ff8c00"  # operators and "="
CLEAR_COLOR = "#e53935"   # clear button

# --- Main Window ---
root = tk.Tk()
root.title("🧮 Calculator")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# --- Entry Widget ---
entry = tk.Entry(root, font=("Consolas", 22, "bold"), bd=5, relief="flat",
                 justify="right", bg=ENTRY_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
entry.grid(row=0, column=0, columnspan=4, pady=10, ipady=10)

# --- Buttons Layout ---
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    color = ACCENT_COLOR if text in ['+', '-', '*', '/', '='] else BTN_COLOR
    text_color = BTN_COLOR if text in ['+', '-', '*', '/', '='] else TEXT_COLOR 
    btn = tk.Button(root, text=text, font=("Consolas", 20, "bold"), bg=color, fg=text_color,
                    relief="flat", width=4, height=2,
                    command=lambda value=text: calculate() if value == "=" else button_click(value))
    btn.grid(row=row, column=col, padx=5, pady=5)

# --- Clear Button ---
clear_btn = tk.Button(root, text="C", font=("Consolas", 20, "bold"),
                      bg=CLEAR_COLOR, fg="white", relief="flat",
                      width=17, height=2, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
