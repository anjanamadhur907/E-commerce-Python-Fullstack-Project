from fastapi import HTTPException
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
load_dotenv()

def generate_token(payload:dict):
    token = jwt.encode(claims=payload,
                       key=os.getenv('TOKEN_SECRET',"suyfgoiuash"),
                       algorithm=os.getenv("TOKEN_ALGO","HS256"))
    return token

def verify_token(token:str):
    try:
        payload = jwt.decode(token,
                             key=os.getenv('TOKEN_SECRET',"suyfgoiuash"),
                             algorithms=os.getenv('TOKEN_ALGO','HS256'))
        print("payload : ",payload)
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Unauthorized access")