from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id=Optional[int]
    username=str
    email=str
    password=str
    is_staff=Optional[bool]
    is_active=Optional[bool]
    
    
    class Config:
        orm_mode=True
        schema_extra={'example':{ "username": "johndoe", "email":"johndoe@gmail.com", "is_staff": False,"is_active": True}}
        
        
        
        
        
        
        
        
        
        
        
        
    class Settings(BaseModel):
        authjwt_secret_key: str = '6ed121c0d717b01a26eb359ca2dec5a59ec1acf457ef299b7b211a5e50008f7a'
    
    class LoginModel(BaseModel):
        username: str
        password: str