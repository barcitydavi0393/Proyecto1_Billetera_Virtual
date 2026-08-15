from fastapi import Depends, HTTPException, FastAPI
from database import Base, engine
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse
from core.security import get_password_hash, verify_password, create_access_token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.post("/register", response_model= UserResponse)
async def crear_usuario(item: UserCreate, db: Session = Depends(get_db)):
    db_user= db.query(User).filter(User.phone == item.phone).first()
    if db_user is not None:
        raise HTTPException(
            status_code= 400,
            detail = f"El numero de telefono '{item.phone}' ya esta registrado"
        ) 

    password_hashed = get_password_hash(item.password)

    nuevo_usuario = User(
        name = item.name,
        phone= item.phone,
        password_hash = password_hashed,
       
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

@app.post("/login")
async def login_usuario(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phone == form_data.username).first()
    if not db_user or not verify_password(form_data.password, db_user.password_hash):
        raise HTTPException(
            status_code= 401,
            detail= f'Credenciales Incorrectas'
        )

    access_token = create_access_token({"sub": db_user.phone})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

