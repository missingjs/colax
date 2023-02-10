import os

import aiohttp
from sanic import Sanic
from sanic.response import text

app = Sanic("colax-worker-python")

consul_address = os.environ["COLAX_CONSUL_ADDR"]

service_host = os.environ["COLAX_WORKER_HOST"]
service_port = 8000


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.get("/health")
async def health_check(request):
    return text("OK")


async def register_service():
    async with aiohttp.ClientSession() as session:
        url = f"http://{consul_address}/v1/agent/service/register?replace-existing-checks=true"
        body = {
            "ID": "colax-worker-python-2",
            "Name": "colax-worker-python",
            "Address": service_host,
            "Port": service_port,
            "Check": {
                "HTTP": f"http://{service_host}:{service_port}/health",
                "DeregisterCriticalServiceAfter": "1m",
                "Interval": "10s",
                "Timeout": "5s"
            },
            "EnableTagOverride": True
        }
        async with session.put(url, json=body) as response:
            assert response.status >= 200 and response.status < 300
            print(response.headers)

app.add_task(register_service())

