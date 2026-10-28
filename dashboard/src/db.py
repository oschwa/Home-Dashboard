import sqlite3
from sqlite3 import DatabaseError

class DatabaseConnectError(DatabaseError):
    "Exception for failing to open or close the database."

DB_NAME = "home_dash.db"

# Database-related exception messages
NO_OPEN_ERROR = "ERROR - Could not open dashboard database.\n"
NO_CLOSE_ERROR = "ERROR - Dashboard database could not safely close.\n"
TASK_SETUP_ERROR = "ERROR - Could not create Task Schema.\n"

TASK_SETUP_QUERY = "CREATE TABLE IF NOT EXISTS task (" \
        "task_id TEXT PRIMARY KEY, " \
        "title TEXT NOT NULL, " \
        "date_assigned TEXT NOT NULL, " \
        "description TEXT NOT NULL, " \
        "status TEXT NOT NULL DEFAULT 'ready' " \
        "CHECK (status IN ('ready', 'in_progress', 'completed'))" \
        ");"

def open_db():
    try:
        "Open the application file database."
        db_conn = sqlite3.connect(DB_NAME)
        return db_conn
    except DatabaseError as e:
        raise DatabaseConnectError(NO_OPEN_ERROR) from e

def close_db(db_conn):
    "Close a given database connection."
    try:
        db_conn.close()
    except DatabaseError as e:
        raise DatabaseConnectError(NO_CLOSE_ERROR) from e
    
def make_task_table():
    "Update schema with Task table."
    try:
        db_conn = open_db()
    except DatabaseConnectError as e:
        return e
    
    cursor = db_conn.cursor()

    try:
        cursor.execute(TASK_SETUP_QUERY)
    except sqlite3.DatabaseError as e:
        print(TASK_SETUP_ERROR)

    try: 
        close_db()
    except DatabaseConnectError as e:
        return e




