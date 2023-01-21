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
        
async def setup(bot):
    await bot.add_cog(Main(bot=bot))