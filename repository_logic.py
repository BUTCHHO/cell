from path_explorator.interfaces import IStorageWriter

class RepositoryMaker:
    def __init__(self, filesystem_actor: IStorageWriter, CELL_REPO_ROOT: str, repository_db, hash_maker, repo_id_len):
        self.filesystem_actor = filesystem_actor
        self.CELL_REPO_ROOT = CELL_REPO_ROOT
        self.repository_db = repository_db
        self.hash_maker = hash_maker
        self.repo_id_len = repo_id_len

    def make_new_repository(self, user_model, repo_model):
        repository_id = self.hash_maker.make_hash(self.repo_id_len)
        self.filesystem_actor.create_dir(path=self.CELL_REPO_ROOT, name=repository_id, exist_ok=False)
