""" サービスの健康状態を定義

サービスの健康状態を定義する．それぞれのマイクロサービスを対象に
共通の監視用エンドポイントのインターフェースを提供する．

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

import json
from enum import Enum
from typing import NamedTuple


# 多重継承を追加
class HealthStatus(int, Enum):
    """
    サービスの状態を簡潔に表す状態を列挙．
    """
    GREEN = 100
    YELLOW = 200
    RED = 300


class Health(object):
    """ サービスヘルス

    サービスの健康状態を扱う．
    これを元にそれぞれのマイクロサービスの健康状態を表すエンドポイントの応答が作られる．

    Attributes:
        status (HealthStatus): サービスの状態をHealthStatusで表す．
        description (str): サービスの状態の詳細を英語で表す．人間が読むことを意識．
    """

    def __init__(self,
                 status: HealthStatus,
                 description: str):
        """ Healthクラスのコンストラクタ

        サービスの健康状態を初期化する．

        Note:
            statusはHealthStatusクラスから設定する．

        Args:
            status(HealthStatus): サービスの状態をHealthStatusで表す．
            description(str): サービスの状態の詳細を英語で表す．人間が読むことを意識．
        """
        self.status = status
        self.description = description

    def to_dict(self):
        """ 辞書化するメソッド

        辞書型でデータ属性(data attribute)を返す．

        Returns:
            dict: インスタンスが保持するデータ属性を返す．
        """
        return {
            "status": int(self.status),
            "description": self.description
        }
