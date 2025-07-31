import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.backend.db import get_session
from app.users.models import User
from app.users.schemas import UserBase, UserRead, UserUpdate

router = APIRouter(
    prefix="/users",
    tags=["tguse"])



@router.get("/get_user", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(get_session)):
    """Получение всех пользователей"""
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


@router.get("/{user_id}", response_model=UserRead)
async def get_users(user_id: int, session: AsyncSession = Depends(get_session)):
    """Получение пользователей по id"""
    time.sleep(0.1)
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, payload: UserUpdate,session: AsyncSession = Depends(get_session)
):
    time.sleep(0.1)
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data = payload.model_dump(exclude_unset=True)  # Pydantic v2
    for field, value in data.items():
        setattr(user, field, value)

    await session.commit()
    await session.refresh(user)
    return user

