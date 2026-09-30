import sqlite3

# constants
DB_NAME = "home_dash.db"

# creating db
db_conn = sqlite3.connect(DB_NAME)

# create tables
cur = db_conn.cursor()

cur = ("CREATE TABLE task(title, description, date)")



