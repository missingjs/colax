import asyncio
import os

import aiohttp
from fastapi import FastAPI

app = FastAPI()

consul_address = os.environ["COLAX_CONSUL_ADDR"]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/consul-host")
async def consul_host():
    consul_host = os.environ.get("COLAX_CONSUL_HOST")
    return {"consul_host": consul_host}


@app.get("/health")
async def health():
    return {"message": "OK"}


async def update_server_list():
    while True:
        await do_update_server_list()
        await asyncio.sleep(10)


async def do_update_server_list():
    async with aiohttp.ClientSession() as session:
        url = f"http://{consul_address}/v1/agent/services"
        async with session.get(url) as response:
            print(response.status, response.headers)
            print(await response.json())


@app.on_event("startup")
async def show_hello():
    asyncio.create_task(update_server_list())
