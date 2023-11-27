from discord import Intents, Client
from discord_webhook import DiscordWebhook

from os import environ

def notify():

    TOKEN = environ.get("TOKEN" , None)
    HOOK = environ.get("HOOK" , None)
    ADMIN_ID = environ.get("ADMIN_ID", None)
    USER_ID = environ.get("USER_ID", None)

    intents = Intents.default()
    intents.messages = True
   
    client = Client(intents=intents)

    webhook_url = HOOK

    admin_id = ADMIN_ID
    user_id = USER_ID

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user or message.webhook_id:
            return
        # create your message
        webhook = DiscordWebhook(url=webhook_url, content=f"<@{admin_id}> <@{user_id}> A New Alert has been triggered")
        response = webhook.execute()

    client.run(TOKEN)