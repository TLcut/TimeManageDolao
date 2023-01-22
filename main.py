import discord
from discord import app_commands
from discord.ext import commands
import json
import asyncio
import datetime
import os

with open("./items.json",mode="r") as file:
    data = json.load(file)

intent = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intent)

@bot.command(name = "hi", description = "My first application Command")
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

async def main():
    for filename in  os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(data["token"])
    
if __name__=="__main__":
    asyncio.run(main())