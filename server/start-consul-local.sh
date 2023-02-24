#!/bin/bash

docker run --rm -it --network colax-server -p "8500:8500" hashicorp/consul:1.14 agent -dev -client 0.0.0.0
