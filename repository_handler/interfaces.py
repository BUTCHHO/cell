from schemas.abstract import DomainModel
from typing import Type


class IRepositoryCreator:
    def create_repository(self, repository: Type[DomainModel] ):