"""Write a Python program to connect to an SQLite3 database, create a table, insert data, and
fetch data."""


import sqlite3

conn = sqlite3.connect('example.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 35))

conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()


print("Users in the database:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()