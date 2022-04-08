import pytest
from model import Task, Quadrants
from datetime import datetime


def create_valid_task():
    return Task(
        owner="valid_owner",
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
    invalid_low_value = Task.min_scale_value - 1
    with pytest.raises(ValueError):
        task.importance = invalid_low_value


def test_throws_error_if_importance_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = Task.max_scale_value + 1
    with pytest.raises(ValueError):
        task.importance = invalid_high_value


def test_throws_error_if_urgency_is_less_than_minimum_allowed():
    task = create_valid_task()
    invalid_low_value = Task.min_scale_value - 1
    with pytest.raises(ValueError):
        task.urgency = invalid_low_value


def test_throws_error_if_urgency_is_more_than_max_allowed():
    task = create_valid_task()
    invalid_high_value = Task.max_scale_value + 1
    with pytest.raises(ValueError):
        task.urgency = invalid_high_value


def test_task_with_high_importance_and_urgency_are_categorized_as_do_now():
    task = create_valid_task()
    task.urgency = 5
    task.importance = 5
    assert task.recommended_action == Quadrants.do_now


def test_task_with_high_importance_and_low_urgency_are_categorized_as_schedule():
    task = create_valid_task()
    task.urgency = -5
    task.importance = 5
    assert task.recommended_action == Quadrants.schedule


def test_task_with_low_importance_and_high_urgency_are_categorized_as_delegate():
    task = create_valid_task()
    task.urgency = 5
    task.importance = -5
    assert task.recommended_action == Quadrants.delegate


def test_task_with_low_importance_and_low_urgency_are_categorized_as_delegate():
    task = create_valid_task()
    task.urgency = -5
    task.importance = -5
    assert task.recommended_action == Quadrants.eliminate
