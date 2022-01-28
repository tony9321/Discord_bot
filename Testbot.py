import discord
from discord.ext import commands
import json
import random

with open("Setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="[", intents = intents)

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata["Left_channel"]))
    await channel.send(f'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata["Left_channel"]))
    await channel.send(f'{member} left!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')

@bot.command()
async def pic(ctx):
    random_pic = random.choice(jdata["picture"])
    picture = discord.File(random_pic)
    await ctx.send(file=picture)

bot.run(jdata["Token"])