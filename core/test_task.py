import pytest
from task import Task
from quadrant import Quadrant
from datetime import datetime


valid_high = Task.MAX_SCALE_VALUE
valid_low = Task.MIN_SCALE_VALUE


def create_valid_task(urgency=None, importance=None):
    task = Task(
        owner="valid_owner",
        name="valid_name",
        description="valid_description",
    )
    task.importance = importance
    task.urgency = urgency
    return task


def test_task_is_created_with_timestamp():
    task = create_valid_task()
    assert type(task.created_at) is datetime


def test_throws_error_if_importance_is_less_than_minimum_allowed():
    task = create_valid_task()
    invalid_low_value = Task.MIN_SCALE_VALUE - 1
    with pytest.raises(ValueError):
        task.importance = invalid_low_value


def test_throws_error_if_importance_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = Task.MAX_SCALE_VALUE + 1
    with pytest.raises(ValueError):
        task.importance = invalid_high_value


def test_throws_error_if_urgency_is_less_than_minimum_allowed():
    task = create_valid_task()
    invalid_low_value = Task.MIN_SCALE_VALUE - 1
    with pytest.raises(ValueError):
        task.urgency = invalid_low_value


def test_throws_error_if_urgency_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = Task.MAX_SCALE_VALUE + 1
    with pytest.raises(ValueError):
        task.urgency = invalid_high_value


def test_task_with_high_importance_and_urgency_are_categorized_as_do_now():
    task = create_valid_task()
    task.urgency = valid_high
    task.importance = valid_high
    assert task.recommended_action == Quadrant.do_now


def test_task_with_high_importance_and_low_urgency_are_categorized_as_schedule():
    task = create_valid_task()
    task.urgency = valid_low
    task.importance = valid_high
    assert task.recommended_action == Quadrant.schedule


def test_task_with_low_importance_and_high_urgency_are_categorized_as_delegate():
    task = create_valid_task()
    task.urgency = valid_high
    task.importance = valid_low
    assert task.recommended_action == Quadrant.delegate


def test_task_with_low_importance_and_low_urgency_are_categorized_as_eliminate():
    task = create_valid_task()
    task.urgency = valid_low
    task.importance = valid_low
    assert task.recommended_action == Quadrant.eliminate


def test_task_representation_includes_urgency_importance_and_recommended_action():
    task = create_valid_task(urgency=4, importance=3)
    task_repr = str(task)
    print(task_repr)
