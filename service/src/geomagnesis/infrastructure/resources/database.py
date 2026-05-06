from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, registry

from src.geomagnesis.config import settings


def make_async_sessionmaker() -> async_sessionmaker[AsyncSession]:
    engine = create_async_engine(
        url=settings.postgresql_url,
        pool_size=settings.postgresql.POOL_SIZE,
        max_overflow=settings.postgresql.MAX_OVERFLOW,
        connect_args={
            "connect_timeout": settings.postgresql.CONNECTION_TIMEOUT,
        },
        echo=settings.postgresql.ECHO,
    )

    return async_sessionmaker(
        bind=engine,
        autoflush=settings.postgresql.AUTOFLUSH,
        expire_on_commit=settings.postgresql.EXPIRE_ON_COMMIT,
        class_=AsyncSession,
    )


class Base(DeclarativeBase):
    registry = registry()
