FROM python:3

WORKDIR /opt/python/unique
COPY /unique/unique.py /opt/python/unique

ENTRYPOINT [ "python", "unique.py" ]
