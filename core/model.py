import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class Task:
    """A task is one item which has a name, description and is positioned in the
    Eisenhower matrix by setting the properties urgency and importance (from 0 to 10)

    Raises:
        ValueError: when urgency or importante is not in the range from 0 to 10 (inclusive)

    Returns:
        A task
    """

    max_scale_value = 10
    min_scale_value = -10

    def __init__(self, owner, name, description):
        self.owner = owner
        self.name = name
        self.description = description
        self._id = str(uuid.uuid4())
        self._created_at = datetime.now()
        self._importance = None
        self._urgency = None

    def _validate_scale_value(self, value):
        if value < self.min_scale_value or value > self.max_scale_value:
            raise ValueError(
                "Value must be between {0} and {1}".format(
                    self.min_scale_value, self.max_scale_value
                )
            )
        return value

    @property
    def id(self) -> str:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def importance(self):
        return self._importance

    @importance.setter
    def importance(self, value):
        self._importance = self._validate_scale_value(value)

    @property
    def urgency(self):
        return self._urgency

    @urgency.setter
    def urgency(self, value):
        self._urgency = self._validate_scale_value(value)

    @property
    def is_important(self):
        return self.importance > 0

    @property
    def is_urgent(self):
        return self.urgency > 0

    @property
    def recommended_action(self):
        if self.is_important and self.is_urgent:
            return Quadrants.do_now

        if not self.is_important and self.is_urgent:
            return Quadrants.delegate

        if self.is_important and not self.is_urgent:
            return Quadrants.schedule

        return Quadrants.eliminate


class Quadrants(Enum):
    do_now = 1
    schedule = 2
    delegate = 3
    eliminate = 4
