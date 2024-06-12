import tkinter as tk
from tkinter import messagebox

class LinearSearchApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def linear_search(self, arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1

    def display_numbers(self):
        user_input = self.entry_numbers.get()
        if not user_input.strip():
            messagebox.showerror("Input Error", "Please enter a list of numbers.")
            return
        
        try:
            numbers = [float(x) if '.' in x else int(x) for x in user_input.split()]
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid list of numbers separated by spaces.")
            return
        
        self.numbers_display.config(text=", ".join(map(str, numbers)))
        self.entry_numbers.delete(0, tk.END)

    def search_number(self):
        user_input = self.numbers_display.cget("text")
        target_input = self.entry_target.get()
        
        if not user_input or not target_input.strip():
            messagebox.showerror("Input Error", "Please enter both a list of numbers and a target number.")
            return
        
        try:
            numbers = [float(x) if '.' in x else int(x) for x in user_input.split(", ")]
            target = float(target_input) if '.' in target_input else int(target_input)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number to search for.")
            return
        
        index = self.linear_search(numbers, target)
        
        if index != -1:
            self.result_label.config(text=f"Number {target} found at index {index}.")
        else:
            self.result_label.config(text=f"Number {target} not found in the list.")

    def create_widgets(self):
        self.title_label = tk.Label(self.parent, text="Number Search with Linear Search", font=("Arial", 20, "bold"), fg="#02343F", bg='#F0EDCC')
        self.title_label.pack(pady=20)
        
        entry_numbers_label = tk.Label(self.parent, text="Enter a list of numbers separated by spaces:", font=("Poppins",15),fg="#02343F",bg="#F0EDCC")
        entry_numbers_label.pack(pady=5)
        
        self.entry_numbers = tk.Entry(self.parent, width=50)
        self.entry_numbers.pack(pady=5)
        
        display_button = tk.Button(self.parent, text="Display Numbers", command=self.display_numbers, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        display_button.pack(pady=10)
        
        self.numbers_display = tk.Label(self.parent, text="", fg="#02343F",bg="#F0EDCC", font=("Helvetica", 12))
        self.numbers_display.pack(pady=5)
        
        entry_target_label = tk.Label(self.parent, text="Enter the number to search for:",  font=("Poppins",15),fg="#02343F",bg="#F0EDCC")
        entry_target_label.pack(pady=5)
        
        self.entry_target = tk.Entry(self.parent, width=20)
        self.entry_target.pack(pady=5)
        
        search_button = tk.Button(self.parent, text="Search", command=self.search_number, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        search_button.pack(pady=10)
        
        self.result_label = tk.Label(self.parent, text="", fg="#02343F",bg="#F0EDCC", font=("Helvetica", 12))
        self.result_label.pack(pady=5)


