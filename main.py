import discord
from discord.ext import commands
import json
import asyncio
import datetime

with open("./items.json",mode="r") as file:
    data = json.load(file)

intent = discord.Intents.all()

bot = commands.Bot(command_prefix="[",intents=intent)

@bot.event
async def on_ready():
    print(">>bot is online")

@bot.event
async def on_member_join(member):
    print(f"{member} join!")

@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"pong!機器人延遲了: {round(bot.latency*1000)} ms")
    
@bot.command()
async def say(ctx,*msg):
    await ctx.message.delete()
    sendmsg = ""
    for word in msg:
        sendmsg += word + " "
    await ctx.send(sendmsg)
    
if __name__ == "__main__":
    bot.run(data["token"])