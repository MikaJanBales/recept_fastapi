from sqlalchemy import Integer, Column, String, Text

from db.config import Base


class Recept(Base):
    __tablename__ = "recept"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    ingredients = Column(String(100), nullable=False)
    steps_cooking = Column(Text, nullable=False)

    def __repr__(self):
        return f'<Recept "{self.name}">'