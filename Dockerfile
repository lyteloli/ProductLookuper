FROM python:3.10.11-alpine

RUN mkdir /usr/src/app
ADD . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD [ "python3.10", "main.py" ]
