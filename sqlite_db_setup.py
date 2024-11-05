import sqlite3

# Connect to the chocolate_house.db database (or create it if it doesn't exist)
conn = sqlite3.connect('chocolate_house.db')
print("Opened database successfully")

# Create the flavors table
conn.execute('''
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    description TEXT
)
''')
print("Table 'flavors' created successfully")

# Create the ingredients table
conn.execute('''
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL,
    quantity INTEGER
)
''')
print("Table 'ingredients' created successfully")

# Create the suggestions table
conn.execute('''
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    suggestion TEXT,
    allergy_concern TEXT
)
''')
print("Table 'suggestions' created successfully")

# Close the database connection
conn.close()
print("Database setup completed successfully")
