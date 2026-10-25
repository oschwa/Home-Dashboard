import sqlite3
from sqlite3 import DatabaseError

class DatabaseConnectError:
    "Exception for failing to open or close the database."

class DBConnection:
    DB_NAME = "home_dash.db"

    # Database-related exceptions
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

    def _open_db(self):
        try:
            "Open the application file database."
            db_conn = sqlite3.connect(self.DB_NAME)
            return db_conn
        except DatabaseError as e:
            raise DatabaseConnectError(self.NO_OPEN_ERROR) from e

    def _close_db(self, db_conn):
        "Close a given database connection."
        try:
            db_conn.close()
        except DatabaseError as e:
            raise DatabaseConnectError(self.NO_CLOSE_ERROR) from e
            
    def make_task_table(self):
        "Update schema with Task table."
        try:
            db_conn = self._open_db()
        except DatabaseConnectError as e:
            return e
        
        cursor = db_conn.cursor()

        try:
            cursor.execute(self.TASK_SETUP_QUERY)
        except sqlite3.DatabaseError as e:
            print(self.TASK_SETUP_ERROR)

        try: 
            self._close_db()
        except DatabaseConnectError as e:
            return e




