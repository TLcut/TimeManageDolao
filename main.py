import discord
from discord.ext import commands
import json
import asyncio
import os
import keep_alive

with open("./cmds/items.json",mode="r") as file:
    data = json.load(file)

intent = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intent,help_command=None)
    
async def main():
    for filename in os.listdir("./cmds"):
        if filename.endswith("py"):
            bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(data["token"])
    
if __name__=="__main__":
    keep_alive.keep_alive()
    asyncio.run(main())