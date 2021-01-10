FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install -r requirements.txt
ADD ./ /code/
CMD ["python", "store/manage.py", "runserver", "0.0.0.0:8001"]