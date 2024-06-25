import time


class Task:
    def __init__(self, name, date=None, finished=False):
        """
        Initialise une nouvelle tâche.

        :param name: Le nom de la tâche.
        :param finished: Statut d'achèvement de la tâche (par défaut False).
        """
        self.name = name
        self.date = time.time()
        self.finished = False

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "finished": self.finished
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            date=data['date'],
            finished=data['finished']
        )

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        """
        Renvoie une représentation en chaîne de la tâche.
        """
        status = 'X' if self.finished else ' '
        return f"[{status}] {self.name}"
