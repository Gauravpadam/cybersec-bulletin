@echo off
rem Change to the directory where your docker-compose.yml file is located
cd /d "../"

rem Run docker-compose build
docker-compose build

rem Run docker-compose up
docker-compose up
