import uvicorn
from fastapi import FastAPI
import router

app = FastAPI(title="Recepts")

app.include_router(router.router, prefix="/recept", tags=["recept"])

if __name__ == "__main__":
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
