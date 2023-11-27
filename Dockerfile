FROM python:3.10.4-slim-buster

LABEL maintainer=shayanghani1384@gmail.com

ENV TOKEN HOOK ADMIN_ID USER_ID

WORKDIR /opt/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . . 

CMD ["bash", "start.sh"]
