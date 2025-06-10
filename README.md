# Task Tracker CLI
![tasker-x_demo](https://github.com/user-attachments/assets/6dc5d0a7-5c01-4021-9d24-e955264a7df3)

## Description
TaskerX is a command-line interface (CLI) application built for the management and tracking of tasks. This application allows users to add, delete, update, list, and manage their tasks easily.

## Features
TaskerX allows users to track and manager their tasks using various commands. This involve:
- **Adding tasks**: A task can be added by using the **add** command and providing a **description**. The task will be given an automatic idea and a timestamp so the user can be aware when the task was created.
- **Updating tasks**: A task can be updated by using the **update** command and providing a task **id** and a new **description**. The task's description will be updated along with the timestamp to show when the task was updated last.
- **Deleting tasks**: A task can be simply deleted by using the **delete** command and providing a task **id**. This allows the user to delete tasks easily
- **Marking status of tasks**: Tasks can be makred as **done** or **in-progress** by the user. They can use the commands **mark-in-progress** and **mark-done** and providing as task **id**
- **Listing tasks**: When a task is created, it has the status of todo by default. However, a user can **list** all the tasks or filter and choose between different statuses like, **done**, **todo**, and **in-progress**

## Installation and usage
1. Clone this repo, or download the zip
2. Run this command in the project folder:
```
pip install --editable .
```

Then from there, you can use the various commands like so:
```
tasker-x add "Do some coding"
tasker-x list done
tasler-x update 2 "Learn more python"
```

## Project source
This project was sourced from [Roadmapsh](https://roadmap.sh/projects/task-tracker)

