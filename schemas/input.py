import pydantic


class RepositoryInputModel(pydantic.BaseModel):
    name: str = pydantic.Field(max_length=64, min_length=1)