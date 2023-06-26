from database import create_db_and_tables
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import authentication, requests, songs, users

app = FastAPI()
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(requests.router)
app.include_router(songs.router)


@app.on_event("startup")
async def startup():
    create_db_and_tables()


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
