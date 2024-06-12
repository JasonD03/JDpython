import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


class LoginForm(tk.Frame):
    def __init__(self, parent, on_login_success):
        super().__init__(parent, bg="white")
        self.configure(width=650, height=500)
        self.on_login_success = on_login_success

        # Load the background image
        image_path = "Images/jj.jpg"
        image_obj = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image_obj)

        # Create a label with the background image
        main_label = tk.Label(self, image=photo_image)
        main_label.place(x=0, y=0, relwidth=1, relheight=1)
        main_label.image = photo_image  # Keep a reference to the image to prevent garbage collection

        # Create a frame
        main_frame = tk.Frame(self, width=350, height=330, padx=20, pady=20, bg="#02343F", relief="raised", bd=5)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        original_image = Image.open("Images/OIP.jpg")
        # Create a circular mask
        mask = Image.new("L", (original_image.width, original_image.height), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, original_image.width, original_image.height), fill=255)

        # Apply the circular mask to the original image
        masked_image = original_image.copy()
        masked_image.putalpha(mask)

        # Resize the masked image
        resized_image = masked_image.resize((100, 100))

        # Convert the resized image to PhotoImage
        self.Logo_image = ImageTk.PhotoImage(resized_image)

        # Profile Image
        self.Logo_image_label = tk.Label(main_frame, background="#02343F", image=self.Logo_image)
        self.Logo_image_label.grid(row=0, columnspan=2, padx=10, pady=(10, 5), sticky="n")

        # Load the eye image
        self.eye_image = Image.open("Images/hidden.png")
        self.eye_image = self.eye_image.resize((14, 14))
        self.eye_photo_image = ImageTk.PhotoImage(self.eye_image)

        self.eye_image_hidden = Image.open("Images/view.png")
        self.eye_image_hidden = self.eye_image_hidden.resize((14, 14))
        self.eye_photo_image_hidden = ImageTk.PhotoImage(self.eye_image_hidden)

        username_frame = tk.Frame(main_frame, background="#02343F")
        username_frame.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        # Username Entry
        self.username_label = tk.Label(main_frame, background="#02343F", text="Username:", fg="#F0EDCC", font=("Italic", 12, "bold"))
        self.username_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.username_entry = tk.Entry(username_frame, width=25)
        self.username_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Password Entry
        password_frame = tk.Frame(main_frame, background="#02343F")
        password_frame.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.password_label = tk.Label(main_frame, background="#02343F", text="Password:", fg="#F0EDCC", font=("Italic", 12, "bold"))
        self.password_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(password_frame, width=25, show="*")
        self.password_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.eye_label = tk.Label(password_frame, image=self.eye_photo_image, cursor="hand2")
        self.eye_label.place(relx=0.9, rely=0.5, anchor=tk.E)
        self.eye_label.bind("<Button-1>", self.toggle_password_visibility)

        # Forgot Password
        self.forgot_password_label = tk.Label(main_frame, background="#02343F", font=("Italic", 9, "bold"), text="Forgot password?", cursor="hand2", fg="Skyblue")
        self.forgot_password_label.grid(row=5, columnspan=2, padx=10, pady=5, sticky="nsew")
        self.forgot_password_label.bind("<Button-1>", self.forgot_password)

        # Frame for Login and Exit buttons
        button_frame = tk.Frame(main_frame, background="#02343F")
        button_frame.grid(row=6, columnspan=2, pady=10)

        # Login Button
        self.login_button = tk.Button(button_frame, text="Login", bg="#F0EDCC", fg="#02343F", font=("Italic", 9, "bold"), command=self.login)
        self.login_button.pack(side="left", padx=(10, 5))
        self.login_button.config(width=10, height=2)  # Resize the button

        # Exit Button
        self.exit_button = tk.Button(button_frame, text="Exit", bg="#F0EDCC", fg="#02343F", font=("Italic", 9, "bold"), command=self.quit_application)
        self.exit_button.pack(side="right", padx=(10, 5))
        self.exit_button.config(width=10, height=2)  # Resize the button

        # Centering the image horizontally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Bind the Enter key to the login function
        self.bind("<Return>", self.login)

    def toggle_password_visibility(self, event):
        if self.password_entry["show"] == "*":
            self.password_entry["show"] = ""
            self.eye_label.config(image=self.eye_photo_image_hidden)
        else:
            self.password_entry["show"] = "*"
            self.eye_label.config(image=self.eye_photo_image)

    def forgot_password(self, event):
        messagebox.showwarning("Forgot Password", "Please contact the administrator for assistance.")

    def login(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "jasond" and password == "habibi":
            messagebox.showinfo("Hello 😊", "Greetings!, Welcome to my\n Project Dashboard!")
            self.on_login_success()
        elif username != "jasond" and password != "habibi":
            messagebox.showerror("Invalid Login", "The username and password are both invalid.")
        elif username != "jasond":
            messagebox.showerror("Invalid Username", "The username is invalid.")
        elif password != "habibi":
            messagebox.showerror("Invalid Password", "The password is invalid.")

    def quit_application(self, event=None):
        root.quit()  # Quit the main application loop
        root.destroy()  # Destroy the entire application window


def on_login_success():
    root.destroy()  # Destroy the login window
    open_project_dashboard()  # Open the project dashboard

def open_project_dashboard():
    import Project_dashboard
    Project_dashboard.main()

def main():
    global root
    root = tk.Tk()
    root.geometry("650x500")
    root.overrideredirect(True)  # Hide the default title bar

    # Create a custom title bar
    title_bar = tk.Frame(root, bg="#02343F", relief="raised", bd=2)
    title_bar.pack(side="top", fill="x")

    # Title label
    title_label = tk.Label(title_bar, text="Login Form", bg="#02343F", fg="#F0EDCC", font=("Italic", 12, "bold"))
    title_label.pack(side="left", padx=10)

    # Minimize, Maximize, Close buttons
    def minimize_window():
        root.overrideredirect(False)
        root.iconify()

    def toggle_maximize():
        if root.state() == "normal":
            root.state("zoomed")
        else:
            root.state("normal")

    def close_window():
        root.quit()

    button_frame = tk.Frame(title_bar, bg="#02343F")
    button_frame.pack(side="right")

    minimize_button = tk.Button(button_frame, text="__", bg="#02343F", fg="#F0EDCC", command=minimize_window, bd=0, padx=5, pady=2)
    minimize_button.pack(side="left")

    maximize_button = tk.Button(button_frame, text="⬜", bg="#02343F", fg="#F0EDCC", command=toggle_maximize, bd=0, padx=5, pady=2)
    maximize_button.pack(side="left")

    close_button = tk.Button(button_frame, text="X", bg="#02343F", fg="#F0EDCC", command=close_window, bd=0, padx=5, pady=2)
    close_button.pack(side="left")

    # Add functionality to drag the window
    def start_move(event):
        root.x = event.x
        root.y = event.y

    def stop_move(event):
        root.x = None
        root.y = None

    def do_move(event):
        x = event.x_root - root.x
        y = event.y_root - root.y
        root.geometry(f"+{x}+{y}")

    title_bar.bind("<ButtonPress-1>", start_move)
    title_bar.bind("<ButtonRelease-1>", stop_move)
    title_bar.bind("<B1-Motion>", do_move)

    # Create an instance of LoginForm
    login_form = LoginForm(root, on_login_success)
    login_form.pack(fill=tk.BOTH, expand=True)

    # Override the window manager functions for minimize and restore
    def restore_window(event=None):
        root.overrideredirect(True)

    root.bind("<Unmap>", lambda event: root.overrideredirect(False))
    root.bind("<Map>", restore_window)

    root.mainloop()


if __name__ == "__main__":
    main()
