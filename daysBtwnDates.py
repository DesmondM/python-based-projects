import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_days():
    try:
        date_format = "%m/%d/%Y"
        date1 = datetime.strptime(entry_date1.get(), date_format)
        date2 = datetime.strptime(entry_date2.get(), date_format)
        difference = abs((date2 - date1).days)
        result_label.config(text=f"Difference: {difference} days")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter dates in MM/DD/YYYY format.")

# Create the main window
root = tk.Tk()
root.title("Date Difference Calculator")
root.geometry("300x200")

# Create and place widgets
tk.Label(root, text="Enter Date 1 (MM/DD/YYYY):").pack(pady=5)
entry_date1 = tk.Entry(root)
entry_date1.pack(pady=5)

tk.Label(root, text="Enter Date 2 (MM/DD/YYYY):").pack(pady=5)
entry_date2 = tk.Entry(root)
entry_date2.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Difference", command=calculate_days)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
