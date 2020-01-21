Dockerize NodeJS app

This app print the Hostname of the server where is installed.
Was Build as test for loadbalancer and mysql connection...

```
docker build -t pierangelo1982/node_mysql .
```

Push on DockerHub:

Login in docker dockerhub
```
docker login docker.io
```
Push:
```
docker push pierangelo1982/node_mysql
```
ENV:
-e DB_NAE=demo  DB_USER=demo DB_PASSWORD=demo DB_HOST=db

Try:
```
docker run --name test-nodemysql \
    -p 8080:8080 \
    -e DB_NAME=demo \
    -e DB_USER=demo \
    -e DB_PASSWORD=demo \
    -e DB_HOST=db \
    -d pierangelo1982/node_mysql
```