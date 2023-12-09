# Developed by: Nemanja Radojkovic, www.linkedin.com/in/radojkovic

import logging
import os
from fastapi import FastAPI

app = FastAPI()
DEFAULT_HELLO = "This is a default hello message!"

logger = logging.getLogger(__name__)


@app.get("/")
async def root():
    hello_msg = os.getenv("HELLO_MESSAGE", DEFAULT_HELLO)
    logger.info("Root accessed")
    return {"message": hello_msg}
