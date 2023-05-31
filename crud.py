from db.models.recepts import Recept
# from db.models.users import NewUser
# from db.schemas.users import CreateUserSchema
from db.config import db as session


# def create_user(session: Session, user: CreateUserSchema):
#     db_user = NewUser(**user.dict())
#     session.add(db_user)
#     session.commit()
#     session.refresh(db_user)
#     return db_user
#
#
# def get_user(session: Session, email: str):
#     return session.query(NewUser).filter(NewUser.email == email).one()
#
#
# def get_user_by_id(session: Session, id: int):
#     return session.query(NewUser).filter(NewUser.id == id).one()
#
#
# def list_users(session: Session):
#     return session.query(NewUser).all()


# Получение списка всех рецептов из бд
def get_recept():
    return session.query(Recept).order_by(Recept.id.desc()).all()


# Получение информации о конкретном рецепте по ID из бд
def get_recept_by_id(recept_id: int):
    return session.query(Recept).filter(Recept.id == recept_id).first()


# Создание нового рецепта в бд
def create_recept(title: str, description: str,
                  ingredients: str, steps_cooking: str):
    _recept = Recept(title=title, description=description,
                     ingredients=ingredients,
                     steps_cooking=steps_cooking)
    session.add(_recept)
    session.commit()
    session.refresh(_recept)
    return _recept


# Удаление рецепта по ID из бд
def remove_recept(recept_id: int):
    _recept = get_recept_by_id(recept_id)
    session.delete(_recept)
    session.commit()
    session.close()


# Редактирование рецепта по ID из бд
def update_recept(recept_id: int, title: str, description: str,
                  ingredients: str, steps_cooking: str):
    _recept = get_recept_by_id(recept_id=recept_id)
    _recept.title = title
    _recept.description = description
    _recept.ingredients = ingredients
    _recept.steps_cooking = steps_cooking

    session.commit()
    session.refresh(_recept)
    return _recept
