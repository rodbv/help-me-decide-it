from model import matrix, task


LOW = -5
HIGH = 5


def create_valid_task(urgency=None, importance=None):
    valid_task = task.Task(
        owner="valid_owner",
        name="valid_name",
        description="valid_description",
        urgency=urgency,
        importance=importance,
    )
    return valid_task


def test_can_add_task_to_matrix():
    m = matrix.Matrix()
    valid_task = create_valid_task()
    m.add_tasks(valid_task)
    assert len(m.tasks) == 1


def test_ignores_same_task_added_twice():
    m = matrix.Matrix()
    valid_task = create_valid_task()
    m.add_tasks(valid_task, valid_task)
    assert len(m.tasks) == 1


def test_task_urgent_and_important_goes_to_do_now_quadrant():
    m = matrix.Matrix()
    do_now_task = create_valid_task(importance=HIGH + 1, urgency=HIGH)
    assert m.get_task_quadrant(do_now_task) == matrix.Quadrant.do_now


def test_task_urgent_and_not_important_goes_to_delegate_quadrant():
    m = matrix.Matrix()
    delegate_task = create_valid_task(importance=LOW, urgency=HIGH)
    assert m.get_task_quadrant(delegate_task) == matrix.Quadrant.delegate


def test_task_not_urgent_and_important_goes_to_schedule_quadrant():
    m = matrix.Matrix()
    schedule_task = create_valid_task(importance=HIGH, urgency=LOW)
    assert m.get_task_quadrant(schedule_task) == matrix.Quadrant.schedule


def test_task_not_urgent_and_not_important_goes_to_eliminate_quadrant():
    m = matrix.Matrix()
    eliminate_task = create_valid_task(importance=LOW, urgency=LOW)
    assert m.get_task_quadrant(eliminate_task) == matrix.Quadrant.eliminate


def test_get_matrix_as_backlog():
    m = matrix.Matrix()

    do_now_task = create_valid_task(importance=HIGH, urgency=HIGH)
    delegate_task = create_valid_task(importance=LOW + 1, urgency=HIGH)
    schedule_task = create_valid_task(importance=HIGH, urgency=LOW)
    eliminate_task = create_valid_task(importance=LOW, urgency=LOW)
    m.add_tasks(do_now_task, delegate_task, schedule_task, eliminate_task)

    assert [
        do_now_task,
        delegate_task,
        schedule_task,
        eliminate_task,
    ] == m.get_backlog()
