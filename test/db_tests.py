import pytest
import sqlite3

class TestTasks:

    TASK_SETUP_QUERY = "CREATE TABLE IF NOT EXISTS task (" \
        "task_id TEXT PRIMARY KEY, " \
        "title TEXT NOT NULL, " \
        "date_assigned TEXT NOT NULL, " \
        "description TEXT NOT NULL, " \
        "status TEXT NOT NULL DEFAULT 'ready' " \
        "CHECK (status IN ('ready', 'in_progress', 'completed'))" \
        ");"

    @pytest.fixture
    def test_conn(self):
        "setup test connection and tear down after test."
        connection = sqlite3.connect(":memory:")
        cursor = connection.cursor()
        cursor.execute(self.TASK_SETUP_QUERY)
        yield connection
        connection.close()

    def test_db_task_table_creation(self, test_conn):
        pass


    
