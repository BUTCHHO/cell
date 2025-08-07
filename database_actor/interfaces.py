from schemas.abstract import DomainModel

class ModelDB:
    def create(self, domain_model) -> DomainModel: pass
    def delete(self, domain_model) -> DomainModel: pass
    def get(self, **kwargs) -> DomainModel: pass
    def change(self, domain_model_with_new_values, **kwargs) -> DomainModel: pass
    def get_all(self, **kwargs) -> list[DomainModel]: pass
    def get_n(self, n, **kwargs) -> list[DomainModel]: pass