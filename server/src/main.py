from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import authentication, users

app = FastAPI()
app.include_router(users.router)
app.include_router(authentication.router)


@app.get("/")
async def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
