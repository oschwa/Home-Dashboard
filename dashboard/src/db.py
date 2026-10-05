import sqlite3

# constants
DB_NAME = "home_dash.db"

# creating db
db_conn = sqlite3.connect(DB_NAME)

cursor = db_conn.cursor()

# tasks table
cursor.execute("" \
"CREATE TABLE IF NOT EXISTS task(title, date, description, status)")

