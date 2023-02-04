#!/bin/bash

uvicorn colax.server.server:app --host 0.0.0.0 --port 8000
