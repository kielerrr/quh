from sqlalchemy.orm import Session, Query
from . import models, schemas


def create_vendor(db: Session, vendor: schemas.VendorCreate):
	db_vendor = models.Vendor(sfy_id=vendor.sfy_id, afy_id=vendor.afy_id, sku=vendor.sku)
	db.add(db_vendor)
	db.commit()
	db.refresh(db_vendor)
	return db_vendor


def get_vendors(db: Session, skip: int = 0, limit: int = 250):
	return db.query(models.Vendor).offset(skip).limit(limit).all()


def get_missing_vendors(db: Session, sfy_vendors=None):
	missing_vendors = []
	if sfy_vendors is None:
		sfy_vendors = []
	for vendor in sfy_vendors:
		print('looking for sfy vendors missing in db')
		if db.query(models.AffMap).filter(models.AffMap.sfy_id == vendor).first():
			continue
		else:
			print('found missing vendor ', vendor)
			missing_vendors.append(vendor)
			
			
	print('missing vendors in db ', missing_vendors)
	if len(missing_vendors) > 0:
		return missing_vendors
	else:
		return ["All Vendors accounted for. Nice work!"]
	 
	


def get_vendor_skus(db: Session, sfy_id: str):
	print(db.query(models.Vendor.sku).filter(models.Vendor.sfy_id == sfy_id).all())
	return db.query(models.Vendor.sku).filter(models.Vendor.sfy_id == sfy_id).all()


def get_db_skus(db: Session, skip: int = 0, limit: int = 250, sfy_id: str = '0'):
	skus = db.query(models.Vendor.sku).filter(models.Vendor.sfy_id == sfy_id).offset(skip).limit(limit).all()
	return [sku['sku'] for sku in skus]


def delete_vendor(db, vendor: schemas.VendorDelete):
	db_vendor = db.query(models.Vendor).filter(models.Vendor.sfy_id == vendor.sfy_id).first()
	db.delete(db_vendor)
	db.commit()
	# db.refresh(db_vendor)
	return db_vendor


def update_sku_affmap(db: Session, affmap: schemas.AffMapUpdate):
	print('aaaa', affmap.skus)
	
	db_affmap = models.AffMap(
			id=affmap.id,
			sfy_id=affmap.sfy_id,
			afy_id=affmap.afy_id,
			skus=affmap.skus)
	
	# affmap_data = affmap.dict(exclude_unset=True)
	affmap_data = {
			'sfy_id': affmap.sfy_id,
			'afy_id': affmap.afy_id,
			'skus'  : affmap.skus,
			'id': affmap.id,
			}
	for key, value in affmap_data.items():
		setattr(db_affmap, key, value)
	db.commit()
	# db.refresh(db_affmap)
	return affmap


def get_affmap(db: Session, skip: int = 0, limit: int = 250):
	return db.query(models.AffMap).offset(skip).limit(limit).all()


def delete_affmap(db, affmap: schemas.AffMapDelete):
	dbn_affmap = db.query(models.AffMap).filter(models.AffMap.sfy_id == affmap.sfy_id).first()
	db.delete(dbn_affmap)
	db.commit()
	# db.refresh(dbn_affmap)
	return affmap


def get_affmap_one(db: Session, sfy_id: str):
	return db.query(models.AffMap).filter(models.AffMap.sfy_id == sfy_id).first()


def create_affmap_one(db: Session, affmap: schemas.AffMapCreate):
	db_affmap = models.AffMap(sfy_id=affmap.sfy_id, afy_id=affmap.afy_id,skus=affmap.skus)
	db.add(db_affmap)
	db.commit()
	# db.refresh(db_affmap)
	return affmap
