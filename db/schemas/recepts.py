from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class ReceptSchema(BaseModel):
    id: int
    title: str
    description: str
    ingredients: str
    steps_cooking: str

    class Config:
        orm_mode = True


class RequestRecept(BaseModel):
    parameter: ReceptSchema = Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]