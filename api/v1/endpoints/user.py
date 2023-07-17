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



@router.post("/login") #, response_model=schemas.Token
async def Login(*, db: Session = Depends(deps.get_db), response: Response, form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
        OAuth2 compatible token login, get an access token for future requests
    """    
    _user = crud.user.get_user_by_id(db, user_id= form_data.username.lower())
    if not _user:
        raise HTTPException(status_code=404, detail="این حساب کاربری در سیستم وجود ندارد.")    
    if not security.verify_password(form_data.password, _user.password):
        raise HTTPException(status_code=401, detail="اطلاعات وارد شده اشتباه است.")
    
    access_token = security.create_access_token(
            _user.id, expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    #set HttpOnly cookie in response
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True)  
    
    return {  "access_token":access_token,    "token_type": "bearer" , "user": _user}

@router.get("/get-student-display-info", response_model=schemas.user.Student)
async def get_student_display_info(db: Session = Depends(deps.get_db), current_user: schemas.user.User = Depends(deps.get_current_eligible_user)) -> Any:
    """
    Get current student-display-info.
    """
    _student = crud.user.get_student_display_info(db, student_id = current_user.id)
    if _student:
        return _student
    raise HTTPException(status_code=404, detail="این حساب کاربری در سیستم وجود ندارد.") 

@router.get("/get-employee-display-info", response_model=schemas.user.Employee)
async def get_employee_display_info(db: Session = Depends(deps.get_db), current_user: schemas.user.User = Depends(deps.get_current_eligible_user)) -> Any:
    """
    Get current employee-display-info.
    """
    _employee = crud.user.get_employee_display_info(db, emp_id= current_user.id)
    if _employee:
        return _employee
    raise HTTPException(status_code=404, detail="این حساب کاربری در سیستم وجود ندارد.") 

@router.get("/sum")  # , response_model=schemas.User)
async def sum( num1: int, num2: int,   request: Request
) -> Any:
    """
    add two numbers 
    """
    # return {" num1  + num2" +" = " + " " + num1+num2 }
    return {"Result": f"{num1} + {num2} = {num1 + num2}" }
    
@router.get("/subtract")  # , response_model=schemas.User)
async def subtract( num1: int, num2: int,   request: Request
) -> Any:
    """
    add two numbers 
    """
    return {"Result": f"{num1} - {num2} = {num1 - num2}"  }

@router.get("/multiplication")  # , response_model=schemas.User)
async def multiplication( num1: int, num2: int,   request: Request
) -> Any:
    """
    add two numbers 
    """
    return {"Result": f"{num1} * {num2} = {num1 * num2}" } 

@router.get("/Division")  # , response_model=schemas.User)
async def Division( num1: int, num2: int,   request: Request
) -> Any:
    """
    add two numbers 
    """
    return {"Result": f"{num1} / {num2} = {num1 / num2}" } 

    