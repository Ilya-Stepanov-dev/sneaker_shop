from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import settings

Base = declarative_base()

class DataBaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10,
    ):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )

        self.session_factory = async_sessionmaker(
            bind=url,
            autoflush=False,
            expire_on_commit=False,
        )
        
    async def dispose(self):
        await self.engine.dispose()

    
    async def get_session(self):
        async with self.session_factory() as session:
            yield session
    
database_helper = DataBaseHelper(
    url=settings.db.url,
    echo=settings.orm.echo,
    pool_size=settings.orm.pool_size,
    max_overflow=settings.orm.max_overflow,
)