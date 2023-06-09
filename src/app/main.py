import logging

from fastapi import FastAPI, Depends
from tortoise.contrib.fastapi import register_tortoise

from app.config import get_settings, Settings


from app.api import  summary
from app.db import init_db


log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(summary.router, prefix="/summary", tags=["summary"])

    return application


app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")