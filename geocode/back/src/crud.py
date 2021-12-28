from . import schemas, database

db = database.db


def create_nad(nad: schemas.NadCreate, cur_db: database.MongoClient = db):
	if hasattr(nad, 'id'):
		delattr(nad, 'id')
	ret = cur_db.nad.insert_one(nad.dict(by_alias=True))
	nad.id = ret.inserted_id
	return nad


def get_xyzs(skip: int = 0, limit: int = 250, xyzs=None, cur_db: database.MongoClient = db):
	hits = cur_db.find(
			{
					"$and": [
							{
									"Latitude": {
											"$gt": f"{xyzs.south}",
											"$lt": f"{xyzs.north}",
											}
									},
							{
									"Longitude": {
											"$gt": f"{xyzs.west}",
											"$lt": f"{xyzs.east}",
											}
									}
							]
					}
			)
	
	x = [hit for hit in hits]
	return x[1:250]


def get_nad_one(db: database.MongoClient, nad_id: str):
	return db.find(schemas.Nad).filter(schemas.Nad.nad_id == nad_id).first()


def get_nads(skip: int = 0, limit: int = 250):
	return db.find({ })


def delete_nad(db, nad: schemas.NadDelete):
	nad = db.query(schemas.Nad).filter(schemas.Nad.nad_id == nad.nad_id).first()
	db.delete(nad)
	db.commit()
	return nad


def update_nad(db: database.MongoClient, nad: schemas.NadUpdate):
	print('aaaa', nad.skus)
	
	db_nad = schemas.Nad(
			id=nad.id,
			nad_id=nad.nad_id,
			afy_id=nad.afy_id,
			skus=nad.skus)
	
	# nad_data = nad.dict(exclude_unset=True)
	nad_data = {
			'nad_id': nad.nad_id,
			'afy_id': nad.afy_id,
			'skus'  : nad.skus,
			'id'    : nad.id,
			}
	for key, value in nad_data.items():
		setattr(db_nad, key, value)
	db.commit()
	# db.refresh(db_nad)
	return nad
