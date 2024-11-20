import pytest
import sqlite3
from src.db_utils import create_db, check_and_create_db, insert_calculation, get_all_calculations, clear_calculations

# Setup and teardown for testing the database
@pytest.fixture(scope="module")
def setup_db():
    # Create an in-memory database for testing
    conn = sqlite3.connect(":memory:")  # In-memory database for tests
    cursor = conn.cursor()

    # Create the table
    create_db(cursor)

    yield cursor, conn  # Provide cursor and connection to tests

    # Teardown: Close the connection after tests are done
    conn.close()

# Test create_table function
def test_create_table(setup_db):
    cursor, conn = setup_db
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='calculations';")
    table_exists = cursor.fetchone()
    assert table_exists is not None  # Table should exist

# Test insert_calculation function
def test_insert_calculation(setup_db):
    cursor, conn = setup_db
    denom_counts = {5: 1, 1: 1, 0.25: 2, 0.05: 1}  # Correctly passing denom_counts as a dictionary
    insert_calculation(cursor, 6.55, 5, denom_counts)  # 6.55 is the amount, 5 is total_items
    conn.commit()

    # Verify insertion
    cursor.execute("SELECT * FROM calculations WHERE amount = 6.55;")
    result = cursor.fetchone()
    assert result is not None  # Should return a row
    assert result[1] == 6.55  # Ensure the amount matches
    assert result[2] == 5   #Ensure the total items matches
    assert result[3] == "{5: 1, 1: 1, 0.25: 2, 0.05: 1}"  # Ensure the breakdown matches

# Test get_calculations function
def test_get_calculations(setup_db):
    cursor, conn = setup_db
    clear_calculations(cursor)
    insert_calculation(cursor, 1, 1, "{1: 1}")
    insert_calculation(cursor, 10.00, 1, "{10: 1}")

    calculations = get_all_calculations(cursor)
    assert len(calculations) == 2  # We inserted two records
    assert calculations[0][1] == 1  # First record's total
    assert calculations[1][1] == 10.00  # Second record's total

# Test clear_calculations function
def test_clear_calculations(setup_db):
    cursor, conn = setup_db
    insert_calculation(cursor, 1, 1, "{1: 1}")
    insert_calculation(cursor, 10.00, 1, "{10: 1}")

    # Clear the table
    clear_calculations(cursor)

    # Verify the table is cleared
    cursor.execute("SELECT * FROM calculations;")
    results = cursor.fetchall()
    assert len(results) == 0  # Table should be empty
