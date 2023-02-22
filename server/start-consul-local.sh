#!/bin/bash

docker run --rm -it --net host hashicorp/consul:1.14 agent -dev -client 0.0.0.0
