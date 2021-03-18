import os
from fastapi import FastAPI,Response

app = FastAPI()
@app.get("/{key}")
def return_env(key:str):
    value = os.getenv(key)
    if value is None:
        return Response(status_code=404)
    else:
        return Response(content=value)
