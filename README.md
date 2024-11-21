# Change Count Machine

## Description
The Change Count Machine is a Python application that calculates the optimal denomination breakdown for a given monetary amount. It includes a GUI built using Tkinter for user interaction.

## Features
- Calculates the minimum number of denominations for any given amount.
- Displays a detailed breakdown of the denominations used.
- Saves results to SQL database that can be viewed later.
- Ability to clear database of previously saved calculations.
- User-friendly interface for entering the amount and viewing results.

## Files
### 1. `change_count_machine.py`
- **Purpose**: Contains the core functionality for calculating the denomination breakdown.
- **Key Functions**:
  - `denominations_calc(money_left, dom)': Determines how many of a specific denomination can be used for the given amount.
  - `compute_loop(money_left,denom_list,denom_counts,total_items)': Iteratively calculates the optimal denomination breakdown for the input amount.
  - `compute_change(money)': Holds the list of denominations, call "compute_loop" to preform it's loop, and returns results to the requester.

### 2. `gui.py`
- **Purpose**: Provides a graphical user interface for interacting with the Change Count Machine.
- **Features**:
  - Entry field for inputting the amount.
  - Button to trigger the calculation.
  - Button to trigger the display for previous results.
  - Button to trigger clearing of SQL database.
  - Display area for showing the results.
 
### 3. 'db_utils.py'
- **Purpose**: Contains the functionality for the SQL database
- **Features**:
  -  `create_db(cursor)': Creates the SQL table.
  -  `check_and_create_db()': Checks if the SQL database already exists and if not call "create_db".
  -  `insert_calculation(conn, cursor, amount, total_items, denom_counts)': Inserts a calculation from "change_count_machine.py" into the SQL database.
  -  `def get_all_calculations(cursor)': Gathers all of the calculations in the SQL database and returns them.
  -  `def clear_calculations(conn, cursor)': Clears the SQL database of previously saved calculations.

## Requirements
- Python 3.x
- Tkinter (included in most Python installations)
- SQLite

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
4. Click "View History" to view saved calculations.
5. Click "Clear" to clear saved calculations (will need to confirm your choice).

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
- To run tests either use "pytest" for all tests or "pytest _test_file_name_".
- To run tests either be in the "root" directory or "tests" directory (tests will not run as stated inside the "src" directory).

## Testing Notes
- Comment 'create_gui()[0].mainloop()' when running all tests or tests with 'test_gui.py'.
  

