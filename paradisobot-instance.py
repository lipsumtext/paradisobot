import discord
from discord.ext import commands
import paradisobot
import os

client = commands.Bot(command_prefix='/para ', help_command=None)

@client.command(name="hello")
async def _hello(ctx):
    await ctx.send('Hello!')

@client.command(name="help")
async def _help(ctx):
    await ctx.send(paradisobot.copypasta("help"))

@client.command(name="cp")
async def _cp(ctx, arg):
    await ctx.send(paradisobot.copypasta(arg))

@client.command(name="pekofy")
async def _pekofy(ctx):
    channelr = client.get_channel(ctx.message.reference.channel_id)
    messager = await channelr.fetch_message(ctx.message.reference.message_id)
    await ctx.send(paradisobot.pekofy(messager.content))

if os.environ.get("DISCORD_API_KEY"):
    client.run(os.environ.get("DISCORD_API_KEY"))
else :
    with open("key.txt") as keyfile:
        client.run(keyfile.read())
