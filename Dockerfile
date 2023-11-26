FROM python:3.10.4-slim-buster

LABEL maintainer=shayanghani1384@gmail.com

WORKDIR /opt/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

CMD ["bash", "start.sh"]
