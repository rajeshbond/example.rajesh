from cgi import test
from datetime import datetime
import email
from operator import le
from pydantic import BaseModel, EmailStr , conint
from typing import Optional
from app.models import *


# class Post(BaseModel):
#     title: str
#     content: str
#     publish: bool = True
#     # rating: Optional[int] = None 
#     # id: int 
#     # data: jjdict # data can be validate and transdered through other methods as well 

class UserCreate(BaseModel):
    email: EmailStr           # Check for proper email syntex 
    password : str
    
    class Config:
        orm_mode = True  # original 
 
class UserOut(BaseModel):  # Select BaseMolel is we select UserCreate then password field also get inhertited by default 
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True  
    
        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    class Config:
        orm_mode = True  

 
 
class PostBase(BaseModel):
    title: str
    content: str
    publish: bool = True
           
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut  
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post : Post
    votes : int
    class Config:
            orm_mode = True

    

#  auth.py Token schemas
 
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    
# Schemes for voting 

class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)

    
    
        
     
#---------Scheme for User creation starts here ------------------

# class UserCreate(BaseModel):
#     email: EmailStr           # Check for proper email syntex 
#     password : str
#     class Config:
#         orm_mode = True  
 
# # class UserOut(BaseModel):  # Select BaseMolel is we select UserCreate then password field also get inhertited by default 
# #     id: int
# #     email: EmailStr
# #     created_at: datetime
    
        
# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str
   

  
 