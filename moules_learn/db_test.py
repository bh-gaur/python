import sqlite3

# 1. Connect to SQLite database (creates test.db if it doesn't exist)
conn = sqlite3.connect('test.db')

# Optional: Access columns by name like dictionary keys (e.g., row['name'])
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# ==============================================================================
# 2. CREATE TABLE
# ==============================================================================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

# ==============================================================================
# 3. INSERT QUERIES
# ==============================================================================
# A. Single Insert with Parameterized Query (prevents SQL injection)
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

# B. Insert Multiple Rows at Once (executemany)
multiple_users = [
    ("Bob", 30),
    ("Charlie", 35),
    ("Diana", 22)
]
cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", multiple_users)

# Commit transactions to save changes
conn.commit()
print("✅ Inserted sample records.\n")


# ==============================================================================
# 4. SELECT / READ QUERIES
# ==============================================================================

# A. Fetch ALL rows (fetchall)
print("--- 1. Fetch All Users ---")
cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
for row in all_rows:
    print(f"ID: {row['id']}, Name: {row['name']}, Age: {row['age']}")

# B. Fetch ONE row (fetchone)
print("\n--- 2. Fetch Single User ---")
cursor.execute("SELECT * FROM users WHERE name = ?", ("Alice",))
single_row = cursor.fetchone()
if single_row:
    print(f"Found: {single_row['name']} (Age: {single_row['age']})")

# C. Filter with WHERE clause
print("\n--- 3. Users Older Than 24 ---")
cursor.execute("SELECT name, age FROM users WHERE age > ? ORDER BY age DESC", (24,))
for row in cursor.fetchall():
    print(f"{row['name']} -> {row['age']} years old")


# ==============================================================================
# 5. UPDATE QUERY
# ==============================================================================
print("\n--- 4. Update User Age ---")
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
conn.commit()
print(f"Rows updated: {cursor.rowcount}")


# ==============================================================================
# 6. DELETE QUERY
# ==============================================================================
print("\n--- 5. Delete User ---")
cursor.execute("DELETE FROM users WHERE name = ?", ("Diana",))
conn.commit()
print(f"Rows deleted: {cursor.rowcount}")


# ==============================================================================
# 7. Close Connection
# ==============================================================================
conn.close()
print("\n✅ Database connection closed.")