from cell_dataclasses import dataclass
from typing import Any

@dataclass
class Cell:
    id: Any
    max_size_bytes: int
    bodies: list
    owners: list
    auditors: list
    writers: list
    readers: list
    is_open: bool