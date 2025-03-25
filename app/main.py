from fastapi import FastAPI
from app.database.init_db import init_db

app = FastAPI()

# Ejecutar la inicialización al arrancar
@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def read_root():
    return {"mensaje": "API BOST_HORARIOS funcionando ✅"}
