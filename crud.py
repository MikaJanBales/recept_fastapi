from sqlalchemy.orm import Session

from db.models.recepts import Recept
from db.schemas.recepts import ReceptSchema


# Получение списка всех рецептов
def get_recept(db: Session):
    return db.query(Recept).all()


# Получение информации о конкретном рецепте по ID
def get_recept_by_id(db: Session, recept_id: int):
    return db.query(Recept).filter(Recept.id == recept_id).first()


# Создание нового рецепта
def create_recept(db: Session, recept: ReceptSchema):
    _recept = Recept(title=recept.title, description=recept.description, ingredients=recept.ingredients,
                     steps_cooking=recept.steps_cooking)
    db.add(_recept)
    db.commit()
    db.refresh(_recept)
    return _recept


# Удаление рецепта по ID
def remove_recept(db: Session, recept_id: int):
    _recept = get_recept_by_id(db=db, recept_id=recept_id)
    db.delete(_recept)
    db.commit()


# Редактирование рецепта по ID
def update_recept(db: Session, recept_id: int, title: str, description: str, ingredients: str, steps_cooking: str):
    _recept = get_recept_by_id(db=db, recept_id=recept_id)
    _recept.title = title
    _recept.description = description
    _recept.ingredients = ingredients
    _recept.steps_cooking = steps_cooking

    db.commit()
    db.refresh(_recept)
    return _recept