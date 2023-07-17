from typing import List
from sqlalchemy.orm import Session
from schemas.kala import Kala
from schemas.user import User, Student, Employee
from sqlalchemy.sql import text
import json

class CRUDKala():

    def get_kala_by_id(self,kala_id: int)-> Kala:
        items = [{"id" : 1 , "name" : "piaz" , "price" : 5000}]
        temp = items.where(id == kala_id)
        return temp
    
kala= CRUDKala()