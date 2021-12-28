from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional
from pymongo import MongoClient

client = MongoClient()
db = client['nad']


class PyObjectId(ObjectId):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate
	
	@classmethod
	def validate(cls, v):
		print('validating objectiddrrrrr')
		if not ObjectId.is_valid(v):
			raise ValueError('Invalid objectiddddddddddddd')
		return ObjectId(v)
	
	@classmethod
	def __modify_schema__(cls, field_schema):
		field_schema.update(type='string')


class Xyzs(BaseModel):
	north: float = 42.007002589771421      # lat lt
	south: float = 42.006002589771419      # lat gt
	
	
	east: float = 100     # lng lt
	west: float = -100      # lng gt
	#
	# east: float = - 78.897214858899000     # lng lt
	# west: float = -78.195214858890000      # lng gt
	#


class NadDelete(BaseModel):
	nad_id: str


	
class NadBase(BaseModel):
	OID_: Optional[str]
	State: Optional[str]
	County: Optional[str]
	Inc_Muni: Optional[str]
	Uninc_Comm: Optional[str]
	Nbrhd_Comm: Optional[str]
	Post_Comm: Optional[str]
	Zip_Code: Optional[str]
	Plus_4: Optional[str]
	Bulk_Zip: Optional[str]
	Bulk_Plus4: Optional[str]
	StN_PreMod: Optional[str]
	StN_PreDir: Optional[str]
	StN_PreTyp: Optional[str]
	StN_PreSep: Optional[str]
	StreetName: Optional[str]
	StN_PosTyp: Optional[str]
	StN_PosDir: Optional[str]
	StN_PosMod: Optional[str]
	AddNum_Pre: Optional[str]
	Add_Number: Optional[str]
	AddNum_Suf: Optional[str]
	LandmkPart: Optional[str]
	LandmkName: Optional[str]
	Building: Optional[str]
	Floor: Optional[str]
	Unit: Optional[str]
	Room: Optional[str]
	Addtl_Loc: Optional[str]
	Milepost: Optional[str]
	Longitude: Optional[str]
	Latitude: Optional[str]
	NatGrid_Coord: Optional[str]
	GUID: Optional[str]
	Addr_Type: Optional[str]
	Placement: Optional[str]
	Source: Optional[str]
	AddAuth: Optional[str]
	UniqWithin: Optional[str]
	LastUpdate: Optional[str]
	Effective: Optional[str]
	Expired: Optional[str]


class Nad(NadBase):
	id: Optional[PyObjectId] = Field(alias='_id')
	
	class Config:
		arbitrary_types_allowed = True
		json_encoders = {
				ObjectId: str
				}


class NadAddress(BaseModel):
	State: Optional[str]
	Inc_Muni: Optional[str]
	Zip_Code: Optional[str]
	StreetName: Optional[str]
	StN_PosTyp: Optional[str]
	Add_Number: Optional[str]
	Longitude: Optional[str]
	Latitude: Optional[str]
	Addr_Type: Optional[str]
	Placement: Optional[str]
	Source: Optional[str]
	AddAuth: Optional[str]



class NadCreate(NadBase):
	pass


class NadUpdate(Nad):
	pass
