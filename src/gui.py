import tkinter as tk
from tkinter import messagebox, ttk
from change_count_machine import compute_change
from db_utils import check_and_create_db, insert_calculation, get_all_calculations, clear_calculations

def create_gui():
    # Establish the database connection
    conn, cursor = check_and_create_db()
    def on_calculate():
        try:
            user_input = entry.get()

            # Check for valid input
            if '.' in user_input and len(user_input.split('.')[-1]) > 2:
                messagebox.showerror("Error", "Please enter a number with no more than two decimal places.")
                return

            money = float(user_input)

            if money < 0:
                messagebox.showerror("Error", "Amount cannot be negative.")
                return

            # Compute the change and get results
            total_items, denom_counts = compute_change(money)
            result_text = f"Total items: {total_items}\nDenomination breakdown:\n"
            for denom, count in denom_counts.items():
                result_text += f"${denom:.2f}: {count}\n"
            result_label.config(text=result_text)

            # Insert the calculation into the database
            
            insert_calculation(conn, cursor, money, total_items, denom_counts)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    def on_view_calculations():
        # Retrieve past calculations
        calculations = get_all_calculations(cursor)
        if not calculations:
            messagebox.showinfo("Info", "No calculations found.")
            return

        # Display past calculations in a new window
        history_window = tk.Toplevel(root)
        history_window.title("Calculation History")
        history_window.configure(bg="#2E2E2E")

        # Create a table to display calculations
        columns = ("ID", "Amount", "Total Items", "Denominations", "Timestamp")
        tree = ttk.Treeview(history_window, columns=columns, show="headings", height=10)
        tree.heading("ID", text="ID")
        tree.heading("Amount", text="Amount")
        tree.heading("Total Items", text="Total Items")
        tree.heading("Denominations", text="Denominations")
        tree.heading("Timestamp", text="Timestamp")

        for calc in calculations:
            tree.insert("", "end", values=calc)

        tree.pack(fill="both", expand=True)

    def on_clear_calculations():
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all calculations?"):
            clear_calculations(conn, cursor)
            messagebox.showinfo("Info", "All calculations cleared.")

    root = tk.Tk()
    root.title("Change Count Machine")

    # Set a custom theme
    root.configure(bg='#2E2E2E')
    root.option_add("*Font", "Arial 12")
    root.option_add("*Foreground", "white")
    root.option_add("*Background", "#3A3A3A")

    # Create input frame
    entry_frame = tk.Frame(root, bg="#2E2E2E")
    dollar_sign_label = tk.Label(entry_frame, text="$", fg="lightgreen", bg="#2E2E2E", font=("Arial", 12))
    entry = tk.Entry(entry_frame, font=("Arial", 12), fg="black", bg="white", bd=2, relief="solid")
    dollar_sign_label.pack(side="left", padx=5)
    entry.pack(side="left", padx=5)

    # Buttons and labels
    calculate_button = tk.Button(root, text="Calculate", command=on_calculate, font=("Arial", 12),
                                  fg="white", bg="#4CAF50", relief="flat", padx=10, pady=5)
    view_button = tk.Button(root, text="View History", command=on_view_calculations, font=("Arial", 12),
                             fg="white", bg="#2196F3", relief="flat", padx=10, pady=5)
    clear_button = tk.Button(root, text="Clear History", command=on_clear_calculations, font=("Arial", 12),
                              fg="white", bg="#F44336", relief="flat", padx=10, pady=5)
    result_label = tk.Label(root, text="", bg="#2E2E2E", fg="lightblue", font=("Arial", 12))

    # Pack widgets
    entry_frame.pack(pady=10)
    calculate_button.pack(pady=5)
    view_button.pack(pady=5)
    clear_button.pack(pady=5)
    result_label.pack(pady=10)

    return root, entry, calculate_button, result_label

# Uncomment to run the GUI
create_gui()[0].mainloop()
