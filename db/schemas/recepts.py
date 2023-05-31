from pydantic import BaseModel


class ReceptSchema(BaseModel):
    title: str
    description: str
    ingredients: str
    steps_cooking: str

    class Config:
        orm_mode = True
