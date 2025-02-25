def libroEntity(item) -> dict:
	return {
		"id": str(item["_id"]),
		"titulo": item["titulo"],
		"autor": item["autor"],
		"genero": ["genero"]
	}

def librosEntity(entity) -> list:
	return [librosEntity(item) for item in entity]

def serializeDict(a) -> dict:
	return {**{i:str(a[i]) for i in a if i == "_id" }, **{i:a[i] for i in a if i != "_id"}}

def serializeList(entity) -> list:
	return [serializeDict(a) for a in entity]