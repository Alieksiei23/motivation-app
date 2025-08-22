import uvicorn

from fastapi import FastAPI

from views import router as router_views
from databases import router as router_database

app = FastAPI()
app.include_router(router_database)
app.include_router(router_views)







if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)