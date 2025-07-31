from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

# Создаём движок для асинхронного подключения к PostgreSQL
engine = create_async_engine(
    'postgresql+asyncpg://embrass:StrongPass123@localhost:5432/tg',
    echo=True
)

# Фабрика сессий
async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Базовый класс для моделей
class Base(DeclarativeBase):
    pass

# Зависимость для FastAPI — получение сессии
async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
