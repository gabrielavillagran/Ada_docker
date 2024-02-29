# Fatos sobre gatos
Essa aplicacao ela apresenta 3 fatos sobre gatos 😻

## Dockerhub
```
docker commit 81600748be8b gabrielavillagran/aplicacao_flask:v1
docker login
docker push gabrielavillagran/aplicacao_flask:v1
docker commit 99f7e4262a14 gabrielavillagran/mysql:5.7 
```
https://hub.docker.com/repository/docker/gabrielavillagran/aplicacao_flask/general
https://hub.docker.com/repository/docker/gabrielavillagran/mysql/general

## Aplicação
```
docker build -t aplicacao_flask --no-cache .
docker run -d -p 3000:3000 --name flask-container --network projetoada aplicacao_flask

docker build -t mysql:5.7 .
docker run -d -p 3306:3306 --name mysql_api_container --network projetoada -e MYSQL_ROOT_PASSWORD=minhasenha -d mysql:5.7 
```
![get](https://github.com/gabrielavillagran/Ada_docker/assets/92838700/02ad9025-7a5d-4328-95ef-b96985863125)
![post](https://github.com/gabrielavillagran/Ada_docker/assets/92838700/733b2aff-f6b0-4b7a-9eeb-3fceeb050725)
