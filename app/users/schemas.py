from pydantic import BaseModel

# Базовая схема
class UserBase(BaseModel):
    name: str
    usernametg: str
    category: str

# Схема для чтения (ответ API)
class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
        # позволяет конвертировать SQLAlchemy модель -> Pydantic


class UserUpdate(BaseModel):
    name: str | None = None
    usernametg: str | None = None
    category: str | None = None