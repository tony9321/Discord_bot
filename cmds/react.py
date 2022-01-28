import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open("Setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def pic(self, ctx):
        random_pic = random.choice(jdata["picture"])
        picture = discord.File(random_pic)
        await ctx.send(file=picture)

def setup(bot):
    bot.add_cog(React(bot))