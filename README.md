# iTravel


### Starting project with docker-compose.yml from root directory
```
docker-compose up
```
#### Migration
```
docker-compose run django_server python manage.py migrate 
```
#### Setup for .env file
```
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=database_name(iTravel for example)
PORT=5432(default)
HOST=0.0.0.0
SECRET_KEY=uuid(anything)
```