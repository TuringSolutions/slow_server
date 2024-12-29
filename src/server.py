from fastapi import FastAPI
from time import sleep
from random import randint

app = FastAPI()

@app.get("/test")
async def test():
    sleep(10)
    return randint(1, 1000)