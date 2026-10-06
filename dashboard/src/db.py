import sqlite3

DB_NAME = "home_dash.db"

#   tasks table query
CREATE_QUERY = \
    "CREATE TABLE IF NOT EXISTS task (" \
    "task_id TEXT PRIMARY KEY, " \
    "title TEXT NOT NULL, " \
    "date_created TEXT NOT NULL, " \
    "date_completed TEXT," \
    "description TEXT NOT NULL, " \
    "status TEXT NOT NULL DEFAULT 'ready' " \
    "CHECK (status IN ('ready', 'in_progress', 'completed'))" \
    ");"

def create_db(self):
    """
    Create application-file-format database according 
    to predefined constants.
    """
    db_conn = sqlite3.connect(DB_NAME)
    cursor = db_conn.cursor()
    cursor.execute(CREATE_QUERY)

