import uvicorn
from fastapi import FastAPI
import router
from db.config import engine, Base

Base.metadata.create_all(engine)

app = FastAPI(title="Recepts")
app.include_router(router.router)

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
