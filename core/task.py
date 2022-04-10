import uuid
from dataclasses import dataclass, field
from datetime import datetime
from quadrant import Quadrant


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
        """ensures that the value being passed for urgency and importance are either None or within the min and max values"""

        if value is None:
            return value

        if value < self.MIN_SCALE_VALUE or value > self.MAX_SCALE_VALUE:
            raise ValueError(
                f"Value must be between {self.MIN_SCALE_VALUE} and {self.MAX_SCALE_VALUE}"
            )
        return value

    def __repr__(self):
        return f"Task {self.name!r}, created by by {self.owner}. Urgency: {self._urgency}, importance: {self._importance}. Recommend action: {self.recommended_action}"

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
            return Quadrant.do_now

        if not self.is_important and self.is_urgent:
            return Quadrant.delegate

        if self.is_important and not self.is_urgent:
            return Quadrant.schedule

        if not self.is_important and not self.is_urgent:
            return Quadrant.eliminate

        return None
