import uuid
from dataclasses import dataclass
from datetime import datetime


class Task:
    """A task is one item which has a name, description and is positioned in the
    Eisenhower matrix by setting the properties urgency and importance (from 0 to 10)

    Raises:
        ValueError: when urgency or importante is not in the range from 0 to 10 (inclusive)

    Returns:
        A task
    """

    max_scale_value = 10
    min_scale_value = 0

    def __init__(self, owner, name, description):
        self.owner = owner
        self.name = name
        self.description = description
        self._id = str(uuid.uuid4())
        self._created_at = datetime.now()
        self._importance = None
        self._urgency = None

    def _validate_scale_value(self, value):
        scale_values = range(self.min_scale_value, self.max_scale_value + 1)

        if value not in scale_values:
            raise ValueError("Scale value must be positive")
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
