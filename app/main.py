from typing import Union
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"{os.environ.get('HOSTNAME','Default env')}"}