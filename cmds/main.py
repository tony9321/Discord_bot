import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("Setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("I love Stacy, she's so sexy and cute") 
           

def setup(bot):
    bot.add_cog(Main(bot))