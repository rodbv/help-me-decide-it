import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto


@dataclass
class Task:
    """A task is one item which has a name, description and is positioned in the
    Eisenhower matrix by setting the properties urgency and importance (from 0 to 10)

    Raises:
        ValueError: when urgency or importante is not in the range from 0 to 10 (inclusive)

    Returns:
        A task
    """

    MAX_SCALE_VALUE = 10
    MIN_SCALE_VALUE = -10

    owner: str
    name: str
    description: str
    created_at: datetime = field(init=False, default_factory=datetime.now)
    _urgency: int = field(init=False, repr=False)
    _importance: int = field(init=False, repr=False)

    def _validate_scale_value(self, value):
        if value < self.MIN_SCALE_VALUE or value > self.MAX_SCALE_VALUE:
            raise ValueError(
                "Value must be between {0} and {1}".format(
                    self.MIN_SCALE_VALUE, self.MAX_SCALE_VALUE
                )
            )
        return value

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
    do_now = auto()
    schedule = auto()
    delegate = auto()
    eliminate = auto()
