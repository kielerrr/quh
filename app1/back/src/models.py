from sqlalchemy import Column, Integer, String
from .database import Base


class Vendor(Base):
	__tablename__ = "vendors"
	
	id = Column(Integer, primary_key=True, index=True)
	sfy_id = Column(String, index=True)
	afy_id = Column(String, index=True)
	sku = Column()


class AffMap(Base):
	__tablename__ = "affmap"
	
	id = Column(Integer, primary_key=True, index=True)
	sfy_id = Column(String)
	afy_id = Column(String)
	skus = Column(String)
	
	
