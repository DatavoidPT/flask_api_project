#!/usr/bin/env bash

# Remove previous container
docker stop app_hello_world
docker rm app_hello_world

# Build container
docker build -t app .

# Run container
docker run --name app_hello_world -d -p 5000:5000 --restart on-failure app

# List containers
docker ps -a