from partiel.Task import Task

if __name__ == "__main__":
    task = Task("my task")
    print(task)
    task.mark_finished()
    print(task)