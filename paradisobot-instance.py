import discord
import paradisobot
import os

client = discord.Client()

prefix = '/para'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+' hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith(prefix+' cp'):
        keyword = message.content.split(' ')[2]
        await message.channel.send(paradisobot.copypasta(keyword))
    elif message.content.startswith(prefix+' pekofy'):
        if message.reference is None:
            await message.channel.send(paradisobot.pekofy(""))
        else :
            channelr = client.get_channel(message.reference.channel_id)
            messager = await channelr.fetch_message(message.reference.message_id)
            await message.channel.send(paradisobot.pekofy(messager.content))
    else: # this also implies /para help, help is implemented as a copypasta
        if message.content.startswith(prefix):
            keyword = message.content.split(' ')[1]
            await message.channel.send(paradisobot.copypasta(keyword))

if os.environ.get("DISCORD_API_KEY"):
    client.run(os.environ.get("DISCORD_API_KEY"))
else :
    with open("key.txt") as keyfile:
        client.run(keyfile.read())
