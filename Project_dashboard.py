import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
from Mapview import MapView
from Coinchanger import CoinChanger
from Scheduling import ScheduleApp
from Linear_search import LinearSearchApp
from Binary_search import BinarySearchApp
from Selection_sort import SelectionSortApp
from Merge_sort import MergeSortApp
from Suduko3 import SudokuApp
# Initialize the main application window
master = tk.Tk()
master.geometry('1000x700')
master.configure(bg="#02343F")
master.overrideredirect(True)  # Hide the default title bar

# Create a custom title bar
title_bar = tk.Frame(master, bg="#02343F", relief="raised", bd=2)
title_bar.pack(side="top", fill="x")

# Title label
title_label = tk.Label(title_bar, text="Project Dashboard", bg="#02343F", fg="#F0EDCC", font=("Italic", 12, "bold"))
title_label.pack(side="left", padx=10)

# Minimize, Maximize, Close buttons
def minimize_window():
    master.overrideredirect(False)
    master.iconify()

def toggle_maximize():
    if master.state() == "normal":
        master.state("zoomed")
    else:
        master.state("normal")

def close_window():
    master.quit()

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
    master.x = event.x
    master.y = event.y

def stop_move(event):
    master.x = None
    master.y = None

def do_move(event):
    x = event.x_root - master.x
    y = event.y_root - master.y
    master.geometry(f"+{x}+{y}")

title_bar.bind("<ButtonPress-1>", start_move)
title_bar.bind("<ButtonRelease-1>", stop_move)
title_bar.bind("<B1-Motion>", do_move)

# Override the window manager functions for minimize and restore
def restore_window(event=None):
    master.overrideredirect(True)

master.bind("<Unmap>", lambda event: master.overrideredirect(False))
master.bind("<Map>", restore_window)

# Create the options frame
options = tk.Frame(master, bg="#02343F")
options.pack(pady=5)
options.pack_propagate(False)
options.configure(width=800, height=70, bd=2)

# Main frame where content will be displayed
main_frame = tk.Frame(master, bg="#02343F")
main_frame.pack(fill=tk.BOTH, expand=True)

# Switch function to handle frame changes
def switch(indicator, page_function):
    # Reset all indicators
    for child in options.winfo_children():
        if isinstance(child, tk.Label):
            child['bg'] = '#02343F'
    # Set the selected indicator
    indicator['bg'] = '#F0EDCC'
    
    # Clear the main frame
    for fm in main_frame.winfo_children():
        fm.destroy()
    
    # Load the new page
    page_function()

# Home page frame
def home_Page_Frame():
    home_page = tk.Frame(main_frame, bg="#02343F")
    home_page.pack(fill=tk.BOTH, expand=True)

    # Ensure the images are in the correct directory
    left_image_path = "Images/nemsulogo.jpg"
    right_image_path = "Images/citelogo.jpg"

    # Load the left image
    left_image = Image.open(left_image_path)
    left_mask = Image.new("L", (left_image.width, left_image.height), 0)
    left_draw = ImageDraw.Draw(left_mask)
    left_draw.ellipse((0, 0, left_image.width, left_image.height), fill=255)
    left_masked_image = left_image.copy()
    left_masked_image.putalpha(left_mask)
    left_resized_image = left_masked_image.resize((120, 120))
    left_Logo_image = ImageTk.PhotoImage(left_resized_image)  # Keep reference

    # Load the right image
    right_image = Image.open(right_image_path)
    right_mask = Image.new("L", (right_image.width, right_image.height), 0)
    right_draw = ImageDraw.Draw(right_mask)
    right_draw.ellipse((0, 0, right_image.width, right_image.height), fill=255)
    right_masked_image = right_image.copy()
    right_masked_image.putalpha(right_mask)
    right_resized_image = right_masked_image.resize((120, 120))
    right_Logo_image = ImageTk.PhotoImage(right_resized_image)  # Keep reference

    # Store references to the images in the home_Frame
    home_page.left_Logo_image = left_Logo_image
    home_page.right_Logo_image = right_Logo_image

    # Display logos in a top frame
    logo_frame = tk.Frame(home_page, background="#02343F")
    logo_frame.pack(side="top", fill="x", pady=10)

    left_logo_image_label = tk.Label(logo_frame, background="#02343F", image=left_Logo_image)
    left_logo_image_label.pack(side="left", padx=10)

    right_logo_image_label = tk.Label(logo_frame, background="#02343F", image=right_Logo_image)
    right_logo_image_label.pack(side="right", padx=10)

    # Create content frame below logos
    content_frame = tk.Frame(home_page, bg="#02343F")
    content_frame.pack(expand=True, fill=tk.BOTH)

    # Add new label with the provided text
    text = ("COMPILATION OF ACTIVITIES\n\n"
            "FINAL REQUIREMENTS\n\n"
            "(CS 221-Algorithm & Complexity)\n"
            "2nd Semester Ay 2023-2024\n\n"
            "In Partial Fulfillment of\n"
            "the Requirements for the Degree of\n"
            "Bachelor of Science in Computer Science\n\n"
            "Submitted by:\n\n"
            "Jason E. Diaz\n\n"
            "Submitted to:\n\n"
            "Mr. Virgilio F. Tuga jr.\n"
            "(Instructor)")
    
    info_lbl = tk.Label(content_frame, text=text, font=('Century Schoolbook', 14, "bold"), bg="#02343F", fg="#F0EDCC", width=50,justify=tk.CENTER)
    info_lbl.pack(pady=0)

# Coinchanger project frame
def project1_Page_Frame():
    project1_page = tk.Frame(main_frame, bg='#02343F')
    project1_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project1_page, text="Coin Changer Project", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project1_page, bg='#02343F')
    content_frame.pack(pady=0,expand=True,fill=tk.X)
    CoinChanger(content_frame)

def project2_Page_Frame():
    project2_page = tk.Frame(main_frame, bg='#02343F')
    project2_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project2_page, text="Scheduling", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project2_page, bg='#F0EDCC')
    content_frame.pack(expand=True, fill=tk.X,pady=50)
    ScheduleApp(content_frame)

# Mapview project frame
def project3_Page_Frame():
    project3_page = tk.Frame(main_frame, bg='#02343F')
    project3_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project3_page, text="Mapview Project", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project3_page, bg='#F0EDCC')
    content_frame.pack(expand=True, fill=tk.BOTH)
    MapView(content_frame)

# Sudoku project frame
def project4_page_Frame():
    project4_page = tk.Frame(main_frame, bg='#02343F')
    project4_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project4_page, text="Sudoku Version 3.0", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project4_page, bg='#F0EDCC')
    content_frame.pack(expand=True,fill=tk.BOTH)
    SudokuApp(content_frame)

def project5_page_Frame():
    project5_page = tk.Frame(main_frame, bg='#02343F')
    project5_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project5_page, text="Linear Search", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project5_page, bg='#F0EDCC')
    content_frame.pack(expand=True, fill=tk.X)
    LinearSearchApp(content_frame)

def project6_page_Frame():
    project6_page = tk.Frame(main_frame, bg='#02343F')
    project6_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project6_page, text="Binary Search", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project6_page, bg='#F0EDCC')
    content_frame.pack(expand=True, fill=tk.X)
    BinarySearchApp(content_frame)

def project7_page_Frame():
    project7_page = tk.Frame(main_frame, bg='#02343F')
    project7_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project7_page, text="Selection Sort", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project7_page, bg='#F0EDCC')
    content_frame.pack(expand=True,fill=tk.X)
    SelectionSortApp(content_frame)

def project8_page_Frame():
    project8_page = tk.Frame(main_frame, bg='#02343F')
    project8_page.pack(fill=tk.BOTH, expand=True)
    title_label = tk.Label(project8_page, text="Merge Sort", font=("Arial", 20, "bold"), bg='#02343F', fg="#F0EDCC")
    title_label.pack(pady=20)
    content_frame = tk.Frame(project8_page, bg='#F0EDCC')
    content_frame.pack(expand=True,fill=tk.X)
    MergeSortApp(content_frame)
# Create buttons for navigation
home_button = tk.Button(options, text='Home', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC",activebackground="Lightgray", activeforeground='#070952', command=lambda: switch(home_indicator, home_Page_Frame))
home_button.place(x=80, y=0, width=125)

project1_button = tk.Button(options, text='Coin Changer', font=('Tahoma', 11, 'bold'),bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project1_indicator, project1_Page_Frame))
project1_button.place(x=205, y=0, width=125)

project2_button = tk.Button(options, text='Scheduling', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project2_indicator, project2_Page_Frame))
project2_button.place(x=328, y=0, width=125)

project3_button = tk.Button(options, text='MapView', font=('Tahoma', 11, 'bold'),bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project3_indicator, project3_Page_Frame))
project3_button.place(x=450, y=0, width=125)

project4_button = tk.Button(options, text='Sudoku3', font=('Tahoma', 11, 'bold'),bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project4_indicator, project4_page_Frame))
project4_button.place(x=570, y=0, width=125)

project5_button = tk.Button(options, text='LinearSearch', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project5_indicator, project5_page_Frame))
project5_button.place(x=145, y=35, width=125)

project6_button = tk.Button(options, text='BinarySearch', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project6_indicator, project6_page_Frame))
project6_button.place(x=270, y=35, width=125)

project7_button = tk.Button(options, text='SelectionSort', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project7_indicator, project7_page_Frame))
project7_button.place(x=395, y=35, width=125)

project8_button = tk.Button(options, text='MergeSort', font=('Tahoma', 11, 'bold'), bd=0, fg='#02343F', bg="#F0EDCC", activebackground="Lightgray",activeforeground='#070952', command=lambda: switch(project8_indicator, project8_page_Frame))
project8_button.place(x=520, y=35, width=125)

# Create indicators for each button
home_indicator = tk.Label(options, bg="#F0EDCC")
home_indicator.place(x=98, y=30, width=80, height=2)

project1_indicator = tk.Label(options, bg="#F0EDCC")
project1_indicator.place(x=213, y=30, width=110, height=2)

project2_indicator = tk.Label(options, bg="#F0EDCC")
project2_indicator.place(x=340, y=30, width=95, height=2)

project3_indicator = tk.Label(options, bg="#F0EDCC")
project3_indicator.place(x=470, y=30, width=80, height=2)

project4_indicator = tk.Label(options, bg="#F0EDCC")
project4_indicator.place(x=590, y=30, width=80, height=2)

project5_indicator = tk.Label(options, bg="#F0EDCC")
project5_indicator.place(x=152, y=65, width=110, height=2)

project6_indicator = tk.Label(options, bg="#F0EDCC")
project6_indicator.place(x=278, y=65, width=108, height=2)

project7_indicator = tk.Label(options, bg="#F0EDCC")
project7_indicator.place(x=403, y=65, width=108, height=2)

project8_indicator = tk.Label(options, bg="#F0EDCC")
project8_indicator.place(x=540, y=65, width=90, height=2)

# Set the initial page to home_Page_Frame
switch(home_indicator, home_Page_Frame)

# Add footer
footer = tk.Label(master, text="Copyright © 2024 | All Rights Reserved.", fg="#02343F",background="#F0EDCC", font=("Arial", 12, "bold"))
footer.place(x=0, y=715, relwidth=1, height=50)
# Logout function
def logout():
    master.destroy()  # Destroy the entire application window
    open_login_form()  # Open the login form window
def open_login_form():
    import Login_form
    Login_form.main()

# Add the logout button to the footer
logout_button = tk.Button(footer, text="Logout", font=("Arial", 12, "bold"), bg="#02343F", fg="#F0EDCC", command=logout)
logout_button.pack(side=tk.RIGHT, padx=20, pady=10)

master.mainloop()
def main():
    pass

if __name__ == "__main__":
    main()