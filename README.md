## Prerequisites

Install Docker-compose, If you don't want to use Docker, then you just need Python3 and Postgres installed.

## Local Development with Docker

Start the dev server for local development:

```bash
cp .env.dist .env
sudo docker-compose up --build
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

## Local Development without Docker

### Install

```bash
python3 -m venv env && source env/bin/activate                # activate venv
cp .env.dist .env                                             # create .env file and fill-in DB info
pip install -r requirements.txt                               # install py requirements
./manage.py migrate                                           # run migrations
```

### Run dev server

This will run server on [http://localhost:8001](http://localhost:8001)

```bash
./manage.py runserver
```

### Create superuser

you can create initial super-user with next commad:

```bash
./manage.py createsuperuser
```

## API Docs
login by visiting this [link](http://localhost:8001). 

API documentation is automatically generated using Swagger. You can view documention by visiting this [link](http://localhost:8001/docs).


## for Post man
Genrate token using this endpoint at swagger
/api/v1/token/
```bash
http://0.0.0.0:8001/api/v1/token/
```


In the Header provide 
```bash
Authorization: Bearer 'paste token here'
`

## Add more user

```bash
http://localhost:8001/api/v1/users/
```
## run unit tests
Enter in container 
```bash
sudo docker exec -it assessment1_web_1 /bin/bash

```

in the container run pytest

```bash
pytest
```
