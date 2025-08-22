from sqlalchemy import select
from fastapi import APIRouter, HTTPException
from datetime import datetime

from core import SessionDep, engine
from databases.models import AddUser, Admin
from databases.scheme import Base, Users, Letters


router = APIRouter(tags=['работа с базой данных'], prefix='/database')


@router.post('/tables/')
async def create_tables(admin: Admin):
    if admin.username == 'admin' and admin.password == 'admin':
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
        return {
            "create tables": "success"
        }
    else:
        raise HTTPException(status_code=402, detail='Authorization error, incorrect login or password.')

@router.post('/registration/')
async def add_user(user: AddUser, session: SessionDep):
    new_user = Users(
        username=user.username,
        password=user.password,
        email=user.email,
        date_start=datetime.now()
    )
    session.add(new_user)
    await session.commit()
    return {'user commit': 'success'}


@router.get('/users/')
async def get_all_users(session: SessionDep):
    query = select(Users)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/letters/')
async def get_all_letters(session: SessionDep):
    query = select(Letters)
    result = await session.execute(query)
    return result.scalars().all()