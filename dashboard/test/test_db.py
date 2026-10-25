import pytest
import sqlite3
from src.db import DBConnection
from src.db import DatabaseConnectError
from unittest.mock import patch

def is_open(conn) -> bool:
    "test helper method for determining if a connection is open."
    try:
        conn.execute("SELECT 1")
        return True
    except sqlite3.ProgrammingError:
        return False

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

    def test_db_open_successful(self, monkeypatch):
        monkeypatch.setattr(DBConnection, "DB_NAME", ":memory:")
        test_db_conn = DBConnection()
        connection = test_db_conn._open_db()
        assert connection is not None
        assert is_open(connection)
        connection.close()

    @patch("src.db.sqlite3.connect",
       side_effect=sqlite3.DatabaseError())
    def test_successfully_catches_db_open_exception(self, mock_connect):
        test_db_conn = DBConnection()
        with pytest.raises(DatabaseConnectError):
            connection = test_db_conn._open_db()
        mock_connect.assert_called_once()

    



    
