import time

def elapsed_time(taskTime: int):
    """
    Retourne le temps écoulé depuis la création de la tâche formaté en secondes, minutes, heures, etc.

    :return: Temps écoulé formaté en chaîne de caractères.
    """
    elapsed_seconds = time.time() - taskTime
    if elapsed_seconds < 60:
        return f"{int(elapsed_seconds)} seconds"
    elif elapsed_seconds < 3600:
        minutes = elapsed_seconds // 60
        return f"{int(minutes)} minutes"
    elif elapsed_seconds < 86400:
        hours = elapsed_seconds // 3600
        return f"{int(hours)} hours"
    else:
        days = elapsed_seconds // 86400
        return f"{int(days)} days"
