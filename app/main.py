from fastapi import FastAPI,HTTPException
from models import User
from database import init_db
from pydantic import SecretStr
from pydantic_extra_types import phone_numbers
app = FastAPI()
init_db(app)
@app.get("/")
def hi():
    return{"hi"}
@app.get('/{userId}')
async def getUser(userId : int):
    user=await User.filter(id=userId)
    if(user): return user
    raise HTTPException(status_code=404, detail=f"user {userId} not found")
@app.post('/reg')
async def addUser(number : phone_numbers.PhoneNumber, PASSWORD : SecretStr):
    return await User.create(phone=str(number), password=PASSWORD.get_secret_value())
@app.put('/update/{userId}')
async def update_user(userId: int, number : phone_numbers.PhoneNumber, PASSWORD : SecretStr):
    if(await User.filter(id=userId).update(phone=str(number), password=PASSWORD.get_secret_value())):
        return await User.get(id=userId)
    raise HTTPException(status_code=404,detail=f"user {userId} not found")
@app.delete('/delete/{userId}')
async def delete_user(userId: int):
    if (await User.filter(id=userId).delete()):
        return f"user {userId} deleted"
    raise HTTPException(status_code=404, detail=f"user {userId} not found")