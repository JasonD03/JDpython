import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.create_widgets()
        self.schedule = []

    def create_widgets(self):
        self.root.update()  # Ensure the dimensions are up to date

        # Configuring the root grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=5)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Day of the Week
        self.day_label = tk.Label(self.root, text="Day of the Week:", fg="#02343F",bg="#F0EDCC")
        self.day_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

        self.day_var = tk.StringVar()
        self.day_menu = ttk.Combobox(self.root, textvariable=self.day_var)
        self.day_menu['values'] = self.days_of_week
        self.day_menu.grid(row=0, column=1, sticky="w", padx=10, pady=10)

        # Subject
        self.subject_label = tk.Label(self.root, text="Subject:", fg="#02343F",bg="#F0EDCC")
        self.subject_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

        # Start Time
        self.start_time_label = tk.Label(self.root, text="Start Time (HH:MM am/pm):", fg="#02343F",bg="#F0EDCC")
        self.start_time_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

        self.start_time_entry = tk.Entry(self.root)
        self.start_time_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        # End Time
        self.end_time_label = tk.Label(self.root, text="End Time (HH:MM am/pm):", fg="#02343F",bg="#F0EDCC")
        self.end_time_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

        self.end_time_entry = tk.Entry(self.root)
        self.end_time_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        # Add Interval Button
        self.add_button = tk.Button(self.root, text="Add Interval", fg="#F0EDCC", bg="#02343F", command=self.add_interval)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)

        # Clear Table Button
        self.clear_button = tk.Button(self.root, text="Clear Table", fg="#F0EDCC",bg="#02343F", command=self.clear_table)
        self.clear_button.grid(row=4, column=1, padx=10, pady=10)

        # Treeview
        self.tree = ttk.Treeview(self.root, columns=("Day", "Subject", "Start Time", "End Time"), show="headings")
        self.tree.heading("Day", text="Day")
        self.tree.heading("Subject", text="Subject")
        self.tree.heading("Start Time", text="Start Time")
        self.tree.heading("End Time", text="End Time")
        self.tree.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

        # Configure treeview scrollbars
        self.scroll_y = tk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.scroll_y.grid(row=5, column=2, sticky="ns")
        self.tree.configure(yscrollcommand=self.scroll_y.set)

    def add_interval(self):
        day = self.day_var.get()
        subject = self.subject_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()

        if not day or not subject or not start_time or not end_time:
            messagebox.showwarning("Input Error", "All fields must be filled.")
            return

        if not self.is_valid_time_format(start_time) or not self.is_valid_time_format(end_time):
            messagebox.showwarning("Input Error", "Time must be in HH:MM am/pm format.")
            return

        if self.is_conflict(day, start_time, end_time):
            messagebox.showerror("Conflict", "Schedule conflict detected.")
            return

        self.schedule.append((day, start_time, end_time))
        self.tree.insert("", "end", values=(day, subject, start_time, end_time))

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.schedule.clear()

    def is_valid_time_format(self, time_str):
        pattern = r"^(1[0-2]|0?[1-9]):([0-5]?[0-9]) (AM|PM|am|pm)$"
        return re.match(pattern, time_str)

    def is_conflict(self, day, start_time, end_time):
        start_time_minutes = self.time_to_minutes(start_time)
        end_time_minutes = self.time_to_minutes(end_time)

        for sched_day, sched_start, sched_end in self.schedule:
            if sched_day == day:
                sched_start_minutes = self.time_to_minutes(sched_start)
                sched_end_minutes = self.time_to_minutes(sched_end)
                if start_time_minutes < sched_end_minutes and end_time_minutes > sched_start_minutes:
                    return True
        return False

    def time_to_minutes(self, time_str):
        hours, minutes, am_pm = re.match(r"^(1[0-2]|0?[1-9]):([0-5]?[0-9]) (AM|PM|am|pm)$", time_str).groups()
        hours = int(hours)
        minutes = int(minutes)
        if am_pm.lower() == 'pm' and hours != 12:
            hours += 12
        elif am_pm.lower() == 'am' and hours == 12:
            hours = 0
        return hours * 60 + minutes



