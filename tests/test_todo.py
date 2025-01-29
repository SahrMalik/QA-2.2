import unittest
from todo import add_todo, view_todo

class TestTodoBasic(unittest.TestCase):
    def test_basic_functionality(self):
        # Test adding a task (just check no errors)
        try:
            add_todo("Test Task", "Test Description")
        except Exception as e:
            self.fail(f"Add todo failed: {e}")

        # Test viewing tasks (just check no errors)
        try:
            view_todo()
        except Exception as e:
            self.fail(f"View todo failed: {e}")

if __name__ == '__main__':
    unittest.main()