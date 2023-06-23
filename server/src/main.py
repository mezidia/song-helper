from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import authentication, requests, songs, users

app = FastAPI()
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(requests.router)
app.include_router(songs.router)


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
