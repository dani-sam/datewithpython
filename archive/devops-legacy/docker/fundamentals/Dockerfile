FROM python:3.14
WORKDIR /usr/local/app

COPY app.py  .
RUN pip3 install redis

CMD [ "python3", "app.py" ]
