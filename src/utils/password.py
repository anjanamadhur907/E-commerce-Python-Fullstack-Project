import bcrypt

def hash_password(password: str):
    """
    convert password to hashed password
    """
    password_bytes = password.encode('utf-8')
    salt_key = bcrypt.gensalt(10)
    return bcrypt.hashpw(password_bytes, salt_key).decode('utf-8')