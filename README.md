# Change Count Machine

## Description
The Change Count Machine is a Python application that calculates the optimal denomination breakdown for a given monetary amount. It includes a GUI built using Tkinter for user interaction.

## Features
- Calculates the minimum number of denominations for any given amount.
- Displays a detailed breakdown of the denominations used.
- User-friendly interface for entering the amount and viewing results.

## Files
### 1. `change_count_machine.py`
- **Purpose**: Contains the core functionality for calculating the denomination breakdown.
- **Key Functions**:
  - `denominations_calc(money_left, dom)': Determines how many of a specific denomination can be used for the given amount.
  - `calculate_denominations(money)': Iteratively calculates the optimal denomination breakdown for the input amount.

### 2. `gui.py`
- **Purpose**: Provides a graphical user interface for interacting with the Change Count Machine.
- **Features**:
  - Entry field for inputting the amount.
  - Button to trigger the calculation.
  - Display area for showing the results.

## Requirements
- Python 3.x
- Tkinter (included in most Python installations)

## Installation
1. Clone or download the repository.
2. Ensure you have Python installed on your system.
3. No additional libraries are required.

## Usage
1. **Run the GUI**:
   - Make sure that the last line in `gui.py' is uncommented:
     ```python
     create_gui()[0].mainloop()
     ```
   - Execute the script:
     ```bash
     python gui.py
     ```
2. Enter the desired monetary amount in the input field.
3. Click "Calculate" to view the denomination breakdown.

## Example
### Input
- Amount: '123.45'
  
### Output
- Total items: 9
- Denomination breakdown: $100.00: 1, $20.00: 1, $1.00: 3, $0.25: 1, $0.10: 2

## Notes
- The denomination list can be adjusted in 'change_count_machine.py' to include additional values, e.g., '$2' or '$0.50`.
- Input validation ensures that only positive numeric values are accepted.

## Testing
- The GUI components ( 'root', 'entry', 'calculate_button', 'result_label') are returned for unit testing in 'create_gui()'.
- Comment 'create_gui()[0].mainloop()' for testing use.

