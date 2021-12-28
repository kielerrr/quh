import json
from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from .src import crud, schemas
import json

# def create_db_and_tables():
#     models.Base.metadata.create_all(bind=engine)
app = FastAPI()
# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()
origins = [
		# "*"
		# "http://localhost",
		# "http://localhost:3400",
		]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"], )
		# allow_origins=["*"],


@app.post("/xyzs/", response_model=List[schemas.NadAddress])
def read_nads(xyzs: schemas.Xyzs, skip: int = 0, limit: int = 250):
	if xyzs is None:
		xyzs = { }
	nads = crud.get_xyzs(skip=skip, limit=limit, xyzs=xyzs)
	if nads is None:
		raise HTTPException(status_code=404, detail="Nadss not found")
	return nads


@app.get("/nad/", response_model=schemas.NadBase)
def get_one():
	try:
		db_nad = crud.get_nad_one(nad_id=nad_id)
		if db_nad is None:
			raise HTTPException(status_code=404, detail="Nad not found")
		db_nad = {
				'id'    : db_nad.id,
				}
		return db_nad
	
	except Exception as e:
		return {
				'nad_id': '999999',
				}


@app.get('/nadsSSS/', response_model=List[schemas.Nad])
async def list_nads():
	# return ['DDDast']
	# nads = crud.get_nads(skip=skip, limit=limit)
	nads = crud.get_nads()
	if nads is None:
		raise HTTPException(status_code=404, detail="Nads not found")
	return [nad for nad in nads]


@app.post('/nad/')
async def create_nad(nad: schemas.NadCreate):
	if hasattr(nad, 'id'):
		delattr(nad, 'id')
	ret = db.nad.insert_one(nad.dict(by_alias=True))
	nad.id = ret.inserted_id
	return { 'nad': nad }


@app.post("/nad/", response_model=schemas.NadCreate)
def create_nad(nad: schemas.NadCreate):
	db_nad = crud.get_nad_one(nad_id=nad.nad_id)
	if db_nad:
		raise HTTPException(status_code=400, detail="Nad  already have this nad")
	return crud.create_nad(nad=nad)


@app.delete("/nad/{nad_id}/")
def delete_nad(nad_id: str, nad: schemas.NadDelete):
	nad.nad_id = nad_id
	db_nad = crud.get_nad_one(nad_id=nad.nad_id)
	if db_nad is None:
		raise HTTPException(status_code=404, detail="Nad to delete not found")
	return crud.delete_nad(nad=nad)


@app.patch("/nad/", response_model=schemas.Nad)
def update_nad(nad: schemas.Nad):
	db_nad = crud.get_nad_one(nad_id=nad.nad_id)
	# db_nad.skus = crud.get_db_skus(db, nad_id=nad.nad_id)
	db_nad.skus = nad.skus
	if db_nad is None:
		raise HTTPException(status_code=404, detail="Nad not found in Nad")
	return crud.update_nad(nad=db_nad)


if __name__ == "__main__":
	uvicorn.run(app,
				host="0.0.0.0",
				port=5000,
				log_level="trace",
				# ssl_certfile="etc/keys/c1",
				# ssl_keyfile="etc/keys/k1",
				interface="asgi3",
				ssl_cert_reqs=0,
				ssl_ca_certs="etc/keys/combined")
