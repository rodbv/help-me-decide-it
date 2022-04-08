import pytest
from model import Task
from datetime import datetime


def create_valid_task():
    return Task(
        user_id="valid_user_id",
        name="valid_name",
        description="valid_description",
    )


def test_task_is_created_with_timestamp_and_id():
    task = create_valid_task()

    assert type(task.created_at) is datetime
    assert len(task.id) == 36


def test_task_can_have_importance_and_urgency_assigned():
    task = create_valid_task()
    task.importance = 5
    task.urgency = 4

    assert task.importance == 5
    assert task.urgency == 4


def test_throws_error_if_importance_is_less_than_minimum_allowed():
    task = create_valid_task()
    invalid_low_value = -1
    with pytest.raises(ValueError):
        task.importance = invalid_low_value


def test_throws_error_if_importance_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = 1000
    with pytest.raises(ValueError):
        task.importance = invalid_high_value


def test_throws_error_if_urgency_is_less_than_minimum_allowed():
    task = create_valid_task()
    invalid_low_value = -1
    with pytest.raises(ValueError):
        task.urgency = invalid_low_value


def test_throws_error_if_urgency_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = 1000
    with pytest.raises(ValueError):
        task.urgency = invalid_high_value
