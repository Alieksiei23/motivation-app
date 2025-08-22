from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_PASS: str
    DB_USER: str

    @property
    def sync_url_db(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def async_url_db(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


setting = Settings()
