from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud
from db.config import SessionLocal
from db.schemas.recepts import RequestRecept, Response

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create(request: RequestRecept, db: Session = Depends(get_db)):
    crud.create_recept(db, recept=request.parameter)
    return Response(code=200, status="OK", message="Recept created successfully").dict(exclude_none=True)


@router.get("/")
async def get(db: Session = Depends(get_db)):
    _recept = crud.get_recept(db)
    return Response(code=200, status="OK", message="Success fetch all data", result=_recept).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id: int, db: Session = Depends(get_db)):
    _recept = crud.get_recept_by_id(db, id)
    return Response(code=200, status="OK", message="Success get data", result=_recept).dict(exclude_none=True)


@router.post("/update")
async def update_recept(request: RequestRecept, db: Session = Depends(get_db)):
    _recept = crud.update_recept(db, recept_id=request.parameter.id, title=request.parameter.title,
                                 description=request.parameter.description, ingredients=request.parameter.ingredients,
                                 steps_cooking=request.parameter.steps_cooking)
    return Response(code=200, status="OK", message="Success update data", result=_recept)


@router.delete("/{id}")
async def delete(id: int, db: Session = Depends(get_db)):
    crud.remove_recept(db, recept_id=id)
    return Response(code=200, status="OK", message="Success delete data").dict(exclude_none=True)
