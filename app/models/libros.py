from pydantic import BaseModel

class Libros(BaseModel):
	titulo: str
	autor: str
	genero: str