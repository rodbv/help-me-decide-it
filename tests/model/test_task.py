import pytest
from model import task
from datetime import datetime


valid_high = task.Task.MAX_SCALE_VALUE
valid_low = task.Task.MIN_SCALE_VALUE


def create_valid_task(urgency=None, importance=None):
    t = task.Task(
        owner="valid_owner",
        name="valid_name",
        description="valid_description",
    )
    t.importance = importance
    t.urgency = urgency
    return t


def test_task_is_created_with_timestamp():
    t = create_valid_task()
    assert type(t.created_at) is datetime


def test_throws_error_if_importance_is_less_than_minimum_allowed():
    t = create_valid_task()
    invalid_low_value = task.Task.MIN_SCALE_VALUE - 1
    with pytest.raises(ValueError):
        t.importance = invalid_low_value


def test_throws_error_if_importance_is_more_than_max_allowed():
    t = create_valid_task()
    invalid_high_value = task.Task.MAX_SCALE_VALUE + 1
    with pytest.raises(ValueError):
        t.importance = invalid_high_value


def test_throws_error_if_urgency_is_less_than_minimum_allowed():
    t = create_valid_task()
    invalid_low_value = task.Task.MIN_SCALE_VALUE - 1
    with pytest.raises(ValueError):
        t.urgency = invalid_low_value


def test_throws_error_if_urgency_is_more_than_max_allowed():
    t = create_valid_task()
    invalid_high_value = task.Task.MAX_SCALE_VALUE + 1
    with pytest.raises(ValueError):
        t.urgency = invalid_high_value
