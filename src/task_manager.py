import json
from datetime import date
from pathlib import Path

from task import Task

class TaskManager():
    """TaskManager manages all the logic of tasks"""

    def __init__(self, filepath = "tasks.json"):
        self.filepath = filepath
        self.path = Path(self.filepath)

    def path_exists(self):
        """Check if file exists"""
        if not self.path.exists():
            with open(self.path, 'w') as f:
                json.dump([], f)
            return True
    
    def add_task(self, description):
        """Adds a task to the json file"""

        try:
            if self.path_exists:

                with open(self.path, encoding='utf-8', mode='r') as f:
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
            
                print(f"Task added successfully (ID: {id})")
            
                return tasks
        except:
            print("Something went wrong")
    
    def delete_task(self, id):
        """Deletes a task from json file"""

        try:
            with open('tasks.json', encoding='utf-8', mode='r') as f:
                tasks = json.load(f)
            
            if len(tasks) == 0:
                print("You haven't created any tasks yet to delete")
                return
            
            for i, task in enumerate(tasks):
                if task.get('id') == id:
                    del_task = tasks.pop(i)
                    break
            
            with open('tasks.json', encoding='utf-8', mode='w') as f:
                json.dump(tasks, f, indent=2)
            
            print(f"Task has been deleted (ID: {del_task['id']})")

            return del_task
        
        except:
            print("Something went wrong")