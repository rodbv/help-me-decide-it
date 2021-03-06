import pytest
from model import task
from datetime import datetime
import math

VALID_HIGH = task.Task.MAX_SCALE_VALUE
VALID_LOW = task.Task.MIN_SCALE_VALUE
PRIORITY_TEST_DELTA = 0.001


def create_valid_task(urgency=None, importance=None):
    t = task.Task(
        owner="valid_owner",
        name="valid_name",
        description="valid_description",
        urgency=urgency,
        importance=importance,
    )
    return t


class TestTask:
    def test_task_is_created_with_timestamp(self):
        t = create_valid_task()
        assert type(t.created_at) is datetime


class TestPriority:
    def test_task_with_importance_2_and_urgency_3_has_priority_10_63(self):
        t = create_valid_task(urgency=3, importance=2)
        expected = math.sqrt(8**2 + 7**2)
        assert expected == pytest.approx(t.priority(), PRIORITY_TEST_DELTA)

    def test_task_with_importance_minus2_and_urgency_minus3_has_priority_17_69(self):
        t = create_valid_task(urgency=-3, importance=-2)
        expected = math.sqrt(13**2 + 12**2)
        assert expected == pytest.approx(t.priority(), PRIORITY_TEST_DELTA)


class TestTaskValidation:
    def test_throws_error_if_importance_is_less_than_minimum_allowed(self):
        t = create_valid_task()
        invalid_low_value = task.Task.MIN_SCALE_VALUE - 1
        with pytest.raises(ValueError):
            t.importance = invalid_low_value

    def test_throws_error_if_importance_is_more_than_max_allowed(self):
        t = create_valid_task()
        invalid_high_value = task.Task.MAX_SCALE_VALUE + 1
        with pytest.raises(ValueError):
            t.importance = invalid_high_value

    def test_throws_error_if_urgency_is_less_than_minimum_allowed(self):
        t = create_valid_task()
        invalid_low_value = task.Task.MIN_SCALE_VALUE - 1
        with pytest.raises(ValueError):
            t.urgency = invalid_low_value

    def test_throws_error_if_urgency_is_more_than_max_allowed(self):
        t = create_valid_task()
        invalid_high_value = task.Task.MAX_SCALE_VALUE + 1
        with pytest.raises(ValueError):
            t.urgency = invalid_high_value
