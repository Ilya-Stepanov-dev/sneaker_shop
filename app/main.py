import uvicorn
from fastapi import FastAPI

from config import settings 
from routers.user import router as user_router

app = FastAPI(
    prefix='/api/v1'
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = settings.main.host,
        port = settings.main.port,
        reload = settings.main.run_reload,
    )

