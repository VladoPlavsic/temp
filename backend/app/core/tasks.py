from typing import Callable
from fastapi import FastAPI

from app.db.tasks import connect_to_db, close_db_connection
from app.cdn.tasks import connect_to_cdn

def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        await connect_to_db(app)
        await connect_to_cdn(app)
  
    return start_app

def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        await close_db_connection(app)

    return stop_app
