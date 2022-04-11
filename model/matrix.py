from model.task import Task
from enum import Enum


class Quadrant(Enum):
    do_now = "Do Now"
    schedule = "Schedule"
    delegate = "Delegate"
    eliminate = "Eliminate"


class Matrix:
    def __init__(self):
        self._tasks: set[Task] = set()

    def add_tasks(self, *tasks):
        [self._tasks.add(task) for task in tasks]

    @property
    def tasks(self):
        return self._tasks

    def get_backlog(self):
        return sorted(self._tasks, key=lambda task: task.ranking())

    @staticmethod
    def get_task_quadrant(task: Task) -> Quadrant:
        if task.is_important:
            return Quadrant.do_now if task.is_urgent else Quadrant.schedule
        return Quadrant.delegate if task.is_urgent else Quadrant.eliminate
