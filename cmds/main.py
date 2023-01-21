import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"pong!機器人延遲了: {round(self.bot.latency*1000)} ms")
    
    @commands.command()
    async def say(self,ctx,*msg):
        await ctx.message.delete()
        sendmsg = msg[0]
        for word in msg[1:]:
            sendmsg += " " + word
        await ctx.send(sendmsg)
    @commands.command()
    async def load(self,ctx,extension):
        await self.bot.load_extension(f"cmds.{extension}",package=None)
        await ctx.send(f"Loaded {extension} done.")
        
    @commands.command()
    async def unload(self,ctx,extension):
        await self.bot.unload_extension(f"cmds.{extension}",package=None)
        await ctx.send(f"Un - Loaded {extension} done.")

    @commands.command()
    async def reload(self,ctx,extension):
        await self.bot.reload_extension(f"cmds.{extension}",package=None)
        await ctx.send(f"Re - Loaded {extension} done.")
        
async def setup(bot):
    await bot.add_cog(Main(bot=bot))