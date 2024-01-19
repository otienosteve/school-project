from main import bcrypt


def generate_hash(password):
    return bcrypt.generate_password_hash(password)