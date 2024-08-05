from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def is_password_exists(password, hased_password):
    return pwd_context.verify(password, hased_password)
