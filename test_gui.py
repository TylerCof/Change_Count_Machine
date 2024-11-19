import pytest
from change_count_machine import compute_change
from gui import create_gui
from unittest.mock import patch
import tkinter as tk

@pytest.fixture
def gui_app():
    """Fixture to set up and tear down the Tkinter app."""
    from gui import create_gui
    root, entry, calculate_button, result_label = create_gui()
    yield root, entry, calculate_button, result_label
    root.destroy()

def test_tkinter_gui(gui_app): #Test for basic functionality of the GUI
    root, entry, calculate_button, result_label = gui_app

    # Simulate user input
    entry.insert(0, "103.17")

    # Mock the `compute_change` function to isolate GUI behavior
    with patch('change_count_machine.compute_change', return_value=(8, {100: 1, 1: 3, 0.1: 1, 0.05: 1, 0.01: 2})):
        # Simulate button click
        calculate_button.invoke()

        # Check if the label was updated with the correct result
        assert "Total items: 8" in result_label.cget("text")
        assert "$100.00: 1" in result_label.cget("text")
        assert "$0.01: 2" in result_label.cget("text")

    # Test invalid input
    entry.delete(0, tk.END)
    entry.insert(0, "-1")
    with patch('tkinter.messagebox.showerror') as mock_error:
        calculate_button.invoke()
        mock_error.assert_called_once_with("Error", "Amount cannot be negative.")

    # Test invalid input
    entry.delete(0, tk.END)
    entry.insert(0,"103.171")
    with patch('tkinter.messagebox.showerror') as mock_error:
        calculate_button.invoke()
        mock_error.assert_called_once_with("Error", "Please enter a number with no more than two decimal places.")

    # Test invalid input
    entry.delete(0, tk.END)
    entry.insert(0,"abcd")
    with patch('tkinter.messagebox.showerror') as mock_error:
        calculate_button.invoke()
        mock_error.assert_called_once_with("Error", "Invalid input. Please enter a numeric value.")

    root.quit()  # Close the window after test

    

