import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import datetime

with open("Setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["Welcome_channel"]))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["Left_channel"]))
        await channel.send(f'{member} left!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ["芃", "陳芃錚", "芃", "我愛你", "stacy"]
        if msg.content == "早安":
            await msg.channel.send("不要吵我要睡覺")
        elif msg.content in keyword:
            await msg.channel.send("stacy is gorgeous and sexy")

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="Pintwo", url="https://g0v.hackmd.io/qeQyLtQ1T1OyUUtHMlcoNQ?view", description="我們的專案介紹", color=0xffffff, timestamp = datetime.datetime.now())
        embed.set_author(name="Pintwo", url="https://github.com/tony9321")
        embed.add_field(name="What is Pintwo", value="我們的和專案的軟體名稱", inline=True)
        embed.add_field(name="Why are we making this", value="發現了一些其他網路社群, 學習資源, 搜尋引擎無法解決的問題", inline=True)
        embed.add_field(name="團隊名稱", value="Swipe For Study Buddies", inline=True)
        embed.add_field(name="軟體簡介", value="以左滑右滑的方式塞選學伴人選", inline=True)
        embed.set_footer(text="thx for visiting for more details plz visit:https://g0v.hackmd.io/qeQyLtQ1T1OyUUtHMlcoNQ?view")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Event(bot))