## Local run

#### Create .env file from .env-example and set all data

```sh
$ docker-compose build --no-cache
$ docker-compose up
$ docker-compose run api python backend/manage.py migrate
$ docker-compose run api python backend/manage.py makemigrations
$ docker-compose run api python backend/manage.py collectstatic

$ docker-compose exec postgres bash
```

### Local urls API

```
$ http://0.0.0.0:8083/api/users/ - cusers
$ http://0.0.0.0:8083/api/message-detail/7/ - message  detail api
 ```

### Local urls FRONT

```
$ http://0.0.0.0:8083/#/chat - Messages
$ http://0.0.0.0:8083/#/sing-up - sing  up page
$ http://localhost:8083/#/login - login
```

