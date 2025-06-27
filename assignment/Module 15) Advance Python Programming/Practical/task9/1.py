"""Write a Python program to create a database and a table using SQLite3."""

import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

print("Database and table created successfully.")

conn.commit()
conn.close()


print()
print("next ..")
print()


