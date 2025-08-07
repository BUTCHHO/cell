from schemas.input import RepositoryInputModel
from schemas.domain import RepositoryDomainModel
from transformer.interfaces import IModelTransformer




class RepositoryCreationHandler:
    def __init__(self, repository_creator, model_transformer):
        self.repository_creator = repository_creator
        self.model_transformer:IModelTransformer = model_transformer

    def _transfer_to_domain(self, repository_model):
         return self.model_transformer.input_to_domain(repository_model, RepositoryDomainModel)

    def create_repository(self, repository_model: RepositoryInputModel):
        repository_model = self._transfer_to_domain(repository_model)
        self.repository_creator.create_repository(repository_model)

