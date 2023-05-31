from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
from db.schemas.recepts import ReceptSchema

router = APIRouter()


@router.post("/add")
async def add_recept(recept: ReceptSchema):
    _recept = crud.create_recept(recept.title, recept.description,
                                 recept.ingredients,
                                 recept.steps_cooking)
    return _recept


@router.get("/")
async def get_all_recept():
    _recept = crud.get_recept()
    return _recept


@router.get("/{recept_id}")
async def get_recept(recept_id: int):
    _recept = crud.get_recept_by_id(recept_id)
    return _recept


@router.put("/edit/{recept_id}")
async def edit_recept(recept_id: int, recept: ReceptSchema):
    _recept = crud.update_recept(recept_id, recept.title,
                                 recept.description, recept.ingredients,
                                 recept.steps_cooking)
    return _recept


@router.delete("/delete/{recept_id}")
async def delete_recept(recept_id: int):
    crud.remove_recept(recept_id=recept_id)
    return "Recept was deleted..."
