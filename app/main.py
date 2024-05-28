from fastapi import FastAPI
from routes.libros import libro

app = FastAPI()

app.include_router(libro)