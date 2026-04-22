from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    gigachat_api_key: str = ""
    yandex_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
