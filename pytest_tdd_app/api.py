from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def add(task: Task) -> int:
    """Add a task (object) to the task database."""
    if not isinstance(task, Task):
        raise TypeError("task must be Task object.")
    if not isinstance(task.summary, str):
        raise TypeError("task.summary must be string.")
    if not (isinstance(task.owner, str) or (task.owner is None)):
        raise TypeError("task.owner must be None or string.")

    task_id = 1 # _taskdb.add(task._asdict())
    return task_id