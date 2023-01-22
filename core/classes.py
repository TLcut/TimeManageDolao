import discord
from discord.ext import commands
from discord import app_commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot