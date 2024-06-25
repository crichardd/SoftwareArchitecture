from datetime import datetime


class Task:
    def __init__(self, name, date=None, finished=False):
        """
        Initialise une nouvelle tâche.

        :param name: Le nom de la tâche.
        :param finished: Statut d'achèvement de la tâche (par défaut False).
        """
        self.name = name
        self.date = date if date is not None else datetime.now()
        self.finished = finished

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        """
        Renvoie une représentation en chaîne de la tâche.
        """
        status = 'X' if self.finished else ' '
        return f"[{status}] {self.name}"
