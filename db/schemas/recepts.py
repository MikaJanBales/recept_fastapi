from pydantic import BaseModel


class ReceptSchema(BaseModel):
    id: int
    title: str
    description: str
    ingredients: str
    steps_cooking: str

    class Config:
        orm_mode = True
