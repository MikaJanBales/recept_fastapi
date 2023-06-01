from fastapi import APIRouter

import crud
from db.config import engine, Base
from db.schemas.recepts import ReceptSchema

router = APIRouter()


@router.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@router.post("/recept/add")
async def add_recept(recept: ReceptSchema):
    _recept = await crud.create_recept(recept.title, recept.description,
                                       recept.ingredients,
                                       recept.steps_cooking)
    return _recept


@router.get("/recept/get_all")
async def get_all_recept():
    _recept = await crud.get_recept()
    return _recept


@router.get("/recept/get_one/{recept_id}")
async def get_recept(recept_id: int):
    _recept = await crud.get_recept_by_id(recept_id)
    return _recept


@router.put("/recept/edit/{recept_id}")
async def edit_recept(recept_id: int, recept: ReceptSchema):
    _recept = await crud.update_recept(recept_id, recept.title,
                                       recept.description, recept.ingredients,
                                       recept.steps_cooking)
    return _recept


@router.delete("/recept/delete/{recept_id}")
async def delete_recept(recept_id: int):
    await crud.remove_recept(recept_id=recept_id)
    return "Recept was deleted..."
