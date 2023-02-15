#!/bin/bash

export COLAX_CONSUL_ADDR="localhost:8500"

uvicorn colax.server.server:app --host 0.0.0.0 --port 6733
