from sqlalchemy import select

from db.models.recepts import Recept
from db.config import db as session


# Получение списка всех рецептов из бд
async def get_recept():
    recept = await session.execute(select(Recept).order_by(Recept.id.desc()))
    return recept.scalars().all()


# Получение информации о конкретном рецепте по ID из бд
async def get_recept_by_id(recept_id: int):
    recept = await session.execute(
        select(Recept).filter(Recept.id == recept_id))
    return recept.scalars().first()


# Создание нового рецепта в бд
async def create_recept(title: str, description: str,
                        ingredients: str, steps_cooking: str):
    _recept = Recept(title=title, description=description,
                     ingredients=ingredients,
                     steps_cooking=steps_cooking)
    session.add(_recept)
    await session.commit()
    await session.refresh(_recept)
    return _recept


# Удаление рецепта по ID из бд
async def remove_recept(recept_id: int):
    _recept = await get_recept_by_id(recept_id)
    await session.delete(_recept)
    await session.commit()


# Редактирование рецепта по ID из бд
async def update_recept(recept_id: int, title: str, description: str,
                        ingredients: str, steps_cooking: str):
    _recept = await get_recept_by_id(recept_id=recept_id)
    _recept.title = title
    _recept.description = description
    _recept.ingredients = ingredients
    _recept.steps_cooking = steps_cooking

    await session.commit()
    await session.refresh(_recept)
    return _recept
