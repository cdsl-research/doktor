import json
from enum import Enum
from typing import NamedTuple


class HealthStatus(Enum):
    GREEN = 100
    YELLOW = 200
    RED = 300

class Health(NamedTuple):
    status : HealthStatus
    description : str