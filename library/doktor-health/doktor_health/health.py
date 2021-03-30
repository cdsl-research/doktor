import json
from enum import Enum
from typing import NamedTuple


# 多重継承を追加
class HealthStatus(int, Enum):
    """ サービスの状態を簡潔に表す状態を列挙 """
    GREEN = 100
    YELLOW = 200
    RED = 300


class Health(NamedTuple):
    """ サービスの健康状態を定義 """
    status: HealthStatus = HealthStatus.GREEN
    description: str = "It works"
