import unittest
import json
import time
import os


from src.task_repository import TaskRepository
from src.task import Task



class TaskTestCase(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test task")
        self.assertEqual(task.content, "Test task")
        self.assertFalse(task.finished)

    def test_mark_finished(self):
        task = Task("Test task")
        task.mark_finished()
        self.assertTrue(task.finished)

    def test_to_dict(self):
        task = Task("Test task")
        task_dict = task.to_dict()
        self.assertEqual(task_dict['content'], "Test task")
        self.assertFalse(task_dict['finished'])

    def test_from_dict(self):
        data = {
            "content": "Test task",
            "time": time.time(),
            "finished": False
        }
        task = Task.from_dict(data)
        self.assertEqual(task.content, "Test task")
        self.assertFalse(task.finished)
        self.assertEqual(task.time, data['time'])

    def test_repository_save(self):
        repo_path = "test_repository_save.json"
        task = Task("test_repository_save")
        task_repository = TaskRepository(repo_path)
        task_repository.write_task(task)
        with open(task_repository.path, 'r') as json_file:
            tasks_dict_list = json.load(json_file)
            tasks = [Task.from_dict(task_dict) for task_dict in tasks_dict_list]
            self.assertEqual(tasks[0], task)
        os.remove(repo_path)

    def test_repository_read(self):
        repo_path = "test_repository_read.json"
        task_repository = TaskRepository(repo_path)
        task = Task("test_repository_read")
        task_repository.write_task(task)
        tasks = task_repository.read_task()
        self.assertEqual(tasks[0], task)
        os.remove(repo_path)

    def test_repository_update(self):
        repo_path = "test_repository_update.json"
        task_repository = TaskRepository(repo_path)
        task = Task("test_repository_update")
        task_repository.write_task(task)
        task_repository.update_task(0)
        tasks = task_repository.read_task()
        self.assertTrue(tasks[0].finished)
        os.remove(repo_path)


if __name__ == '__main__':
    unittest.main()