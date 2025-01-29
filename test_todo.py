import unittest
from unittest.mock import MagicMock, patch
from todo import add_todo, view_todo, delete_todo

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        # Create mock database connection and cursor
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor

    @patch('todo.db')
    def test_add_todo(self, mock_db):
        # Set up the mock
        mock_db.cursor.return_value = self.mock_cursor
        
        # Test adding a todo
        add_todo("Test Task", "Test Description")
        
        # Verify the cursor executed with correct SQL and values
        self.mock_cursor.execute.assert_called_with(
            "INSERT INTO tasks (task_name, description) VALUES (%s, %s)",
            ("Test Task", "Test Description")
        )
        mock_db.commit.assert_called_once()

    @patch('todo.db')
    def test_view_todo(self, mock_db):
        # Set up the mock
        mock_db.cursor.return_value = self.mock_cursor
        self.mock_cursor.fetchall.return_value = [
            (1, "Test Task", "Test Description", 0)
        ]
        
        # Test viewing todos
        view_todo()
        
        # Verify the cursor executed the correct SQL
        self.mock_cursor.execute.assert_called_with("SELECT * FROM tasks")

    @patch('todo.db')
    def test_delete_todo(self, mock_db):
        # Set up the mock
        mock_db.cursor.return_value = self.mock_cursor
        
        # Test deleting a todo
        delete_todo(1)
        
        # Verify the cursor executed with correct SQL and values
        self.mock_cursor.execute.assert_called_with(
            "DELETE FROM tasks WHERE id = %s",
            (1,)
        )
        mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()



