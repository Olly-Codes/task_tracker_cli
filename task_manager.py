import json
from datetime import date
from pathlib import Path

from task import Task

class TaskManager():
    """TaskManager manages all the logic of tasks"""
    path = Path('tasks.json')

    def path_exists(self):
        """Check if file exists"""
        if not self.path.exists():
            with open(self.path, 'w') as f:
                json.dump([], f)
    
    def add_task(self, description):
        """Adds a task to the json file"""
        self.path_exists()

        with open(self.path, 'r') as f:
            tasks = json.load(f)
            current_date = date.today().strftime("%d/%m/%Y")

        id = max({task['id'] for task in tasks}, default=0) + 1
        createdAt = current_date
        updatedAt = current_date

        new_task = Task(id, description, createdAt, updatedAt, status='todo')
        task = {
            'id': new_task.id,
            'description': new_task.description,
            'status': new_task.status,
            'createdAt': new_task.createdAt,
            'updatedAt': new_task.updatedAt
        }

        tasks.append(task)
        with open(self.path, encoding='utf-8', mode='w') as f:
            json.dump(tasks, f, indent=2)
        
        return f"Task added successfully (ID: {id})"