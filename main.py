import uvicorn
from fastapi import FastAPI
from db.config import Base, engine
from views import router

Base.metadata.create_all(engine)

app = FastAPI(title="Recepts", docs_url="/", redoc_url=None)

app.include_router(router, prefix="", tags=["recept"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
