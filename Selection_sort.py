import tkinter as tk
from tkinter import messagebox

class SelectionSortApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def selection_sort(self, input_array):
        for i in range(len(input_array)):
            min_index = i
            for j in range(i + 1, len(input_array)):
                if input_array[j] < input_array[min_index]:
                    min_index = j
            if min_index != i:
                input_array[i], input_array[min_index] = input_array[min_index], input_array[i]
        return input_array

    def sort_names(self):
        user_input = self.entry.get()
        unsorted_names = user_input.split()
        if not unsorted_names:
            messagebox.showerror("Input Error", "Please enter at least one name.")
            return
        sorted_names = self.selection_sort(unsorted_names)
        sorted_names_str = ", ".join(sorted_names)
        self.result_label.config(text=f"Sorted names: {sorted_names_str}")

    def create_widgets(self):
        title_label = tk.Label(self.parent, text="Name Sorter", font=("Helvetica", 16, "bold"), fg="#02343F", bg="#F0EDCC")
        title_label.pack(pady=10)

        entry_label = tk.Label(self.parent, text="Enter a list of unsorted names separated by spaces:",  fg="#02343F",bg="#F0EDCC", font=("Arial", 15))
        entry_label.pack(pady=5)

        self.entry = tk.Entry(self.parent, width=50)
        self.entry.pack(pady=5)

        sort_button = tk.Button(self.parent, text="Sort Names", command=self.sort_names, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        sort_button.pack(pady=10)

        self.result_label = tk.Label(self.parent, text="",  fg="#02343F",bg="#F0EDCC", font=("Helvetica", 12))
        self.result_label.pack(pady=10)
