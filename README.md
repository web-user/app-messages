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
$ http://0.0.0.0:8000/persons/ - list and create persons (Student/Teacher)
$ http://0.0.0.0:8000/person-detail/<int:pk>/ - Detail Update Destroy
$ http://0.0.0.0:8000/course-list/ - list course, related persons
$ http://0.0.0.0:8000/member-list/ - create member
$ http://0.0.0.0:8000/my-course-list - my members
```

### Local urls FRONT

```
$ http://localhost:8080/#/chat - Messages
$ http://localhost:8080/#/sing-up - sing  up page
$ http://localhost:8080/#/login - login
```

