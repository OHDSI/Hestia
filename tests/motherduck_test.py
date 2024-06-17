import os

import duckdb

# Load the MotherDuck token from environment variables
motherduck_token = os.getenv('MOTHERDUCK_TOKEN')
if not motherduck_token:
    raise ValueError("MOTHERDUCK_TOKEN is not set in the environment variables.")

# Create a connection to MotherDuck
conn = duckdb.connect(database=':memory:', access_mode='read_write', config={"access_token": motherduck_token})

# Create a test table
conn.execute("CREATE TABLE test_table (id INTEGER, name VARCHAR)")

# Insert data into the table
conn.execute("INSERT INTO test_table VALUES (1, 'Alice'), (2, 'Bob')")

# Query the table
result = conn.execute("SELECT * FROM test_table").fetchall()

# Check the results
if result == [(1, 'Alice'), (2, 'Bob')]:
    print("Test Passed: Data matches expected results")
else:
    raise Exception("Test Failed: Data does not match expected results")
