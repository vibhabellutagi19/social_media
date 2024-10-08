from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port:str
    db_username: str
    db_password: str
    db_name: str
    secret_key: str
    algorithm: str
    access_token_expiration_time: int = 30

    class Config:
        env_file = '.env'