import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_text.delete("1.0", tk.END)  
        result_text.insert(tk.END, f"The product is: {product}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

root = tk.Tk()
root.geometry("400x300")
root.title("Getting Started with Widgets")

description_label = tk.Label(root,text="This application calculates the product of two numbers.",bg="#dff0d8",  fg="#3c763d", 
                             font=("Arial", 12))
description_label.pack(pady=10)

label1 = tk.Label(root, text="Enter the first number:", bg="#d9edf7", fg="#31708f", font=("Arial", 10))
label1.pack(pady=5)
entry1 = tk.Entry(root, bg="#ffffff", fg="#000000", font=("Arial", 10))
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter the second number:", bg="#d9edf7", fg="#31708f", font=("Arial", 10))
label2.pack(pady=5)
entry2 = tk.Entry(root, bg="#ffffff", fg="#000000", font=("Arial", 10))
entry2.pack(pady=5)

# Add a button 
calculate_button = tk.Button(
    root, 
    text="Calculate Product", 
    command=calculate_product,
    bg="#337ab7",
    fg="#ffffff",  
    font=("Arial", 10)
)
calculate_button.pack(pady=10)

# Add a Text widget
result_text = tk.Text(root, height=3, width=40, bg="#f7f7f9", fg="#333333", font=("Arial", 10))
result_text.pack(pady=10)

root.mainloop()
