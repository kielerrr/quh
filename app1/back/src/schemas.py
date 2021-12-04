from pydantic import BaseModel


class VendorBase(BaseModel):
	sfy_id: str
	afy_id: str
	sku: str


class Vendor(VendorBase):
	id: int
	
	class Config:
		orm_mode = True


class VendorCreate(VendorBase):
	pass


class VendorDelete(BaseModel):
	sfy_id: str



class AffMapBase(BaseModel):
	sfy_id: str
	afy_id: str
	skus: str


class AffMap(AffMapBase):
	id: int
	
	class Config:
		orm_mode = True
	
	

class AffMapCreate(AffMapBase):
	pass


class AffMapDelete(BaseModel):
	sfy_id: str


class AffMapUpdate(AffMap):
	pass
