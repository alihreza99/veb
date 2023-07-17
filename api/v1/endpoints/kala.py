from fastapi import APIRouter, Body, Depends, HTTPException, Request, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any, List, Optional
from api import deps
from sqlalchemy.orm import Session
from core import security
import schemas, crud
from datetime import datetime, timedelta
from core.config import settings
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pyodbc
import os
from dotenv import load_dotenv
from sqlalchemy.sql import text
import json
router = APIRouter()


connection_string = "mssql+pyodbc://@DESKTOP-U89CT2B/sabad_kala?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
                                          
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

router = APIRouter()




def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/kala-info")
def kala_info( db: Session = Depends(get_db)):
    kala = db.execute(text('SELECT * FROM Table_1')).first()
    db.commit()
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if kala:
        for x in numbers:
          return { "id":x , "gheymat":kala[x]}




@router.get("/SoosMast")  # , response_model=schemas.User)
async def hello( userName: str  ,   request: Request
) -> Any:
    
    return {"message": "Soosmast haaaaaaaaaaaaaaaay" , "status_code":200  }


@router.get("/Time")  # , response_model=schemas.User)
async def hello( isPersian: bool  ,   request: Request
) -> Any:
    
    temp : vars

    if isPersian:
        temp = {"message" : "che entezari dari :|"}
    else:
        temp = {"dateTime" : datetime.now()}

    return temp

@router.post("/getKala")  # , response_model=schemas.User)
async def hello( id: int  ,   request: Request
) -> Any:

    temp = crud.kala.get_kala_by_id(id)

    return temp



    