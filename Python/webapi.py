from fastapi import FastAPI , status , HTTPException
from pydantic import BaseModel
from typing import Optional
from database import Database


class CreateRequestBody(BaseModel):
    nationalcode : str
    firstname : str
    lastname : str
    age : str 
    country : str
    gender : bool



class UpdateRequestBody(BaseModel):
    firstname : Optional[str]
    lastname : Optional[str]
    age : Optional[str] 
    country : Optional[str]
    gender : Optional[bool]



class ResponseModel:
    nationalcode : str
    firstname : str
    lastname : str
    age : str 
    country : str
    gender : bool


app = FastAPI()


@app.post('/api/create' ,status_code=status.HTTP_201_CREATED , response_model=ResponseModel)
def create(rb : CreateRequestBody):
    try:
        Database.cur.execute("INSERT INTO info VALUES (?,?,?,?,?)",
                            rb.nationalcode ,
                            rb.firstname,
                            rb.lastname,
                            rb.age,
                            rb.country,
                            rb.gender)
        Database.conn.commit()
    except Exception or HTTPException as error :
        return error
    
    return rb


@app.get('/api/read',status_code=status.HTTP_200_OK)
def read(national_code : str):
    Database.cur.execute(f"SELECT * FROM info WHERE NationalCode = '{national_code}'")
    item = Database.cur.fetchone()

    try:
        if item != None:
            response = {
                "NationalCode" : item[0],
                "FirstName" : item[1],
                "LastName" : item[2],
                "Age" : item[3],
                "Country" : item[4],
                "Gender" : item[5]
            }

            return response
        
        else:
            return "User not found :("
        
    except Exception or HTTPException as error :
        return error
    


@app.patch('/api/update',status_code=status.HTTP_200_OK)
def update(national_code : str , rb : UpdateRequestBody):
    Database.cur.execute(f"SELECT * FROM info WHERE NationalCode = '{national_code}'")
    item = Database.cur.fetchone()

    try:
        if item != None :
            # Check
            if rb.firstname != item[1]:
                Database.cur.execute(f"UPDATE info SET FirstName = {rb.firstname} WHERE FirstName = {item[1]}")
                Database.conn.commit()
            elif rb.lastname != item[2]:
                Database.cur.execute(f"UPDATE info SET LastName = {rb.lastname} WHERE LastName = {item[2]}")
                Database.conn.commit()
            elif rb.age != item[3]:
                Database.cur.execute(f"UPDATE info SET Age = {rb.age} WHERE Age = {item[3]}")
                Database.conn.commit()
            elif rb.country != item[4]:
                Database.cur.execute(f"UPDATE info SET Country = {rb.country} WHERE Country = {item[4]}")
                Database.conn.commit()
            elif rb.gender != item[5]:
                Database.cur.execute(f"UPDATE info SET Gender = {rb.gender} WHERE Gender = {item[5]}")
                Database.conn.commit()

            return rb
        else :
            "User not found :("
    
    except Exception or HTTPException as error :
        return error
    



@app.delete('/api/delete',status_code=status.HTTP_204_NO_CONTENT)
def delete(national_code : str):
    try:
        Database.cur.execute(f"DELETE FROM info WHERE NationalCode = '{national_code}'")
        Database.conn.commit()
        
        return "User successfully deleted ! :)"
    
    except Exception or HTTPException as error :
        return error