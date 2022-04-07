import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    _id = str(uuid.uuid4())
    user_id: str
    name: str
    description: str
    _created_at = datetime.now()

    @property
    def id(self) -> str:
        return self._id

    @property
    def created_at(self) -> datetime:
        return self._created_at
