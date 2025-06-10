import argparse as ap

from task_manager import TaskManager

task_manager = TaskManager()

parser = ap.ArgumentParser(description='helps you track and manage tasks')
subparsers = parser.add_subparsers(dest='commands')

add_parser = subparsers.add_parser('add', help='adds a task')
add_parser.add_argument('description', help='description of the task')

delete_parser = subparsers.add_parser('delete', help='deletes a task')
delete_parser.add_argument('id',type=int, help='id of task to be deleted')

update_parser = subparsers.add_parser('update', help='updates a tasks')
update_parser.add_argument('id', type=int, help='id of task to be updated')
update_parser.add_argument('description', help='new description of task')

mark_done_parser = subparsers.add_parser('mark-done', help='mark task done')
mark_done_parser.add_argument('id',type=int, help='id of task to be marked')

mark_in_progress_parser = subparsers.add_parser('mark-in-progress',
                                                help='mark task in-progress')
mark_in_progress_parser.add_argument('id',type=int,
                              help='id of task to be marked in-progress')

list_parser = subparsers.add_parser('list', help='lists tasks')
list_parser.add_argument('status', nargs='?', default='all', help='status of task')

args = parser.parse_args()

if args.commands == 'add':
    task_manager.path_exists()
    task_manager.add_task(args.description)
elif args.commands == 'delete':
    task_manager.path_exists()
    task_manager.delete_task(args.id)
elif args.commands == 'update':
    task_manager.path_exists()
    task_manager.update_task(args.id, args.description)
elif args.commands == 'mark-done':
    task_manager.path_exists()
    task_manager.mark_task_done(args.id)
elif args.commands == 'mark-in-progress':
    task_manager.path_exists()
    task_manager.mark_task_in_progress(args.id)
elif args.commands == 'list':
    task_manager.path_exists()
    task_manager.list_tasks(args.status)