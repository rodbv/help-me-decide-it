from dataclasses import dataclass, field
from datetime import datetime
import math


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

    def ranking(self):
        """
        The ranking of the task is the point distance between the urgency and importante of the task
        in relation to the point of maximum importance and urgency in the scale, which is 10.

        For example if a task has urgency 2 and importance 3, that would be calculated as:
        ranking = math.sqrt((MAX_URGENCY-task.urgency)**2 + (MAX_IMPORTANCE-task.importance)**2) which is
        math.sqrt(8**2 + 7**2) which is math.sqrt(64+49), or approximately 10.63
        """
        dist_importance = self.MAX_SCALE_VALUE - self.importance
        dist_urgency = self.MAX_SCALE_VALUE - self.urgency
        return math.sqrt((dist_importance**2) + (dist_urgency**2))

    def __hash__(self):
        return hash(id(self))
