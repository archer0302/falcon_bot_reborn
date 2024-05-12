# This example requires the 'message_content' intent.

import discord
import json

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

f = open('config.json')
config = json.load(f)

client = MyClient(intents=intents)
client.run(config['token'])
