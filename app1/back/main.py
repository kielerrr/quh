import json
from typing import List, Dict

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine
import uvicorn
import json



models.Base.metadata.create_all(bind=engine)


def create_db_and_tables():
	models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.on_event("startup")
def on_startup():
	create_db_and_tables()


origins = [
		# "*"
		# "http://localhost",
		# "http://localhost:3400",
		]

app.add_middleware(
		CORSMiddleware,
		allow_origins=origins,
		# allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
		)


# Dependency
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.get("/vendors_missing/", response_model=List)
def read_vendors(db: Session = Depends(get_db)):
	# url = "https://XXXXXXXX.myshopify.com/admin/api/graphql.json"
	# payload = "{\"query\":\"\\nquery productVendors {\\n  shop {\\n    productVendors(first: 250) {\\n      edges {\\n        node\\n      }\\n    }\\n  }\\n}\\n\\n# query test {\\n#     products(first: 50) {\\n#       edges {\\n#         node {\\n#           handle\\n#           vendor\\n#           variants(first: 10) {\\n#             edges {\\n#               node {\\n#                 sku\\n#               }\\n#             }\\n#           }\\n#         }\\n#       }    \\n#   }\\n# }\",\"operationName\":\"productVendors\"}"
	# headers = { 'X-Shopify-Access-Token': "shppa_XXXXXXXXXXXXXXXXXXXXXXXX", 'Content-Type': "application/json" }
	# response = requests.request("POST", url, data=payload, headers=headers)
	
	mock_response = """{ "data": { "shop": { "productVendors": { "edges": [ { "node": "Adventures of Kiel" }, { "node": "Alexa Kiel" }, { "node": "Allie Kiel" }, { "node": "Ava Kiel" }, { "node": "Bethany Strickland Kiel" }, { "node": "Betty Kiel" }, { "node": "Bev Kiel" }, { "node": "Chloe Kiel" }, { "node": "Christina Kiel" }, { "node": "Connor Kiel" }, { "node": "Doug Kiel" }, { "node": "Foterra Kiel" }, { "node": "Foterra Kiel" }, { "node": "Frank Kiel" }, { "node": "Kiel" }, { "node": "Hanna Kiel" }, { "node": "Heather Kiel" }, { "node": "Heather Kiel" }, { "node": "Jaclynn Kiel" }, { "node": "Jan Kiel" }, { "node": "Jen Kiel" }, { "node": "Jen Kiel" }, { "node": "John Baran Kiel" }, { "node": "John Kiel" }, { "node": "Josh Kiel" }, { "node": "Kelli Kiel" }, { "node": "Kelly Kiel" }, { "node": "Kelly Kiel" }, { "node": "Kerry Kiel" }, { "node": "La Vida in Life Kiel" }, { "node": "Lauren Kiel" }, { "node": "Merr Kiel" }, { "node": "Morgan Lane-Kiel" }, { "node": "Morgan's Kiel" }, { "node": "Seth Kiel" }, { "node": "Tiffany Briley | A Quest For Kiel" }, { "node": "Trevor Kiel" }, { "node": "Vince Kiel" }, { "node": "jess Kiel" } ] } } }, "extensions": { "cost": { "requestedQueryCost": 2, "actualQueryCost": 2, "throttleStatus": { "maximumAvailable": 1000.0, "currentlyAvailable": 998, "restoreRate": 50.0 } } } }"""
	
	parsed_vendors = json.loads(mock_response)
	list_vendors = parsed_vendors['data']['shop']['productVendors']['edges']
	sfy_vendors =  [strr['node'] for strr in list_vendors]
	missing_vendors = crud.get_missing_vendors(db, sfy_vendors)
	
	return missing_vendors



@app.get("/vendors/", response_model=List[schemas.Vendor])
def read_vendors(skip: int = 0, limit: int = 250, db: Session = Depends(get_db)):
	vendors = crud.get_vendors(db, skip=skip, limit=limit)
	if vendors is None:
		raise HTTPException(status_code=404, detail="Vendorss not found")
	return vendors


@app.get("/vendor/{sfy_id}/")
def get_vendor_skus(sfy_id: str, db: Session = Depends(get_db)):
	db_vendor = crud.get_vendor_skus(db, sfy_id=sfy_id)
	if db_vendor is None:
		raise HTTPException(status_code=404, detail="Vendor not found")
	return db_vendor


@app.get("/db_skus/{sfy_id}/")
def get_db_skus(sfy_id: str, db: Session = Depends(get_db)):
	db_vendor = crud.get_db_skus(db, sfy_id=sfy_id)
	if db_vendor is None:
		raise HTTPException(status_code=404, detail="Vendor not found, cant find skus")
	return db_vendor


@app.post("/vendor/", response_model=schemas.Vendor)
def create_vendor(vendor: schemas.VendorCreate, db: Session = Depends(get_db)):
	# db_vendor = crud.get_vendor_skus(db, sfy_id=vendor.sfy_id)
	# if db_vendor:
	# 	raise HTTPException(status_code=400, detail="Vendor already have this vendor")
	return crud.create_vendor(db=db, vendor=vendor)


@app.delete("/vendor/{sfy_id}/")
def delete_vendor(sfy_id: str, vendor: schemas.VendorDelete, db: Session = Depends(get_db)):
	vendor.sfy_id = sfy_id
	db_vendor = crud.get_vendor_skus(db, sfy_id=vendor.sfy_id)
	if db_vendor is None:
		raise HTTPException(status_code=404, detail="Vendor to delete not found")
	return crud.delete_vendor(db=db, vendor=vendor)




@app.get("/affmap/"
		 # , response_model=List[schemas.AffMap]
		 )
def read_affmap(skip: int = 0, limit: int = 250, db: Session = Depends(get_db)):
	affmap = crud.get_affmap(db, skip=skip, limit=limit)
	if affmap is None:
		raise HTTPException(status_code=404, detail="Vendors not found")
	return affmap


@app.get("/affmap/{sfy_id}/", response_model=schemas.AffMap)
def get_affmap_one(sfy_id: str, db: Session = Depends(get_db)):
	try:
		db_affmap = crud.get_affmap_one(db, sfy_id=sfy_id)
		if db_affmap is None:
			raise HTTPException(status_code=404, detail="Affmap not found")
		db_affmap = {
				'id'    : db_affmap.id,
				'sfy_id': db_affmap.sfy_id,
				'afy_id': db_affmap.afy_id,
				'skus'  : db_affmap.skus
				}
		return db_affmap
	
	except Exception as e:
		return {
				'sfy_id': '999999',
				'afy_id': '999999',
				'sku'   : '999999',
				'id'    : 9999
				}


@app.patch("/affmap/", response_model=schemas.AffMap)
def update_affmap(affmap: schemas.AffMap, db: Session = Depends(get_db)):
	db_affmap = crud.get_affmap_one(db, sfy_id=affmap.sfy_id)
	# db_affmap.skus = crud.get_db_skus(db, sfy_id=affmap.sfy_id)
	db_affmap.skus = affmap.skus
	if db_affmap is None:
		raise HTTPException(status_code=404, detail="Vendor not found in AffMap")
	return crud.update_sku_affmap(db=db, affmap=db_affmap)


@app.delete("/affmap/{sfy_id}/")
def delete_affmap(sfy_id: str, affmap: schemas.AffMapDelete, db: Session = Depends(get_db)):
	affmap.sfy_id = sfy_id
	db_affmap = crud.get_affmap_one(db, sfy_id=affmap.sfy_id)
	if db_affmap is None:
		raise HTTPException(status_code=404, detail="Vendor to delete not found")
	return crud.delete_affmap(db=db, affmap=affmap)


@app.post("/affmap/", response_model=schemas.AffMapCreate)
def create_affmap(affmap: schemas.AffMapCreate, db: Session = Depends(get_db)):
	db_affmap = crud.get_affmap_one(db, sfy_id=affmap.sfy_id)
	if db_affmap:
		raise HTTPException(status_code=400, detail="Affmap  already have this affmap")
	return crud.create_affmap_one(db=db, affmap=affmap)


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=5000, log_level="trace",
				# ssl_certfile="etc/keys/c1",
				# ssl_keyfile="etc/keys/k1",
				interface="asgi3", ssl_cert_reqs=0, ssl_ca_certs="etc/keys/combined")
