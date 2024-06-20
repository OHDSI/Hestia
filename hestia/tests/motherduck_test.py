import os

import duckdb

# Load the MotherDuck token from environment variables
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')
if not motherduck_token:
    raise ValueError("MOTHERDUCK_TOKEN is not set in the environment variables.")

# Create a connection to MotherDuck
conn = duckdb.connect
conn = duckdb.connect(f'md:?motherduck_token={motherduck_token}')

# Create a test table
conn.execute("""
    USE test;
    DROP TABLE IF EXISTS test_table;
    CREATE TABLE test_table (id INTEGER, name VARCHAR);
    INSERT INTO test_table VALUES (1, 'Alice'), (2, 'Bob');
             """)

# Query the table
result = conn.execute("SELECT * FROM test_table").fetchall()

# Check the results
if result == [(1, 'Alice'), (2, 'Bob')]:
    print("Test Passed: Data matches expected results")
else:
    raise Exception("Test Failed: Data does not match expected results")
