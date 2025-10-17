from tkinter import *
import tkinter as tk

def button_click(value):
    # Insert the clicked button value into the currently focused Entry widget
    current_widget = root.focus_get()  # Get the currently focused widget
    if isinstance(current_widget, tk.Entry):  # Check if the focused widget is an Entry
        current = current_widget.get()
        current_widget.delete(0, tk.END)
        current_widget.insert(0, current + value)

def calculate_area():
    length = float(entry_for_length.get())
    width = float(entry_for_width.get())
    result = length * width
    result_label.config(text=f"Area: {result:.2f} square units")
    amount = result * 20
    amount_label.config(text=f"Total amount: {amount:.2f} $")
    discount = amount - ((amount * 5) / 100)
    discount_label.config(text=f"Due to 5% discount you have to pay: {discount:.2f} $")

# Root window setup
root = tk.Tk()
root.title("Tile Calculator")
root.geometry("600x600")  # Increase window size

# Length input
label_for_length = tk.Label(root, text="Enter length:")
label_for_length.grid(row=0, column=0, padx=10, pady=5)

entry_for_length = tk.Entry(root)
entry_for_length.grid(row=0, column=1, padx=10, pady=5)

# Width input
label_for_width = tk.Label(root, text="Enter width:")
label_for_width.grid(row=1, column=0, padx=10, pady=5)

entry_for_width = tk.Entry(root)
entry_for_width.grid(row=1, column=1, padx=10, pady=5)

# Results display
result_label = tk.Label(root, text="Area: -", font=("Helvetica", 14))
result_label.grid(row=10, column=1, columnspan=2, padx=10, pady=10)

amount_label = tk.Label(root, text="Total amount: -", font=("Helvetica", 14))
amount_label.grid(row=11, column=1, columnspan=2, padx=10, pady=10)

discount_label = tk.Label(root, text="Discount amount: -", font=("Helvetica", 14))
discount_label.grid(row=12, column=1, columnspan=2, padx=10, pady=10)

# Numeric buttons
button_texts = [
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
    ("0", 5, 1)
]

for text, row, col in button_texts:
    button = tk.Button(root, text=text, font=("Arial", 14), width=5, height=2,
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate Area", width=15, height=2, font=("Arial", 14),
                              command=calculate_area)
calculate_button.grid(row=8, column=1, columnspan=2, padx=10, pady=10)

root.mainloop()
