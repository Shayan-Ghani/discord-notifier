# Discord Notifier

Listen on a specific discord server and mention users when a new message is sent.

## Where to use 
Utilize it with alertmanager Discord Combination to mention the admin when an alert is triggered and sent to discord. 


## How to use 
1. Add your server you want to listen on to your Discord Bot (visit [this](https://www.writebots.com/discord-bot-token/) website to get one). 
2. Add a webhook to the server you want the users to be notified on from `Edit Channel>integrations` section.
3. pull the Docker image from DockerHub and run it using the following commands :
   ```bash 
   docker pull devopsteen/discord_notifier
   docker run --name discord-notifier -d -e TOKEN="your bot token" -e HOOK="your server's webhook" -e ADMIN_ID="your server admin id" -e USER_ID="extra user id to notify" devopsteen/discord_notifier:latest 
   SENDER_ID="the webhook you dedicated to prometheus alertmanager"
   ```
4. Alternatively , simply edit and deploy the compose file : 
   ```bash 
   sudo apt update && apt install docker-compose
   docker-compose up -d
   ```


Copyright © 2023 Shayan Ghani shayanghani1384@gmail.com
