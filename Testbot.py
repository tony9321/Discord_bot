import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="[", intents = intents)

@bot.event
async def on_ready():
    print("Bot is Online!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(936592853918969866)
    await channel.send(f'{member} join!')


@bot.event
async def on_member_leave(member):
    channel = bot.get_channel(936592889465683988)
    await channel.send(f'{member} left!')

bot.run("OTM2MTMzNDgxNTMxMDc2NjE5.YfIwPg.z1hak3Iquzr5CHrFu35OPNzsk6U")