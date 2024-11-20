from change_count_machine import compute_change
import tkinter as tk
from tkinter import messagebox

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

    # Create a frame to contain both the dollar sign and the entry widget
    entry_frame = tk.Frame(root)
    
    # Create a label for the dollar sign
    dollar_sign_label = tk.Label(entry_frame, text="$", font=("Arial", 12))
    
    # Create the entry widget for user input
    entry = tk.Entry(entry_frame, font=("Arial", 12))
    
    # Pack the label and entry widget in the frame
    dollar_sign_label.pack(side="left")
    entry.pack(side="left")
    

    calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
    result_label = tk.Label(root, text="", font=("Arial", 12))

    # Pack the widgets
    entry_frame.pack(pady=5)
    calculate_button.pack(pady=5)
    result_label.pack(pady=10)

    return root, entry, calculate_button, result_label #For testing returning GUI features

#Leave commented for testing
#Uncomment to use GUI
#create_gui()[0].mainloop()
