from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException,Body
import uvicorn
from typing import Optional




app = FastAPI()

@app.post('/test_response_code')
async def test_response_code():
    raise HTTPException(
        status_code=404,
        detail='Something not found',
        headers={'header_field': 'header_value'}
)

@app.post('/test_application_json')
async def test_application_json(param:dict):
    return param 

@app.post('/test_text_plain')
async def test_application_json(param:str):
    return param 

@app.post('/test_parameter')
async def test_parameter(name=Body(None), age=Body(None)):
   try: 
     return name+' '+age
   except:
     raise HTTPException(
        status_code=404,
        detail='Something not found',
        headers={'header_field': 'header_value'}
     )

@app.post('/test_1')
def test1():
    while(1):
       print(1)

@app.post('/test_2')
def test2():
    while(1):
       print(2)      


if __name__ == "__main__":
    uvicorn.run("test_fast_api:app", host="0.0.0.0", port=8888, reload=True)