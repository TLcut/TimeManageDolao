import discord
from discord.ext import commands
from discord import app_commands
import json
import asyncio
import datetime
import os

with open("./items.json",mode="r") as file:
    data = json.load(file)

intent = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intent,help_command=None)

@bot.tree.command(name="help")
async def ping(interaction:discord.Integration):
    await interaction.response.send_message("```>help to get start```",ephemeral = False)

async def main():
    for filename in os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(data["token"])
    
if __name__=="__main__":
    asyncio.run(main())