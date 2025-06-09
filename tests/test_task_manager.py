import sys
import os
import json
import unittest
from unittest.mock import mock_open, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                '../src')))

from src.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    """Test cases for Task Manager"""

    def test_add_task(self):
        """Tests if a task has been added correctly"""
        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [] # Empty list, like the initial file creation
        mocked_open = mock_open(read_data=json.dumps(test_data)) 

        with patch("builtins.open", mocked_open): # open() faked using mocked
            with patch("json.dump") as mock_json_dump: # prevents actual writing
                test_result = test_task_manager.add_task("Do some coding")

        print(test_result)
        self.assertEqual(len(test_result), 1)
        self.assertEqual(test_result[0]['description'], "Do some coding")
        self.assertEqual(test_result[0]['status'], "todo")
