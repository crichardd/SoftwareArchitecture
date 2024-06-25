from src.arg_parser import parse_args, create_parser
from src.clock import elapsed_time
from src.task_repository import TaskRepository
from src.task import Task


task_repository = TaskRepository("tasks.json")


def add_task(task_content: str):
    task = Task(task_content)
    task_repository.write_task(task)
    list_tasks()


def finish_task(task_id: int):
    task_list = task_repository.read_task()
    if task_id-1 >=  len(task_list):
        print("L'index n'est pas compris dans la liste")
        exit(0)
    task_repository.update_task(task_id - 1)
    list_tasks()


def list_tasks():
    task_list = task_repository.read_task()
    if len(task_list) == 0:
        print("Il n'y a pas de tache")
        exit(0)
    for i, task in enumerate(task_list):
        print(f"[{i+1}] {task} ({elapsed_time(task.time)})")


if __name__ == "__main__":
    args = parse_args()

    if args.command == 'add':
        add_task(args.content)
    elif args.command == 'finish':
        finish_task(args.id)
    elif args.command == 'list':
        list_tasks()
    else:
        parser = create_parser()
        parser.print_help()
