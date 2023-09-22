FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /fakerApp

WORKDIR /fakerApp

COPY . .

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

RUN adduser -D fakerUser

USER fakerUser

EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]

CMD ["runserver", "0.0.0.0:8000"]