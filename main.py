import discord
from discord.ext import commands
import json
import asyncio
import datetime
import os

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
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")
    
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Un - Loaded {extension} done.")

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Re - Loaded {extension} done.")
    
async def main():
    for filename in  os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(data["token"])
    
if __name__=="__main__":
    asyncio.run(main())