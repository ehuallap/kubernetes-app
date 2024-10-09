import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Aplicación": F"API responde desde el pod {os.environ.get('HOSTNAME', 'DEFAULT_POD')}"}