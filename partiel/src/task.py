import time

class Task:
    def __init__(self, content, time_stamp=None, finished=False):
        """
        Initialise une nouvelle tâche.

        :param content: Le nom de la tâche.
        """
        self.content = content
        self.time = time_stamp if time_stamp is not None else time.time()
        self.finished = finished

    def mark_finished(self):
        self.finished = True

    def to_dict(self):
        return {
            "content": self.content,
            "time": self.time,
            "finished": self.finished
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            content=data['content'],
            time_stamp=data['time'],
            finished=data['finished']
        )

    def __eq__(self, other):
        if isinstance(other, Task):
            return (self.content == other.content and
                    self.time == other.time and
                    self.finished == other.finished)
        return False


    def __str__(self):
        """
        Renvoie une représentation en chaîne de la tâche.
        """
        status = 'X' if self.finished else ' '
        return f"[{status}] {self.content}"
