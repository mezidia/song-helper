from database import create_db_and_tables
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import authentication, requests, users

app = FastAPI(
    title="SongHelper API",
    description="API for SongHelper",
    version="0.1.0",
    contact={
        "name": "mezgoodle",
        "url": "https://github.com/mezgoodle",
        "email": "mezgoodle@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://github.com/mezidia/song-helper/blob/master/LICENSE",
    },
)
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(requests.router)


@app.on_event("startup")
async def startup():
    create_db_and_tables()


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
