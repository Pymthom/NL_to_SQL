import sqlite3
import pandas as pd

# Load the CSV file
csv_path = "myntra_dataset_ByScraping.csv"
df = pd.read_csv(csv_path)

# Create SQLite database file
db_path = "myntra_dataset.db"
connection = sqlite3.connect(db_path)

# Write the dataframe to SQLite database
df.to_sql("MYNTRA_DATA", connection, if_exists="replace", index=False)

connection.close()

db_path
