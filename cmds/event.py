import discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_ready(self):
        print(">>bot is online")

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f"{member} leave!")
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        await ctx.send(f"Rrrr報錯了XUX:\n```{error}```")  

async def setup(bot):
    await bot.add_cog(Event(bot=bot))