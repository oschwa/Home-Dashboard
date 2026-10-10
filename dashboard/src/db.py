import sqlite3

#   constants
DB_NAME = "home_dash.db"

#   creating db
db_conn = sqlite3.connect(DB_NAME)

cursor = db_conn.cursor()

#   tasks table
cursor.execute(
"CREATE TABLE IF NOT EXISTS task (" \
    "task_id TEXT PRIMARY KEY, " \
    "title TEXT NOT NULL, " \
    "date_assigned TEXT NOT NULL, " \
    "description TEXT NOT NULL, " \
    "status TEXT NOT NULL DEFAULT 'ready' " \
    "CHECK (status IN ('ready', 'in_progress', 'completed'))" \
    ");")

db_conn.close()
