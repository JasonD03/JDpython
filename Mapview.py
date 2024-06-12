import tkinter as tk
from tkinter import messagebox
import tkintermapview

class MapView:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the map view
        self.map_view = tkintermapview.TkinterMapView(self.frame, width=1000, height=700, corner_radius=15)
        self.map_view.grid(row=0, column=0, sticky="nsew")

        # Entry and Button Widgets directly on top of the map view
        self.Entry_1_txt = "From"
        self.Entry_1 = tk.Entry(self.map_view, width=30, fg="gray")
        self.Entry_1.insert(0, self.Entry_1_txt)
        self.Entry_1.place(relx=0.95, rely=0.05, anchor='ne')

        self.Entry_2_txt = "To"
        self.Entry_2 = tk.Entry(self.map_view, width=30, fg="gray")
        self.Entry_2.insert(0, self.Entry_2_txt)
        self.Entry_2.place(relx=0.95, rely=0.10, anchor='ne')

        self.Entry_1.bind("<FocusIn>", self.clear_default_text)
        self.Entry_2.bind("<FocusIn>", self.clear_default_text)

        self.Button_1 = tk.Button(self.map_view, text="Search", command=self.search)
        self.Button_1.place(relx=0.95, rely=0.15, anchor='ne')

        self.satellite_button = tk.Button(self.map_view, text="Satellite", command=self.toggle_satellite)
        self.satellite_button.place(relx=0.95, rely=0.20, anchor='ne')

        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

    def clear_default_text(self, event):
        if event.widget == self.Entry_1 and self.Entry_1.get() == self.Entry_1_txt:
            self.Entry_1.delete(0, tk.END)
            self.Entry_1.config(fg="black")

        if event.widget == self.Entry_2 and self.Entry_2.get() == self.Entry_2_txt:
            self.Entry_2.delete(0, tk.END)
            self.Entry_2.config(fg="black")

    def search(self):
        from_address = self.Entry_1.get()
        to_address = self.Entry_2.get()

        marker_1 = self.map_view.set_address(from_address, marker=True)
        marker_2 = self.map_view.set_address(to_address, marker=True)

        if marker_1 and marker_2:
            self.map_view.set_path([marker_1.position, marker_2.position])
            self.map_view.update()
        else:
            messagebox.showerror("Search Error", "One or both of the addresses could not be found. Please enter valid addresses.")

    def toggle_satellite(self):
        if self.map_view.tile_server == "https://a.tile.openstreetmap.org/{z}/{x}/{y}.png":
            self.map_view.set_tile_server("https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}")
        else:
            self.map_view.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        self.map_view.update()