from change_count_machine import compute_change
import tkinter as tk
from tkinter import messagebox

def create_gui():

    def on_calculate():
        try:
            money = float(entry.get())
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
    entry = tk.Entry(root) #Text entry
    calculate_button = tk.Button(root, text="Calculate", command=on_calculate)
    result_label = tk.Label(root, text="")

    entry.pack()
    calculate_button.pack()
    result_label.pack()

    return root, entry, calculate_button, result_label #For testing returning GUI features

#Leave commented for testing
#create_gui()[0].compute_changeloop() #Uncomment to use GUI
