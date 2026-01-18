#!/bin/sh

docker build -t xgalvanize/django-backend .
docker push xgalvanize/django-backend