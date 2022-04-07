import pytest
from model import Task
from datetime import datetime


def test_task_is_created_with_timestamp_and_id():
    task = Task(
        user_id="valid_user_id",
        name="valid_name",
        description="valid_description",
    )

    assert type(task.created_at) is datetime
    assert len(task.id) == 36
