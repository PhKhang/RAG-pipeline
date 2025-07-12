# import asyncio
# from typing import Union

from fastapi import FastAPI
from .routers import chat

app = FastAPI(swagger_ui_parameters={"displayRequestDuration ": True})


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(chat.router)

@app.get("/health")
def health_check():
    return {"status": "healthy"}