from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
from db.config import SessionLocal
from db.schemas.recepts import ReceptSchema

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
async def add_recept(recept: ReceptSchema, db: Session = Depends(get_db)):
    _recept = crud.create_recept(db, recept.title, recept.description, recept.ingredients,
                                 recept.steps_cooking)
    return _recept


@router.get("/")
async def get_all_recept(db: Session = Depends(get_db)):
    _recept = crud.get_recept(db)
    return _recept


@router.get("/{recept_id}")
async def get_recept(recept_id: int, db: Session = Depends(get_db)):
    _recept = crud.get_recept_by_id(db, recept_id)
    return _recept


@router.put("/edit/{recept_id}")
async def edit_recept(recept_id: int, recept: ReceptSchema, db: Session = Depends(get_db)):
    _recept = crud.update_recept(db, recept_id, recept.title, recept.description, recept.ingredients,
                                 recept.steps_cooking)
    return _recept


@router.delete("/delete/{recept_id}")
async def delete_recept(recept_id: int, db: Session = Depends(get_db)):
    crud.remove_recept(db, recept_id=recept_id)
    return "Recept was deleted..."
