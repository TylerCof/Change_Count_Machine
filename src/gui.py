import tkinter as tk
from tkinter import messagebox
import re
from change_count_machine import compute_change

def create_gui():

    def on_calculate():
        try:
            user_input = entry.get()
            
            # Check if the input has more than 2 decimal places
            if '.' in user_input and len(user_input.split('.')[-1]) > 2:
                messagebox.showerror("Error", "Please enter a number with no more than two decimal places.")
                return

            money = float(user_input)
            
            if money < 0:
                messagebox.showerror("Error", "Amount cannot be negative.")
                return
            
            total_items, denom_counts = compute_change(money) #Collecting results from compute_change
            result_text = f"Total items: {total_items}\nDenomination breakdown:\n"
            for denom, count in denom_counts.items():
                result_text += f"${denom:.2f}: {count}\n"
            result_label.config(text=result_text) #Displaying results to the GUI
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    root = tk.Tk()
    root.title("Change Count Machine")

    # Set a custom theme (dark background, light text)
    root.configure(bg='#2E2E2E')  # Dark background color
    root.option_add("*Font", "Arial 12")  # Set default font for all widgets
    root.option_add("*Foreground", "white")  # Text color
    root.option_add("*Background", "#3A3A3A")  # Background color for widgets

    # Create a frame to contain both the dollar sign and the entry widget
    entry_frame = tk.Frame(root, bg="#2E2E2E")  # Dark frame background color
    
    # Create a label for the dollar sign with a bright color
    dollar_sign_label = tk.Label(entry_frame, text="$", fg="lightgreen", bg="#2E2E2E", font=("Arial", 12))
    
    # Create the entry widget for user input with customized color
    entry = tk.Entry(entry_frame, font=("Arial", 12), fg="black", bg="white", bd=2, relief="solid")
    
    # Pack the label and entry widget in the frame
    dollar_sign_label.pack(side="left", padx=5)
    entry.pack(side="left", padx=5)

    # Button to trigger calculation with modern style
    calculate_button = tk.Button(root, text="Calculate", command=on_calculate, font=("Arial", 12),
                                 fg="white", bg="#4CAF50", relief="flat", padx=10, pady=5)

    # Label to display the results with brighter background
    result_label = tk.Label(root, text="", bg="#2E2E2E", fg="lightblue", font=("Arial", 12))

    # Pack the widgets
    entry_frame.pack(pady=10)
    calculate_button.pack(pady=10)
    result_label.pack(pady=10)

    return root, entry, calculate_button, result_label  # For testing returning GUI features

# Uncomment to run the GUI
#create_gui()[0].mainloop()
