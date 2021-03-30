import json
from enum import Enum
from typing import NamedTuple


# 多重継承を追加
class HealthStatus(int, Enum):
    """ サービスの状態を簡潔に表す状態を列挙 """
    GREEN = 100
    YELLOW = 200
    RED = 300


class Health(object):
    """ サービスの健康状態を定義 """

    def __init__(self,
                 status: HealthStatus,
                 description: str):
        self.status = status
        self.description = description

    def to_dict(self):
        return {
            "status": int(self.status),
            "description": self.description
        }
