# myshopforniture

## e-commerce platform build in Django

Install with docker & docker-compose:

open terminal command line inside the main folder of the project:

```
docker-compose build
```
```
docker-compose up -d
```

for migrate db
```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```
N.B: you can access to the DB at this address: http://0.0.0.0:8086

if all it's ok, the app will run at this address: http://0.0.0.0:8002




