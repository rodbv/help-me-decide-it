from task import Task
from matrix import Matrix
from quadrant import Quadrant


LOW = -5
HIGH = 5


def create_valid_task(urgency=None, importance=None):
    task = Task(
        owner="valid_owner",
        name="valid_name",
        description="valid_description",
    )
    task.importance = importance
    task.urgency = urgency
    return task


def test_can_add_task_to_matrix():
    matrix = Matrix()
    valid_task = create_valid_task()
    matrix.add_tasks(valid_task)
    assert len(matrix.tasks) == 1


def test_ignores_same_task_added_twice():
    matrix = Matrix()
    valid_task = create_valid_task()
    matrix.add_tasks(valid_task)
    matrix.add_tasks(valid_task)
    assert len(matrix.tasks) == 1


def test_get_task_quadrant():
    matrix = Matrix()

    do_now_task = create_valid_task(importance=HIGH + 1, urgency=HIGH)
    schedule_task = create_valid_task(importance=HIGH, urgency=LOW)
    delegate_task = create_valid_task(importance=LOW, urgency=HIGH)
    eliminate_task = create_valid_task(importance=LOW, urgency=LOW)

    assert matrix.get_task_quadrant(do_now_task) == Quadrant.do_now
    assert matrix.get_task_quadrant(schedule_task) == Quadrant.schedule
    assert matrix.get_task_quadrant(delegate_task) == Quadrant.delegate
    assert matrix.get_task_quadrant(eliminate_task) == Quadrant.eliminate
