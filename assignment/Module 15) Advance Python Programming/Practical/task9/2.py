""" Write a Python program to insert data into an SQLite3 database and fetch it."""





import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", 
               ("John Doe", "Software Engineer", 75000.00))
cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", 
               ("Jane Smith", "Data Analyst", 65000.00))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("Employees:")
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")

conn.close()