from typing import List, TypeVar

T = TypeVar('T')

def get_first(collection: List[T]) -> T:
    return collection[0]