import discord
from discord.ext import commands
import json
import random
import os

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

for filename in os.listdir("./cmds"):
    if filename.endswith('.py'):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["Token"])