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
        
    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="幫助清單", description="時間就是金錢，我們必須珍惜時光，好得到更多錢", color=0x50648b)
        embed.set_author(name="時間管理俠")
        embed.add_field(name="幫助欄位", value="\>help", inline=True)
        embed.add_field(name="計時器", value="\>timer時分", inline=True)
        embed.add_field(name="定時說話器", value="\>will_say時分", inline=True)
        embed.add_field(name="清除定時器", value="\>del_timer", inline=True)
        embed.add_field(name="清除定時說話器", value="\>del\_will_say", inline=True)
        embed.add_field(name="跟我打乒乓球", value="\>ping", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Main(bot=bot))