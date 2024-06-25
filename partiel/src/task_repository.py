import json

from .task import Task

class TaskRepository:
    def __init__(self, path):
        self.path = path


    def write_task(self, task: Task):
        try:
            with open(self.path, 'r') as json_file:
                tasks_dict_list = json.load(json_file)
        except:
            tasks_dict_list = []
        with open(self.path, 'w') as json_file:
            tasks_dict_list = [task.to_dict()] + tasks_dict_list
            json.dump(tasks_dict_list, json_file, indent=4)

    def read_task(self):
        try:
            with open(self.path, 'r') as json_file:
                tasks_dict_list = json.load(json_file)
                return [Task.from_dict(task_dict) for task_dict in tasks_dict_list]
        except:
            return []


    def update_task(self, id: int):
        try:
            with open(self.path, 'r') as json_file:
                tasks_dict_list = json.load(json_file)
        except:
            print("aucune tache de disponible")

        task = Task.from_dict(tasks_dict_list[id])
        task.mark_finished()
        tasks_dict_list[id] = task.to_dict()

        with open(self.path, 'w') as json_file:
            json.dump(tasks_dict_list, json_file, indent=4)