import tkinter as tk
from tkinter import messagebox

class MergeSortApp:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def merge_sort(self, input_array):
        if len(input_array) > 1:
            mid = len(input_array) // 2
            left_half = input_array[:mid]
            right_half = input_array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    input_array[k] = left_half[i]
                    i += 1
                else:
                    input_array[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                input_array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                input_array[k] = right_half[j]
                j += 1
                k += 1

        return input_array

    def sort_numbers(self):
        user_input = self.entry.get()
        try:
            unsorted_numbers = [float(x) if '.' in x else int(x) for x in user_input.split()]
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a list of numbers separated by spaces.")
            return

        sorted_numbers = self.merge_sort(unsorted_numbers)
        sorted_numbers_str = ", ".join(map(str, sorted_numbers))
        self.result_label.config(text=f"Sorted numbers: {sorted_numbers_str}")

    def create_widgets(self):
        self.title_label = tk.Label(self.parent, text="Number Sorter with Merge Sort", font=("Helvetica", 16, "bold"), fg="#02343F", bg="#F0EDCC")
        self.title_label.pack(pady=10)

        self.entry_label = tk.Label(self.parent, text="Enter a list of unsorted numbers separated by spaces:", fg="#02343F",bg="#F0EDCC",  font=("Poppins",15))
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.parent, width=50)
        self.entry.pack(pady=5)

        self.sort_button = tk.Button(self.parent, text="Sort Numbers", command=self.sort_numbers, bg="#02343F", fg="#F0EDCC", font=("Helvetica", 12))
        self.sort_button.pack(pady=10)

        self.result_label = tk.Label(self.parent, text="", fg="#02343F",bg="#F0EDCC", font=("Helvetica", 12))
        self.result_label.pack(pady=5)