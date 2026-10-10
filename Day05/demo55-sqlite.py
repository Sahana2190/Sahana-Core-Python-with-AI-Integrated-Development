import sqlite3

# Connect to your database (creates prod.db if it doesn't exist)
conn = sqlite3.connect(r"C:\Users\SAHANA\OneDrive\Desktop\Training\Day5\prod.db")
sth = conn.cursor()

# Create the table if it doesn't exist
sth.execute("""
CREATE TABLE IF NOT EXISTS prod (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
)
""")

# Insert some sample rows
sth.execute("INSERT INTO prod (name, price) VALUES ('Laptop', 75000)")
sth.execute("INSERT INTO prod (name, price) VALUES ('Mouse', 500)")
sth.execute("INSERT INTO prod (name, price) VALUES ('Keyboard', 1500)")

# Save changes
conn.commit()

# Query the table
sth.execute("SELECT * FROM prod")
for row in sth.fetchall():
    print(row)

conn.close()
