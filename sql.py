import sqlite3

# Connect to an existing database
connection = sqlite3.connect("myntra_dataset.db")

cursor = connection.cursor()

# Example: read all tables
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables in database:", tables)

# Example: read data from an existing table
data = cursor.execute("SELECT * FROM MYNTRA_DATA").fetchall()
for row in data:
    print(row)

connection.close()
