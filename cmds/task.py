import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json, asyncio, datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        async def interval():
            await self.bot.wait_until_ready()
            self.channel=self.bot.get_channel(936616436389015582)
            while not self.bot.is_closed():
                await self.channel.send("我還活著!")
                await asyncio.sleep(3) #sec

        self.bg_task = self.bot.loop.create_task(interval())

def setup(bot):
    bot.add_cog(Task(bot))