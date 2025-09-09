import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_entry.get()
    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number for length.")
        return
    
    length = int(length)
    if length < 4:
        messagebox.showwarning("Too Short", "Password should be at least 4 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))

    result_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Tkinter window setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=5)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), width=30, state="readonly").pack(pady=5)

tk.Button(root, text="Copy to Clipboard", font=("Arial", 12), command=copy_to_clipboard).pack(pady=5)

root.mainloop()
