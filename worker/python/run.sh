#!/bin/bash

sanic --host 0.0.0.0 --port 8000 colax.worker.server:app
