from odor_helper.security.md5_hasher import MD5Hasher
from odor_helper.security.pbkdf2_hasher import PBKDF2Hasher

_hashers = [
    MD5Hasher,
    PBKDF2Hasher,
    ]

def get_hasher(hasher_name):
    for hasher in _hashers:
        if hasher.hasher_name == hasher_name:
            return hasher
    raise ValueError("no such hasher name")