from schemas.abstract import DomainModel
from typing import Type


class IRepositoryActor:
    def create_repository(self, repository: Type[DomainModel] ): pass
    def change_repository_name(self, repository: Type[DomainModel]): pass
    def delete_repository(self, repository: Type[DomainModel]): pass

class IRepositoryReader:
    def get_repository_size(self, repository: Type[DomainModel]) -> int:pass
    def get_repository_entities_count(self, repository: Type[DomainModel]) -> int: pass
