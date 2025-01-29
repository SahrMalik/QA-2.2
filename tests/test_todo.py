import unittest
import mysql.connector
from todo import add_todo, view_todo, todo_completed, update_todo, delete_todo

class TestTodoApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a test database connection
        cls.db = mysql.connector.connect(
            host='localhost',
            user='sahr',
            password='root',
            database='test_todo_list'
        )
        cls.cursor = cls.db.cursor()
        cls.cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), description TEXT, is_completed BOOLEAN)")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test database
        cls.cursor.execute("DROP TABLE IF EXISTS tasks")
        cls.db.close()

    def setUp(self):
        # Clear the tasks table before each test
        self.cursor.execute("DELETE FROM tasks")
        self.db.commit()

    def test_add_todo(self):
        add_todo("Test Task", "Test Description")
        self.cursor.execute("SELECT * FROM tasks")
        tasks = self.cursor.fetchall()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test Task")
        self.assertEqual(tasks[0][2], "Test Description")

    def test_view_todo(self):
        add_todo("Test Task", "Test Description")
        tasks = view_todo()
        self.assertIsNotNone(tasks)

    def test_todo_completed(self):
        add_todo("Test Task", "Test Description")
        self.cursor.execute("SELECT id FROM tasks")
        task_id = self.cursor.fetchone()[0]
        todo_completed(task_id)
        self.cursor.execute("SELECT is_completed FROM tasks WHERE id = %s", (task_id,))
        is_completed = self.cursor.fetchone()[0]
        self.assertTrue(is_completed)

    def test_update_todo(self):
        add_todo("Test Task", "Test Description")
        self.cursor.execute("SELECT id FROM tasks")
        task_id = self.cursor.fetchone()[0]
        update_todo(task_id, "Updated Task", "Updated Description")
        self.cursor.execute("SELECT task_name, description FROM tasks WHERE id = %s", (task_id,))
        task = self.cursor.fetchone()
        self.assertEqual(task[0], "Updated Task")
        self.assertEqual(task[1], "Updated Description")

    def test_delete_todo(self):
        add_todo("Test Task", "Test Description")
        self.cursor.execute("SELECT id FROM tasks")
        task_id = self.cursor.fetchone()[0]
        delete_todo(task_id)
        self.cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
        task = self.cursor.fetchone()
        self.assertIsNone(task)

if __name__ == '__main__':
    unittest.main()