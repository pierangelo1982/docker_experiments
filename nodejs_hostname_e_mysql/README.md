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

Try:
launch a db for test the app
```
docker run --name test-mysql -e MYSQL_ROOT_PASSWORD=demo -p 0.0.0.0:3306:3306 -d mysql
```

launch the app with .env credentials
```
docker run --name test-nodemysql \
    -p 8080:3000 \
    --link test-mysql:db \
    -e DB_NAME=demo \
    -e DB_USER=root \
    -e DB_PASSWORD=demo \
    -e DB_HOST=db \
    -d pierangelo1982/node_mysql
```