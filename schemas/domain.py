import pydantic


class RepositoryDomainModel(pydantic.BaseModel):
    id: str | None = None
    name: str | None = None
    owner_id: str | None = None
