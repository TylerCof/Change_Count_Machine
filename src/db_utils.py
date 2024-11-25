import sqlite3
import os

def create_db(cursor):
    """Create the database and calculations table if they do not exist."""

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculations_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            total_items INTEGER,
            denom_counts TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')


def check_and_create_db():
    """Check if the database exists, and if not, create it."""
    db_path = 'calculations_history.db'
    
    # Check if the database file exists and create the table if it doesn't
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)  # Establish connection to the database
        cursor = conn.cursor()  # Get the cursor for executing SQL commands
        create_db(cursor)  # Pass the cursor to create the table if needed
    
    else:
        conn = sqlite3.connect(db_path)  # Establish connection to the database
        cursor = conn.cursor()  # Get the cursor for executing SQL commands
    # Commit changes and return the connection and cursor for further use
    conn.commit()
    return conn, cursor

def insert_calculation(conn, cursor, amount, total_items, denom_counts):
    """Insert a new calculation into the database."""
    cursor.execute('''
        INSERT INTO calculations_history (amount, total_items, denom_counts)
        VALUES (?, ?, ?)
    ''', (amount, total_items, str(denom_counts)))  # Store denom_counts as a string
    conn.commit()
    

def get_all_calculations(cursor):
    """Retrieve all past calculations from the database."""

    cursor.execute('SELECT * FROM calculations_history ORDER BY timestamp DESC')
    rows = cursor.fetchall()

    return rows

def clear_calculations(conn, cursor):
    """Clear all past calculations from the database."""

    cursor.execute('DELETE FROM calculations_history')
    conn.commit()
