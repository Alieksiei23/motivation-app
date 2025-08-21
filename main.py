import asyncio

import uvicorn
from fastapi import FastAPI

from core import insert_data


app = FastAPI()



@app.get('/', tags=['welcome page'])
def welcome():
    return {
        'Message': 'Hello, we are pleased to welcome you to the quotes app'
    }














if __name__ == '__main__':
    asyncio.run(insert_data())
    uvicorn.run('main:app', reload=True)