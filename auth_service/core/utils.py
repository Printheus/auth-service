import bcrypt

def bcrypt_hasher(passwd: str) -> bytes:
    salt = bcrypt.gensalt()
    passwd = bcrypt.hashpw(passwd.encode(), salt)
    return passwd

