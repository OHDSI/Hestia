import os

import duckdb

# Load the MotherDuck token from environment variables
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')
if not motherduck_token:
    raise ValueError("MOTHERDUCK_TOKEN is not set in the environment variables.")

# Create a connection to MotherDuck
conn = duckdb.connect
conn = duckdb.connect(f'md:test_db?motherduck_token={motherduck_token}')

# Create a test table
conn.execute("""
    DROP TABLE IF EXISTS test_tbl;
    CREATE TABLE test_tbl (id INTEGER, test_title VARCHAR, test_description VARCHAR);
    INSERT INTO test_tbl VALUES (1, 'Insert Test', 'Test inserting data into a table');
             """)

# Query the table
result = conn.execute("SELECT * FROM test_tbl").fetchall()

# Check the results
if result == [(1, 'Insert Test', 'Test inserting data into a table')]:
    print("Test Passed: Data matches expected results")
else:
    raise Exception("Test Failed: Data does not match expected results")
