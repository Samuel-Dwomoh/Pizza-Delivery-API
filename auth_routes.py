from fastapi import APIRouter,status
from database import Session, engine
from schemas import SignUpModel
from models import Usser
from fastapi.exceptions import HTTPException


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

session=Session(bind=engine)

@auth_router.get("/")
async def hello():
    return {"message": "Hello world"}

@auth_router.post("/signup")
async def signup(user:SignUpModel):
    db_email=session.query(User).filter(User.email=user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with the email already exists")
    
