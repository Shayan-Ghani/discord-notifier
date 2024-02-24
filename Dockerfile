FROM python:3.10.4-slim-buster

LABEL maintainer=shayanghani1384@gmail.com

ENV TOKEN="None" HOOK="None" ADMIN_ID=0 USER_ID=0 SENDER_HOOK_NAME="None" CHANNEL_ID=0

WORKDIR /opt/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . . 

CMD ["python", "discord-notifier.py"]
