from enum import Enum
from typing import List


def get_enum_values(enum: Enum) -> List[str]:
    return [item.value for item in enum]