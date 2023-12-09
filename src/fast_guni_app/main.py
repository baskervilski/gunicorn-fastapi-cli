import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    config_file = os.environ["HELLO_MESSAGE"]
    return {"message": "Hello World"}
