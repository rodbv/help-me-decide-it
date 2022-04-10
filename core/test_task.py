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
