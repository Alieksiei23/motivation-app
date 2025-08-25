from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    DB_PASS: str
    DB_USER: str
    EMAIL_PASSWORD: str
    LOGIN: str

    @property
    def async_url_db(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


setting = Settings()


engine = create_async_engine(
    url=setting.async_url_db,
    echo=True
)
new_session = async_sessionmaker(engine)


async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]

