from task import Task
from quadrant import Quadrant


class Matrix:
    def __init__(self):
        self._tasks: set[Task] = set()

    def add_tasks(self, *tasks) -> None:
        [self._tasks.add(task) for task in tasks]

    @property
    def tasks(self):
        return self._tasks

    @staticmethod
    def get_task_quadrant(task: Task) -> Quadrant:
        if task.is_important and task.is_urgent:
            return Quadrant.do_now

        if not task.is_important and task.is_urgent:
            return Quadrant.delegate

        if task.is_important and not task.is_urgent:
            return Quadrant.schedule

        if not task.is_important and not task.is_urgent:
            return Quadrant.eliminate

        return None
