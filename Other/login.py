import tkinter as tk
from tkinter import messagebox

def submit_number():
    phone_number = phone_number_entry.get()
    # Here you would normally handle the phone number, e.g., validation, saving, etc.
    messagebox.showinfo("Submitted", "Phone Number Submitted: " + phone_number)
    # Here you could proceed to the next screen or close the login window

# Create the main window
root = tk.Tk()
root.title("EASY MACROS")

# Set the window size and position
root.geometry("400x300+500+200")

# Add a label
label = tk.Label(root, text="Please Enter Your Phone Number", font=("Helvetica", 16))
label.pack(pady=20)

# Add an entry widget
phone_number_entry = tk.Entry(root, font=("Helvetica", 16), justify='center')
phone_number_entry.pack(pady=10)

# Add a submit button
submit_button = tk.Button(root, text="Submit", command=submit_number)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
