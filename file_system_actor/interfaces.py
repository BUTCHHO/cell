
class IStorageReader:
    @property
    def root_path(self) -> str: return 'none'
    def join_with_root_path(self, path: str) -> str: pass
    def get_all_filenames_in_dir(self, dirpath: str | None) -> list[str]: pass
    def get_all_entitynames_in_dir(self, dirpath: str | None) -> list[str]: pass
    def find_entities_path(self, searching_in: str | None, pattern: str) -> list[str]: pass
    def is_exists(self, path: str | None) -> bool: pass
    def is_file(self, path: str | None) -> bool: pass
    def is_dir(self, path: str | None) -> bool: pass
    def get_name(self, path: str | None) -> str: pass

class IStorageWriter:
    def delete_entity(self, path: str | None): pass
    def create_dir(self, path: str | None, name:str, exist_ok=True): pass
    def create_file(self, path: str | None , name: str, exist_ok): pass
