from typing import TypeVar
from pydantic import BaseModel


InputModel = TypeVar('InputModel', bound=BaseModel)
OutputModel = TypeVar('OutputModel', bound=BaseModel)
DomainModel = TypeVar('DomainModel', bound=BaseModel)
DBModel = TypeVar('DBModel', bound=BaseModel)