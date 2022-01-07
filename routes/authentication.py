from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from controller import crud
from encryption import hasing
from encryption.token import create_access_token
from routes.do_select import get_db
from schema_mapping import schemas
from sqlalchemy.orm import Session
from model import models


route = APIRouter(
    tags=['Authentication']
)


@route.post('/sign_up', response_model=schemas.SignUp)
def signup(request: schemas.SignUp, db: Session = Depends(get_db)):
    data = db.query(models.UserInformation).filter(models.UserInformation.user_name == request.user_name).first()
    if data:
        raise HTTPException(status_code=203, detail='User Already Exists!')
    return crud.create_users(request, db=db)


@route.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    data = db.query(models.UserInformation).filter(models.UserInformation.email == request.username).first()
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found!')
    if not hasing.verify_password(request.password, data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Check your Password!')
    access_token = create_access_token(data={"sub": data.user_name})
    return {"access_token": access_token, "token_type": "bearer"}
