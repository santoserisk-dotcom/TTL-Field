from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "TTL Field API"
    environment: str = "development"
    database_url: str = "postgresql+asyncpg://ttl:ttl@db:5432/ttl_field"
    jwt_secret: str = "change-me"
    jwt_algorithm: str = "HS256"
    traccar_base_url: str = "http://traccar:8082"


settings = Settings()
