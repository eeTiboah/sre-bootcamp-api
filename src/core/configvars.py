
from pydantic import BaseSettings


class EnvConfig(BaseSettings):
    DB_NAME: str = "NOT REAL DB NAME"
    DB_USER: str = "NOT THE REAL DB USER"
    DB_PASSWORD: str = "NOT THE REAL DB PASSWORD"
    DB_PORT: str = "DB PORT"
    

    class Config:
        env_file = ".env"


env_config = EnvConfig()