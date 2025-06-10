import sys
import os
import json
import unittest
from unittest.mock import mock_open, patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 
                                                '../src')))

from tasker_x.task_manager import TaskManager

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

        self.assertEqual(len(test_result), 1)
        self.assertEqual(test_result[0]['description'], "Do some coding")
        self.assertEqual(test_result[0]['status'], "todo")

    def test_delete_task(self):
        """Tests if a task has been deleted successfully"""

        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [
            {
                'id': 1,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/25',
                'updatedAt': '10/06/25'
            },
            {
                'id': 2,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/25',
                'updatedAt': '10/06/25'
            }
        ]
        mocked_open = mock_open(read_data=json.dumps(test_data))

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.delete_task(2)
        
        self.assertEqual(len(test_result), 1)
    
    def test_update_task(self):
        """Tests if a task is updated correctly"""

        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [
            {
                'id': 1,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            }
        ]

        mocked_open = mock_open(read_data=json.dumps(test_data))

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.update_task(1, "Study")

        self.assertEqual(test_result[0]['description'], 'Study')
        self.assertNotEqual(test_result[0]['updatedAt'], test_data[0]['updatedAt'])

    def test_mark_task_done(self):
        """Tests if a task is marked as done"""

        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [
            {
                'id': 1,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            }
        ]

        mocked_open = mock_open(read_data=json.dumps(test_data))

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.mark_task_done(1)

        self.assertEqual(test_result[0]['status'], 'done')
        self.assertNotEqual(test_result[0]['updatedAt'], test_data[0]['updatedAt'])

    def test_mark_task_in_progress(self):
        """Tests if a task is marked as in-progress"""

        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [
            {
                'id': 1,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            }
        ]

        mocked_open = mock_open(read_data=json.dumps(test_data))

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.mark_task_in_progress(1)
        
        self.assertEqual(test_result[0]['status'], 'in-progress')
        self.assertNotEqual(test_result[0]['updatedAt'], test_data[0]['updatedAt'])
    
    def test_list_tasks(self):
        """Tests if tasks are listed correctly"""

        test_path = "test_task.json"
        test_task_manager = TaskManager(test_path)

        test_data = [
            {
                'id': 1,
                'description': 'Do some coding',
                'status': 'todo',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            },
            {
                'id': 2,
                'description': 'Do some coding',
                'status': 'done',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            },
            {
                'id': 3,
                'description': 'Do some coding',
                'status': 'in-progress',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            },
            {
                'id': 4,
                'description': 'Do some coding',
                'status': 'in-progress',
                'createdAt': '10/06/2025 18:19:42',
                'updatedAt': '10/06/2025 18:19:42'
            },
        ]

        mocked_open = mock_open(read_data=json.dumps(test_data))

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.list_tasks('done')

        self.assertEqual(len(test_result), 1)

        with patch("builtins.open", mocked_open):
            with patch("json.dump") as mock_json_dump:
                test_result = test_task_manager.list_tasks('in-progress')

        self.assertEqual(len(test_result), 2)