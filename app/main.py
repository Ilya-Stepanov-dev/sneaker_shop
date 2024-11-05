import uvicorn
from fastapi import FastAPI

from config import settings 
from routers.user import router as user_router

app = FastAPI(
    prefix=settings.api.prefix
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = settings.uvicorn.host,
        port = settings.uvicorn.port,
        reload = settings.uvicorn.run_reload,
    )