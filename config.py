from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Smart Home API"
    app_env: str = "dev"
    debug: bool = False

    db_user: str = "app_user"
    db_password: str = "secret"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "smart_home_db"
    db_echo: bool = False

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


settings = Settings()