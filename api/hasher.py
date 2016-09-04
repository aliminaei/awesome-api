import hashlib
import os

def hash_password(password):
    salt = os.urandom(16)
    return hashlib.sha224(password).hexdigest()
