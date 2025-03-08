import tkinter as tk
from tkinter import filedialog, messagebox

def select_input_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, filename)

def select_output_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, filename)

def extract_sentences():
    input_file = input_entry.get()
    output_file = output_entry.get()
    keyword = keyword_entry.get().strip()
    
    if not input_file or not output_file or not keyword:
        messagebox.showerror("Error", "Please provide all inputs.")
        return
    
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            text = infile.read()
            sentences = [s.strip() for s in text.split('.') if keyword in s]
        
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(".\n".join(sentences) + ".\n")
        
        messagebox.showinfo("Success", "Sentences extracted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI Setup
root = tk.Tk()
root.title("Keyword Sentence Extractor")

# Input File
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=5, pady=5)

# Keyword
tk.Label(root, text="Keyword:").grid(row=1, column=0, padx=5, pady=5)
keyword_entry = tk.Entry(root, width=50)
keyword_entry.grid(row=1, column=1, padx=5, pady=5)

# Output File
tk.Label(root, text="Output File:").grid(row=2, column=0, padx=5, pady=5)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_file).grid(row=2, column=2, padx=5, pady=5)

# Extract Button
tk.Button(root, text="Extract Sentences", command=extract_sentences).grid(row=3, column=1, pady=10)

root.mainloop()
