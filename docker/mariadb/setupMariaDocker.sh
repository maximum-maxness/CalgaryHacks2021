#/usr/bin/env bash
docker build -t ch21maria .
docker run -dp 3306:3306 --name CH21DB ch21maria