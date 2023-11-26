from discord import Intents, Client
from discord_webhook import DiscordWebhook


def notify():

    intents = Intents.default()
    intents.messages = True

    client = Client(intents=intents)

    webhook_url = "your discord webhook"

    admin_id = "some_id"
    user_id = "some_other_id"

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

    client.run('your bot token')
