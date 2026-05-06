from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI


@asynccontextmanager
async def asgi_lifespan(app: FastAPI) -> AsyncGenerator:
    yield
