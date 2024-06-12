import tkinter as tk
from tkinter import messagebox
import random

class SudokuApp:
    def __init__(self, parent):
        self.parent = parent
        self.num = []
        self.temp2 = None
        self.create_widgets()

    def add_num(self):
        user_input = self.inputNumber_ent.get()
        if not user_input.isdigit() or int(user_input) < 1:
            messagebox.showerror("Input Error", "Please enter a valid positive integer.")
            return

        self.num = []
        for i in range(1, int(user_input) + 1):
            temp_num = list(range(1, int(user_input) + 1))
            random.shuffle(temp_num)
            self.num.append(temp_num)

        var1 = random.randint(0, int(user_input) - 1)
        var2 = random.randint(0, int(user_input) - 1)
        temp = self.num[var1]
        self.temp2 = temp[var2]
        self.num[var1][var2] = '?'

        for widget in self.sudoku_frm.winfo_children():
            widget.destroy()

        for n in range(len(self.num)):
            for j in range(len(self.num[n])):
                add = tk.Entry(self.sudoku_frm, font=("Arial", 10), width=5, justify='center')
                add.insert(0, self.num[n][j])
                add.configure(state='readonly')
                add.grid(row=n, column=j, padx=5, pady=5)

    def check_number(self):
        answer = self.temp2
        if self.inputMissing_ety.get() == str(answer):
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect!")

    def create_widgets(self):
        self.main_frame = tk.Frame(self.parent, bg="#02343F")
        self.main_frame.pack(expand=True)

        inputNumber_lbl = tk.Label(self.main_frame, text='Enter Number:', font=("Arial", 15), fg="#F0EDCC", bg="#02343F")
        inputNumber_lbl.grid(row=0, column=0, padx=10, pady=10)

        self.inputNumber_ent = tk.Entry(self.main_frame, width=25, font=("Arial", 10))
        self.inputNumber_ent.grid(row=0, column=1, padx=10, pady=10)

        inputNumber_btn = tk.Button(self.main_frame, text='Enter', font=("Arial", 10, "bold"), fg="#02343F", bg="#F0EDCC", command=self.add_num)
        inputNumber_btn.grid(row=0, column=2, padx=10, pady=10)

        self.sudoku_frm = tk.Frame(self.main_frame, width=270, height=270, bg='#02343F')
        self.sudoku_frm.grid(row=1, column=0, columnspan=3, pady=20)

        inputMissing_lbl = tk.Label(self.main_frame, text='Input Missing Number:', font=("Arial", 15), fg="#F0EDCC", bg="#02343F")
        inputMissing_lbl.grid(row=2, column=0, padx=10, pady=10)

        self.inputMissing_ety = tk.Entry(self.main_frame, width=25, font=("Arial", 10))
        self.inputMissing_ety.grid(row=2, column=1, padx=10, pady=10)

        inputMissing_btn = tk.Button(self.main_frame, text='Submit', font=("Arial", 10, "bold"), fg="#02343F",bg="#F0EDCC", command=self.check_number)
        inputMissing_btn.grid(row=2, column=2, padx=10, pady=10)

