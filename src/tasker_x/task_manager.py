import json
from datetime import datetime
from pathlib import Path

from tasker_x.task import Task

class TaskManager():
    """TaskManager manages all the logic of tasks"""

    def __init__(self, filepath = "tasks.json"):
        self.filepath = filepath
        self.path = Path(self.filepath)

        self.task_status = ['done', 'in-progress', 'todo']

    def path_exists(self) -> bool:
        """Check if file path exists"""
        if not self.path.exists():
            with open(self.path, 'w') as f:
                json.dump([], f)
            return True
    
    def add_task(self, description: str) -> list:
        """Adds a task to json file"""

        try:
            if self.path_exists:

                with open(self.path, encoding='utf-8', mode='r') as f:
                    tasks = json.load(f)
                    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

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
    
    def delete_task(self, id: int) -> list:
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

                    print(f"Task has been deleted (ID: {del_task['id']})")
                    break
            else:
                 print(f"No task has the id {id}")
            
            with open('tasks.json', encoding='utf-8', mode='w') as f:
                json.dump(tasks, f, indent=2)

            return tasks
        
        except:
            print("Something went wrong")
    
    def update_task(self, id: int, description: str) -> list:
        """Updates the description of a task"""

        try:
            with open('tasks.json', encoding='utf-8', mode='r') as f:
                tasks = json.load(f)
                current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            if len(tasks) == 0:
                    print("You haven't created any tasks yet to update")
                    return
            
            for task in tasks:
                if task['id'] == id:
                    task['description'] = description
                    task['updatedAt'] = current_date
                    
                    print(f"Task has been updated (ID: {id})")
                    break
            else:
                 print(f"No task has the id {id}")

            with open('tasks.json', encoding='utf-8', mode='w') as f:
                json.dump(tasks, f, indent=2)

            return tasks
        except:
            print("Something went wrong")

    def mark_task_done(self, id: int) -> list:
        """Marks a tasks status as done"""

        with open('tasks.json', encoding='utf-8', mode='r') as f:
            tasks = json.load(f)
            current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if len(tasks) == 0:
            print("You haven't created any tasks yet to mark")
            return
        
        for task in tasks:
            if task['id'] == id:
                task['status'] = self.task_status[0]
                task['updatedAt'] = current_date
                    
                print(f"Task has been marked done (ID: {id})")
                break

        else:
             print(f"No task has the id {id}")
                 
        with open('tasks.json', encoding='utf-8', mode='w') as f:
            json.dump(tasks, f, indent=2)

        return tasks
    
    def mark_task_in_progress(self, id: int) -> list:
        """Marks a tasks status in-progress"""
         
        with open('tasks.json', encoding='utf-8', mode='r') as f:
            tasks = json.load(f)
            current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
        if len(tasks) == 0:
            print("You haven't created any tasks yet to mark")
            return
        
        for task in tasks:
             if task['id'] == id:
                task['status'] = self.task_status[1]
                task['updatedAt'] = current_date
                
                print(f"Task has been marked in-progress (ID: {id})")
                break
        else:
            print(f"No task has the id {id}")

        with open('tasks.json', encoding='utf-8', mode='w') as f:
            json.dump(tasks, f, indent=2)
        
        return tasks
    
    def show_tasks(self, task):
        print(f"\tID: {task['id']}")
        print(f"\tDescription: {task['description']}")
        print(f"\tStatus: {task['status']}")
        print(f"\tCreated at: {task['createdAt']}")
        print(f"\tUpdated at: {task['updatedAt']}")
        print("\n")
    
    def list_tasks(self, status: str) -> list:
        """Lists tasks"""

        try:
            with open('tasks.json', encoding='utf-8', mode='r') as f:
                tasks = json.load(f)
        
            if len(tasks) == 0:
                print("You haven't created any tasks yet to mark")
                return

            filtered_tasks = []

            if status == 'all':
                for task in tasks:
                    self.show_tasks(task)
                    filtered_tasks.append(task)
            elif status == self.task_status[0]:
                for task in tasks:
                    if task['status'] == 'done':
                        self.show_tasks(task)
                        filtered_tasks.append(task)
            elif status == self.task_status[1]:
                for task in tasks:
                    if task['status'] == 'in-progress':
                        self.show_tasks(task)
                        filtered_tasks.append(task)
            elif status == self.task_status[2]:
                for task in tasks:
                    if task['status'] == 'todo':
                        self.show_tasks(task)
                        filtered_tasks.append(task)
            else:
                print(f"There is no task with the status {status}")

        except:
            print("Something went wrong")

        return filtered_tasks