import discord
import paradisobot

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

with open("key.txt") as keyfile:
    client.run(keyfile.read())
