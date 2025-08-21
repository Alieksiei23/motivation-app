from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from databases import Base, Letters, Users, setting


sync_engine = create_engine(
    url=setting.sync_url_db,
    echo=True
)
async_engine = create_async_engine(
    url=setting.async_url_db,
    echo=True
)
session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)


Base.metadata.drop_all(sync_engine)
Base.metadata.create_all(sync_engine)

async def insert_data():
    async with async_session() as sess:
        letter1 = Letters(letter='fasfasf')
        letter2 = Letters(letter='dsfdas')
        sess.add_all([letter1, letter2])
        await sess.commit()
