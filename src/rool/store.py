from dataclasses import dataclass

from typing import Dict, Optional

type Value = str | int | float | bool


@dataclass
class Store:
    data: Dict[str, Value]

    def __init__(self, **data):
        self.data = data

    def get(self, key) -> Value:
        return self.data[key]

    def add(self, key: str, value: Value) -> Optional[Value]:
        original = self.data.get(key)
        self.data[key] = value
        return original

    def remove(self, key) -> Optional[Value]:
        self.data.pop(key)

    def size(self) -> int:
        return len(self.data)
