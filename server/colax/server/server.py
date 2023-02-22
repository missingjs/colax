import asyncio
import base64
import json
import logging
import os

import aiohttp
from fastapi import FastAPI, HTTPException

from .solution import UserSolution
from .workers import WorkerManager

app = FastAPI()

consul_address = os.environ["COLAX_CONSUL_ADDR"]

worker_manager = WorkerManager()

logger = logging.getLogger(__name__)


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


@app.post("/solution")
async def solution_solve(us: UserSolution):
    lang = us.language
    services = worker_manager.get_services(lang)
    if not services:
        raise HTTPException(status_code=404, detail=f"no service for language {lang}")


async def update_server_list():
    while True:
        await do_update_server_list()
        await asyncio.sleep(10)


async def do_update_server_list():
    async with aiohttp.ClientSession() as session:
        url = f"http://{consul_address}/v1/agent/services"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    consul_info = await response.json()
                    worker_manager.update_from_consul(consul_info)
                    logger.debug(f"update service info, {consul_info}")
                else:
                    text_info = await response.text()
                    logger.error(
                        f"consul not working properly: {response.status} {response.headers} {text_info}"
                    )
        except Exception:
            logger.exception(f"failed to communicate with consul - {url}")


@app.on_event("startup")
async def show_hello():
    asyncio.create_task(update_server_list())


def base64_decode(s: str) -> str:
    return base64.standard_b64decode(s.encode()).decode()
