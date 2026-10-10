import sqlite3


class DBConnection:
    DB_NAME = "home_dash.db"

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
        "Open the application file database."
        try:
            db_conn = sqlite3.connect(self.DB_NAME)
            return db_conn
        except sqlite3.DatabaseError as e:
            print(self.NO_OPEN_ERROR + e)
            return None

    def _close_db(self, db_conn):
        "Close a given database connection."
        try:
            db_conn.close()
        except sqlite3.DatabaseError as e:
            print(self.NO_CLOSE_ERROR + e)
            

    def make_task_table(self):
        "Update schema with Task table."
        db_conn = self._open_db()

        if (db_conn is None):
            return
        
        cursor = db_conn.cursor()

        try:
            cursor.execute(self.TASK_SETUP_QUERY)
        except sqlite3.DatabaseError as e:
            print(self.TASK_SETUP_ERROR  + e)

        self._close_db()




