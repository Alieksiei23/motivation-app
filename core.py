from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from settings import setting


engine = create_async_engine(
    url=setting.async_url_db,
    echo=True
)
new_session = async_sessionmaker(engine)


async def get_session():
    async with new_session() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
