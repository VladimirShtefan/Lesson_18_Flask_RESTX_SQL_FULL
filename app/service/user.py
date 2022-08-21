import hashlib

from app.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT


class User:
    def get_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
