from sqlalchemy.orm import Session

from db.models.recepts import Recept


# Получение списка всех рецептов из бд
def get_recept(db: Session):
    return db.query(Recept).order_by(Recept.id.desc()).all()


# Получение информации о конкретном рецепте по ID из бд
def get_recept_by_id(db: Session, recept_id: int):
    return db.query(Recept).filter(Recept.id == recept_id).first()


# Создание нового рецепта в бд
def create_recept(db: Session, title: str, description: str,
                  ingredients: str, steps_cooking: str):
    _recept = Recept(title=title, description=description, ingredients=ingredients,
                     steps_cooking=steps_cooking)
    db.add(_recept)
    db.commit()
    db.refresh(_recept)
    return _recept


# Удаление рецепта по ID из бд
def remove_recept(db: Session, recept_id: int):
    _recept = get_recept_by_id(db, recept_id)
    db.delete(_recept)
    db.commit()
    db.close()


# Редактирование рецепта по ID из бд
def update_recept(db: Session, recept_id: int, title: str, description: str, ingredients: str, steps_cooking: str):
    _recept = get_recept_by_id(db=db, recept_id=recept_id)
    _recept.title = title
    _recept.description = description
    _recept.ingredients = ingredients
    _recept.steps_cooking = steps_cooking

    db.commit()
    db.refresh(_recept)
    return _recept
