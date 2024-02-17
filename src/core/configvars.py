from pydantic_settings import BaseSettings


class EnvConfig(BaseSettings):
    DB_NAME: str = "NOT REAL DB NAME"
    DB_USER: str = "NOT THE REAL DB USER"
    DB_PASSWORD: str = "NOT THE REAL DB PASSWORD"
    DB_PORT: str = "DB PORT"
    PRODUCTION_ENV: str = "prod db"
    DATABASE_URL: str = "db url"

    class Config:
        env_file = ".env"


env_config = EnvConfig()