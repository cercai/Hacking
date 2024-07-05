#!/usr/bin/env bash

CONTAINER_NAME=tor
IMAGE_NAME=tor
TAG=0.0.3


docker rm -f $CONTAINER_NAME
docker build -t $IMAGE_NAME:$TAG .
docker run -dit --rm --name $CONTAINER_NAME $IMAGE_NAME:$TAG

docker exec -it $CONTAINER_NAME bash

