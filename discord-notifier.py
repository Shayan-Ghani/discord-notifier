import discord
from discord.ext import commands
from aiohttp import ClientSession
from os import environ

BOT_TOKEN = environ.get("TOKEN" , None)
CHANNEL_ID = int(environ.get("CHANNEL_ID" , '0'))
NOTIFICATION_WEBHOOK_URL = environ.get("HOOK" , None)
USER_ID = int(environ.get("USER_ID", '0'))

SENDER_HOOK_NAME = environ.get("SENDER_HOOK_NAME", None)

def notify():
    intent = discord.Intents.default()
    intent.messages = True

    client = commands.Bot(command_prefix='!', intents=intent)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user.name}')

    # use aiohttp and discord Webhook async to notify the user 
    @client.event
    async def on_message(message):
        # Check if the message is from the target channel and the target bot
        if message.channel.id == CHANNEL_ID and message.author.name == SENDER_HOOK_NAME:

            notification_message = f"<@{USER_ID}> A New Alert has been triggered"

            async with ClientSession() as session:
                webhook = discord.Webhook.from_url(NOTIFICATION_WEBHOOK_URL, session=session)
                await webhook.send(notification_message, username='Captian Hook')

    client.run(BOT_TOKEN)

if __name__ == "__main__":
    notify()