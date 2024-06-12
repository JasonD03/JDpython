import tkinter as tk
from tkinter import messagebox

class BinarySearchApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def display_names(self):
        user_input = self.entry_names.get()
        if not user_input.strip():
            messagebox.showerror("Input Error", "Please enter a list of names.")
            return
        
        self.names = user_input.split()
        self.names_display.config(text=", ".join(self.names))
        self.entry_names.delete(0, tk.END)

    def perform_search(self):
        if not hasattr(self, 'names'):
            messagebox.showerror("Input Error", "Please enter and display a list of names first.")
            return
        
        target_input = self.entry_target.get()
        if not target_input.strip():
            messagebox.showerror("Input Error", "Please enter a target name.")
            return

        target = target_input.strip()
        
        sorted_names = sorted(self.names)
        index_in_sorted = self.binary_search(sorted_names, target)
        
        if index_in_sorted != -1:
            original_index = self.names.index(sorted_names[index_in_sorted])
            self.result_label.config(text=f"Name '{target}' found at original index {original_index}.")
        else:
            self.result_label.config(text=f"Name '{target}' not found.")

    def create_widgets(self):
        title_label = tk.Label(self.parent, text="Binary Search for Names", font=("Helvetica", 16, "bold"), fg="#02343F", bg="#F0EDCC")
        title_label.pack(pady=10)

        entry_label_names = tk.Label(self.parent, text="Enter a list of names separated by spaces:", fg="#02343F", bg="#F0EDCC", font=("Arial", 15,))
        entry_label_names.pack(pady=5)

        self.entry_names = tk.Entry(self.parent, width=50)
        self.entry_names.pack(pady=5)

        display_button = tk.Button(self.parent, text="Display Names", command=self.display_names, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        display_button.pack(pady=10)

        self.names_display = tk.Label(self.parent, text="", fg="#02343F", bg="#F0EDCC", font=("Helvetica", 12))
        self.names_display.pack(pady=5)

        entry_label_target = tk.Label(self.parent, text="Enter the name to search for:", fg="#02343F", bg="#F0EDCC",  font=("Arial", 15,))
        entry_label_target.pack(pady=5)

        self.entry_target = tk.Entry(self.parent, width=50)
        self.entry_target.pack(pady=5)

        search_button = tk.Button(self.parent, text="Search", command=self.perform_search, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        search_button.pack(pady=10)

        self.result_label = tk.Label(self.parent, text="", fg="#02343F", bg="#F0EDCC", font=("Helvetica", 12))
        self.result_label.pack(pady=5)