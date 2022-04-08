import uuid
from dataclasses import dataclass
from datetime import datetime


class Task:
    def __init__(self, user_id, name, description):
        self.user_id = user_id
        self.name = name
        self.description = description
        self._id = str(uuid.uuid4())
        self._created_at = datetime.now()
        self._importance = None
        self._urgency = None

    def _validate_scale_value(self, value):
        if value < 0:
            raise ValueError("Scale value must be positive")
        if value > 10:
            raise ValueError("Scale value must be at most 10")
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
