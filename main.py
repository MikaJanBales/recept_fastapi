import uvicorn
from fastapi import FastAPI
import router
from db.config import engine, Base

Base.metadata.create_all(engine)

app = FastAPI(title="Recepts")

# app.secret_key = os.urandom(24)


app.include_router(router.router, prefix="/recept", tags=["recept"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)