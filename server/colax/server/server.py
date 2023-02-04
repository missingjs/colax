import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/consul-host")
async def consul_host():
    consul_host = os.environ.get("COLAX_CONSUL_HOST")
    return {"consul_host": consul_host}
