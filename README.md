# REST-API-Django

## Django REST-API With Docker Compose

Featuring:

- Docker
- Docker Compose
- Django
- Django REST framework

### Development

Uses the default Django development server.

1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8001](http://localhost:8001). The "store" folder is mounted into the container and your code changes apply automatically.
    
### Test Locally without Docker

- `Clone the repo`
- `Make virtual env - virenv`
- `pip install -r requirements.txt`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver`
