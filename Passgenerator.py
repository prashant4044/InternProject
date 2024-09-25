import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = length_var.get()
    characters = []

    if lowercase_var.get():
        characters.extend(string.ascii_lowercase)
    if uppercase_var.get():
        characters.extend(string.ascii_uppercase)
    if numbers_var.get():
        characters.extend(string.digits)
    if symbols_var.get():
        characters.extend(string.punctuation)

    if not characters:
        # Ensure at least one character type is selected
        tk.messagebox.showwarning("Error", "Please select at least one character type.")
        return

    if exclude_duplicates_var.get():
        password = ''.join(random.sample(characters, password_length))
    else :
        password = ''.join(random.choice(characters) for _ in range(password_length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        tk.messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
         tk.messagebox.showwarning("Warning", "No password to copy!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")

main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

length_var = tk.IntVar(value=12)
length_label = ttk.Label(main_frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_spinbox = ttk.Spinbox(main_frame, from_=8, to=50, textvariable=length_var, width=5)
length_spinbox.grid(row=0, column=1, padx=5, pady=5)

lowercase_var = tk.BooleanVar(value=True)
lowercase_checkbox = ttk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var)
lowercase_checkbox.grid(row=1, column=0, padx=5, pady=5)

uppercase_var = tk.BooleanVar(value=True)
uppercase_checkbox = ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=1, padx=5, pady=5)

numbers_var = tk.BooleanVar(value=True)
numbers_checkbox = ttk.Checkbutton(main_frame, text="Numbers", variable=numbers_var)
numbers_checkbox.grid(row=2, column=0, padx=5, pady=5)

symbols_var = tk.BooleanVar(value=True)
symbols_checkbox = ttk.Checkbutton(main_frame, text="Symbols", variable=symbols_var)
symbols_checkbox.grid(row=2, column=1, padx=5, pady=5)

exclude_duplicates_var = tk.BooleanVar(value=False)
exclude_duplicates_checkbox = ttk.Checkbutton(main_frame, text="Exclude Duplicates", variable=exclude_duplicates_var)
exclude_duplicates_checkbox.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

password_entry = ttk.Entry(main_frame, width=40)
password_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=copy_password)
copy_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()