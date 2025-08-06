from pydantic import BaseModel

from abc import ABC, abstractmethod
from typing import Type

from schemas.abstract import InputModel, DomainModel, OutputModel, DBModel


class IModelTransformer(ABC):
    """transfers and validates models and their params"""
    def input_to_domain(self, input_model: Type[InputModel], domain_model:Type[DomainModel]) -> DomainModel:pass
    def domain_to_output(self, domain_model: Type[DomainModel], output_model:Type[OutputModel]) -> OutputModel: pass
    def db_to_domain(self, db_model: Type[DBModel], domain_model:Type[DomainModel]) -> DomainModel: pass