import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)
display.pack(fill="both", padx=10, pady=10, ipady=10)

def button_click(value):
    display.insert(tk.END, value)
def clear_display():
    display.delete(0, tk.END)
def calculate():
    try:
        expression = display.get()
        if not expression:
            return
        allowed_characters = "0123456789.+-*/() "
        if any(char not in allowed_characters for char in expression):
            raise ValueError

        result = eval(expression, {"__builtins__": None}, {})
        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")
    except (ValueError, SyntaxError, TypeError):
        messagebox.showerror("Error", "Invalid input!")
    except Exception:
        messagebox.showerror("Error", "Something went wrong!")

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(expand=True, fill="both", padx=10, pady=10)
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), (".", 3, 1), ("+", 3, 2), ("=", 3, 3),
]
for text, row, column in buttons:
    if text == "=":
        command = calculate
    else:
        command = lambda value=text: button_click(value)
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18),
        command=command,
        width=5,
        height=2
    )
    button.grid(row=row, column=column, padx=5, pady=5)

clear_button = tk.Button(
    root,
    text="CLEAR",
    font=("Arial", 16),
    command=clear_display,
    bg="#ffcccc"
)
clear_button.pack(fill="both", padx=15, pady=10, ipady=5)


# Run the application
root.mainloop()
