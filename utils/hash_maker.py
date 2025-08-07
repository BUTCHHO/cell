from werkzeug.security import generate_password_hash, check_password_hash

class IHashMaker:
    def make_hash(self, len_of_hash) -> str: pass
    def hash_string(self, string:str, len_of_hash) -> str: pass
    def make_password_hash(self, orig: str) -> str: pass
    def compare_password_hash(self, orig:str, hashed:str) -> bool: pass

class HashMaker:

    def make_password_hash(self, orig):
        return generate_password_hash(orig)

    def compare_password_hash(self, orig, hashed):
        return check_password_hash(hashed, orig)

