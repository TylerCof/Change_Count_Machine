import pytest
import sqlite3
from src.db_utils import create_table, insert_calculation, get_calculations, clear_calculations

# Setup and teardown for testing the database
@pytest.fixture(scope="module")
def setup_db():
    # Create an in-memory database for testing
    conn = sqlite3.connect(":memory:")  # In-memory database for tests
    cursor = conn.cursor()

    # Create the table
    create_table(cursor)

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
    insert_calculation(cursor, 6.55, "{5: 1, 1: 1, 0.25: 2, 0.05: 1}")  # Example calculation

    # Verify insertion
    cursor.execute("SELECT * FROM calculations WHERE total = 6.55;")
    result = cursor.fetchone()
    assert result is not None  # Should return a row
    assert result[1] == 6.55  # Ensure the total matches
    assert result[2] == "{5: 1, 1: 1, 0.25: 2, 0.05: 1}"  # Ensure the breakdown matches

# Test get_calculations function
def test_get_calculations(setup_db):
    cursor, conn = setup_db
    insert_calculation(cursor, 6.55, "{5: 1, 1: 1, 0.25: 2, 0.05: 1}")
    insert_calculation(cursor, 10.00, "{10: 1}")

    calculations = get_calculations(cursor)
    assert len(calculations) == 2  # We inserted two records
    assert calculations[0][1] == 6.55  # First record's total
    assert calculations[1][1] == 10.00  # Second record's total

# Test clear_calculations function
def test_clear_calculations(setup_db):
    cursor, conn = setup_db
    insert_calculation(cursor, 6.55, "{5: 1, 1: 1, 0.25: 2, 0.05: 1}")
    insert_calculation(cursor, 10.00, "{10: 1}")

    # Clear the table
    clear_calculations(cursor)

    # Verify the table is cleared
    cursor.execute("SELECT * FROM calculations;")
    results = cursor.fetchall()
    assert len(results) == 0  # Table should be empty
