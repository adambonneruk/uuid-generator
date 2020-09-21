FROM python:3
WORKDIR /app
COPY . /app

ENTRYPOINT [ "python", "./unique/unique.py" ]