import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime,pytz,json

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
        embed.add_field(name="計時器", value="\>鬧鐘 時分", inline=True)
        embed.add_field(name="定時說話器", value="\>未來要說 時分 內容", inline=True)
        embed.add_field(name="清除定時器", value="\>刪除鬧鐘", inline=True)
        embed.add_field(name="清除定時說話器", value="\>刪除未來要說", inline=True)
        embed.add_field(name="跟我打乒乓球", value="\>ping", inline=True)
        embed.add_field(name="得知現在時間", value="\>now 洲名/國家", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def 刪除鬧鐘(self,ctx):
        with open("cmds/items.json",mode="r") as file:
            self.data = json.load(file)
        self.data["timering"] = []
        with open("cmds/items.json",mode="w") as file:
            json.dump(self.data,file)
        await ctx.send("鬧鐘都刪除了!")
        
    @commands.command()
    async def 刪除未來要說(self,ctx):
            with open("cmds/items.json",mode="r") as file:
                self.data = json.load(file)
            self.data["willsay"] = []
            with open("cmds/items.json",mode="w") as file:
                json.dump(self.data,file)
            await ctx.send("未來要說的話都刪了!")
        
    @commands.command()
    async def now(self,ctx,msg = None):
        try:
            embed=discord.Embed(title="現在時間", description="格林威治天文臺", color=0x50648b)
            counter = 0
            limit = 25
            limit_counter = 0
            for country in pytz.all_timezones:
                if country.startswith(msg) and limit >= limit_counter:
                    limit_counter += 1
                    zone = pytz.timezone(country)
                    week = ["日","一","二","三","四","五","六"][int(datetime.datetime.now(zone).strftime("%w"))]
                    label = datetime.datetime.now(zone).strftime(f"%Y年 %m月 %d日 星期{week} %H點 %M時 %S分")
                    embed.set_author(name="時間管理俠")
                    embed.add_field(name=country, value=label, inline=True)
                    embed.set_footer(text="有效地運用您寶貴的時光")
                else:
                    counter += 1
            if counter == len(pytz.all_timezones):
                embed=discord.Embed(title="現在時間", description="格林威治天文臺", color=0x50648b)
                embed.set_author(name="時間管理俠")
                embed.add_field(name="請輸入參數:", value="洲/國家(英文)", inline=True)
                embed.add_field(name="範例:", value="Asia/Taipei", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")
        except:
            embed=discord.Embed(title="現在時間", description="格林威治天文臺", color=0x50648b)
            embed.set_author(name="時間管理俠")
            embed.add_field(name="請輸入參數:", value="洲/國家(英文)", inline=True)
            embed.add_field(name="範例:", value="Asia/Taipei", inline=True)
            embed.set_footer(text="有效地運用您寶貴的時光")
            
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Main(bot=bot))