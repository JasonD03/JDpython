import tkinter as tk

# coinchanger.py

class CoinChanger:
    def __init__(self, master):
        self.master = master

        # Configure the main frame's row and column weights for responsive resizing
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        # Create frames for the left and right sections
        left_frame = tk.Frame(self.master, bd=2, relief='sunken', bg="#F0EDCC")
        right_frame = tk.Frame(self.master, bd=2, relief='sunken', bg="#F0EDCC")

        # Place the frames in the grid
        left_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)
        right_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

        # Configure the frames' row and column weights
        for i in range(4):
            left_frame.grid_rowconfigure(i, weight=1)
            left_frame.grid_columnconfigure(0, weight=1)
            right_frame.grid_rowconfigure(i, weight=1)
            right_frame.grid_columnconfigure(0, weight=1)

        # Components for available coins
        self.label_coins = tk.Label(left_frame, text='Enter available coins separated by spaces:', bg="#F0EDCC", fg="#02343F", font=("Arial", 12))
        self.label_coins.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.entry_coins = tk.Entry(left_frame, font=("Arial", 12))
        self.entry_coins.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.add_coins_button = tk.Button(left_frame, text='Enter Coins', bg="#02343F", fg="#F0EDCC", command=self.add_coins, font=("Arial", 12))
        self.add_coins_button.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        self.listbox_available_coins = tk.Listbox(left_frame, font=("Arial", 12))
        self.listbox_available_coins.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)

        self.clear_available_coins_button = tk.Button(left_frame, text='Clear Available Coins', bg="#02343F", fg="#F0EDCC",command=self.clear_available_coins, font=("Arial", 12))
        self.clear_available_coins_button.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

        # Components for amount and change
        self.label_amount = tk.Label(right_frame, text='Enter the amount you want to change:', bg="#F0EDCC", fg="#02343F", font=("Arial", 12))
        self.label_amount.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.entry_amount = tk.Entry(right_frame, font=("Arial", 12))
        self.entry_amount.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

        self.calculate_button = tk.Button(right_frame, text='Calculate Change', bg="#02343F", fg="#F0EDCC",command=self.calculate_change, font=("Arial", 12))
        self.calculate_button.grid(row=2, column=0, sticky='ew', padx=5, pady=5)

        self.scrollbar_change = tk.Scrollbar(right_frame)
        self.scrollbar_change.grid(row=3, column=1, sticky='ns')

        self.listbox_change = tk.Listbox(right_frame, font=("Arial", 12))
        self.listbox_change.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)
        self.scrollbar_change.config(command=self.listbox_change.yview)
        self.listbox_change.config(yscrollcommand=self.scrollbar_change.set)

        self.clear_change_button = tk.Button(right_frame, text='Clear Change', bg="#02343F", fg="#F0EDCC",command=self.clear_change, font=("Arial", 12))
        self.clear_change_button.grid(row=4, column=0, sticky='ew', padx=5, pady=5)

    def add_coins(self):
        coins = self.entry_coins.get().split()
        self.listbox_available_coins.delete(0, tk.END)
        for coin in coins:
            self.listbox_available_coins.insert(tk.END, f'Coin: {coin}')

    def clear_available_coins(self):
        self.listbox_available_coins.delete(0, tk.END)

    def calculate_change(self):
        coins = list(map(int, [coin.strip('Coin: ') for coin in self.listbox_available_coins.get(0, tk.END)]))
        amount = int(self.entry_amount.get())
        change = self.greedy_coin_change(coins, amount)
        self.display_change(change)

    def clear_change(self):
        self.listbox_change.delete(0, tk.END)

    def greedy_coin_change(self, coins, amount):
        coins.sort(reverse=True)
        change = []
        for coin in coins:
            while amount >= coin:
                amount -= coin
                change.append(coin)
        return change if amount == 0 else 'Change not possible'

    def display_change(self, change):
        self.listbox_change.delete(0, tk.END)
        if isinstance(change, str):
            self.listbox_change.insert(tk.END, change)
        else:
            for coin in change:
                self.listbox_change.insert(tk.END, f'Coin: {coin}')
