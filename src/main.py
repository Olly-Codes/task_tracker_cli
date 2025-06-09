import argparse as ap

from task_manager import TaskManager

task_manager = TaskManager()

parser = ap.ArgumentParser(description='helps you track and manage tasks')
subparsers = parser.add_subparsers(dest='commands')

add_parser = subparsers.add_parser('add', help='adding a task')
add_parser.add_argument('description', help='description of the task')
args = parser.parse_args()

if args.commands == 'add':
    task_manager.path_exists()
    task_manager.add_task(args.description)