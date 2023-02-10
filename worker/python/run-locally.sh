#!/bin/bash

export COLAX_CONSUL_ADDR="localhost:8500"

ip=$(ifconfig | grep docker0 -A 1 | grep inet | awk '{print $2}')

[ -z $ip ] && { echo "unable to get ip of docker0 interface"; exit 2; }

export COLAX_WORKER_HOST=$ip

sanic --access-logs --host 0.0.0.0 --port 8000 colax.worker.server:app
