import os
from discord import Intents, Client
from discord_webhook import DiscordWebhook


def notify():

    intents = Intents.default()
    intents.messages = True

    client = Client(intents=intents)

    webhook_url = "https://discordapp.com/api/webhooks/1178295918257242263/sqm88M2Q6qbWs4jQjWnybC77x7SPFSVQ8E1LylyDKW_ZbvwSl7e8sad6As6mryT5EQCa"
    captainhook_id= "1165941781494509589"

    admin_id = "1165567657676918836"
    user_id = "732095703257710654"

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user or message.webhook_id:
            return
        webhook = DiscordWebhook(url=webhook_url, content=f"<@{admin_id}> <@{user_id}> A New Alert has been triggered")
        response = webhook.execute()

    client.run('MTE3ODI2NDU5Mjg2NzE0Nzg0OA.GhJhpo.ZEE7Ngk1ZPp7fXuS2mYLj9jtxPuUis_-o-jIJk')
