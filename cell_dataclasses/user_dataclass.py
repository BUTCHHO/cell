from dataclasses import dataclass
from typing import Any

@dataclass
class User:
    id: Any
    name: str
    password: str
