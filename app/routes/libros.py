from fastapi import APIRouter, status, Depends, Response
from bson import ObjectId
from models.libros import Libros
from config.database import conn
from schemas.libros import libroEntity, librosEntity, serializeDict, serializeList

libro = APIRouter()

@libro.get('/', status_code= status.HTTP_200_OK)
async def find_all_libros():
	return serializeList(conn.local.libros.find())

@libro.get('/{id}', status_code= status.HTTP_200_OK)
async def find_one_Libro(id):
	return serializeDict(conn.local.libros.find_one({"_id": ObjectId(id)}))

@libro.post('/', status_code= status.HTTP_201_CREATED)
async def create_libro(libro: Libros):
	conn.local.libros.insert_one(dict(libro))
	return librosEntity(conn.local.libros.find())


@libro.put('/{id}', status_code= status.HTTP_200_OK)
async def update_libro(id, libro: Libros):
	conn.local.libros.find_one_and_update(
		{"_id": ObjectId(id)}, {
			"$set":dict(libro)
		}
	)
	return libroEntity(conn.local.libros.find_one({"_id": ObjectId(id)}))

@libro.delete('/{id}', status_code= status.HTTP_200_OK)
async def delete_libro(id, libro: Libros):
	return libroEntity(
		conn.local.libros.find_one_and_delete({"_id": ObjectId(id)})
	)
