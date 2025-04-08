from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

env_file = Path(__file__).parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_file
    )

    BASE_PATH: str
    FASTAPI_HOST: str
    FASTAPI_PORT: int


settings = Settings()
