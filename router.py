from fastapi import APIRouter, Depends, Form, status, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
import crud
from db.config import SessionLocal

router = APIRouter()

templates = Jinja2Templates(directory="templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add")
async def add(request: Request, title: str = Form(...), description: str = Form(...),
              ingredients: str = Form(...), steps_cooking: str = Form(...), db: Session = Depends(get_db)):
    crud.create_recept(db, title, description, ingredients, steps_cooking)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.get("/addnew")
async def addnew(request: Request):
    return templates.TemplateResponse("addnew.html", {"request": request})


@router.get("/")
async def get(request: Request, db: Session = Depends(get_db)):
    _recept = crud.get_recept(db)
    return templates.TemplateResponse("index.html", {"request": request, "recepts": _recept})


@router.get("/{recept_id}")
async def get_by_id(recept_id: int, db: Session = Depends(get_db)):
    _recept = crud.get_recept_by_id(db, recept_id)
    return _recept


# we will work
@router.get("/edit/{recept_id}")
async def edit(request: Request, recept_id: int, db: Session = Depends(get_db)):
    _recept = crud.get_recept_by_id(db, recept_id)
    return templates.TemplateResponse("edit.html", {"request": request, "recepts": _recept})


@router.post("/update/{recept_id}")
async def update(request: Request, recept_id: int, title: str = Form(...), description: str = Form(...),
                 ingredients: str = Form(...), steps_cooking: str = Form(...), db: Session = Depends(get_db)):
    crud.update_recept(db, recept_id, title, description, ingredients, steps_cooking)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


@router.delete("/delete/{recept_id}")
async def delete(request: Request, recept_id: int, db: Session = Depends(get_db)):
    crud.remove_recept(db, recept_id=recept_id)
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)
