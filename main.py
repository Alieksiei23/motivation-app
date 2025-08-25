import uvicorn
import asyncio
from fastapi import FastAPI

from views import router as router_views
from databases import router as router_database
from sending import router as router_send
from sending import get_all_mail

app = FastAPI()
app.include_router(router_database)
app.include_router(router_views)
app.include_router(router_send)






if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
