import discord
from discord.ext import commands
import asyncio
import datetime
bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print('Logged in as is 문의 답변')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if isinstance(message.channel, discord.DMChannel) and message.author.id != "715171908584210472":
        await bot.get_user(756045138542723082).send(f"{message.author.name} ({message.author.id}) : { message.content}")


    if message.content.startswith(">답변"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send("**Every  Bot 제작자** : " + msg)

bot.run("NzE1MTcxOTA4NTg0MjEwNDcy.Xu4HEA.lSBu-rUFISyud2jdKoqGLLF2hO8")