from fastapi import APIRouter
from schemas.input import RepositoryInputModel


creator_router = APIRouter(prefix='/create/')


@creator_router.get('repository')
def create_repository_endpoint(repository: RepositoryInputModel): pass