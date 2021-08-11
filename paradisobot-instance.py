import discord
import paradisobot
import os

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/para hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('/para cp'):
        keyword = message.content.split(' ')[2]
        await message.channel.send(paradisobot.copypasta(keyword))

if os.environ.get("DISCORD_API_KEY"):
    client.run(os.environ.get("DISCORD_API_KEY"))
else :
    with open("key.txt") as keyfile:
        client.run(keyfile.read())
