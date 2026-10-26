import pytest
import sqlite3
from src.db import open_db, close_db
from src.db import DatabaseConnectError
from unittest.mock import patch, MagicMock

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

    @patch("src.db.sqlite3.connect")
    def test_db_open_successful(self, mock_connect):
        test_connection = open_db()
        assert test_connection is not None
        mock_connect.assert_called_once()

    @patch("src.db.sqlite3.connect",
       side_effect=sqlite3.DatabaseError())
    def test_successfully_catches_db_open_exception(self, mock_connect):
        test_connection = None
        with pytest.raises(DatabaseConnectError):
            test_connection = open_db()
        assert test_connection is None
        mock_connect.assert_called_once()

    @patch("src.db.sqlite3.connect")
    def test_successfully_catches_db_close_exception(self, mock_connect):
        mock_connection_result = MagicMock()
        mock_connection_result.close.side_effect = sqlite3.DatabaseError()
        mock_connect.return_value = mock_connection_result

        test_connection = open_db()

        with pytest.raises(DatabaseConnectError):
            close_db(test_connection)

        mock_connect.assert_called_once()
    
    



    
