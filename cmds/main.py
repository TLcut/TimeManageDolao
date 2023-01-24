import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime,pytz,json

class Main(Cog_Extension):
    
    @discord.slash_command(name="help",description = "幫助欄位")
    async def help(self,ctx):
        embed=discord.Embed(title="幫助清單", description="時間就是金錢，我們必須珍惜時光，好得到更多錢", color=0x50648b)
        embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
        embed.add_field(name="幫助欄位", value="/help", inline=True)
        embed.add_field(name="計時器", value="/ac 時分", inline=True)
        embed.add_field(name="定時說話器", value="/fs 時分 內容", inline=True)
        embed.add_field(name="清除定時器", value="/del_ac", inline=True)
        embed.add_field(name="清除定時說話器", value="/del_fs", inline=True)
        embed.add_field(name="跟我打乒乓球", value="/ping", inline=True)
        embed.add_field(name="得知現在時間", value="/now 洲名/國家", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.respond(embed = embed)
        
    @discord.slash_command(name = "ping",description = "看看我的反應時間")
    async def ping(self,ctx):
        embed=discord.Embed(title="Pong!", description="打得又快又響", color=0x50648b)
        embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
        embed.add_field(name="機器人延遲了:", value=f"{round(self.bot.latency*1000)} (ms)", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.respond(embed = embed)
    
    @discord.slash_command(name = "del_ac",description = "刪除所有鬧鐘")
    async def del_ac(self,ctx):
        with open("cmds/items.json",mode="r") as file:
            self.data = json.load(file)
        self.data["timering"] = []
        with open("cmds/items.json",mode="w") as file:
            json.dump(self.data,file)
        embed=discord.Embed(title="刪除鬧鐘", description="我刪我刪我刪刪刪...", color=0x50648b)
        embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
        embed.add_field(name="刪除結果:", value="成功囉!", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.respond(embed = embed)
        
    @discord.slash_command(name = "del_fs",description = "刪除所有未來要說的話")
    async def del_fs(self,ctx):
        with open("cmds/items.json",mode="r") as file:
            self.data = json.load(file)
        self.data["willsay"] = []
        with open("cmds/items.json",mode="w") as file:
            json.dump(self.data,file)
        embed=discord.Embed(title="刪除未來要說", description="我刪我刪我刪刪刪...", color=0x50648b)
        embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
        embed.add_field(name="刪除結果:", value="成功囉!", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.respond(embed = embed)
        
    @discord.slash_command(name = "now",description = "標準時間")
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
                    label = datetime.datetime.now(zone).strftime(f"%Y年 %m月 %d日 星期{week} %H點 %M分 %S秒")
                    embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                    embed.add_field(name=country, value=label, inline=True)
                    embed.set_footer(text="有效地運用您寶貴的時光")
                else:
                    counter += 1
            if counter == len(pytz.all_timezones):
                embed=discord.Embed(title="現在時間", description="格林威治天文臺", color=0x50648b)
                embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                embed.add_field(name="請輸入參數:", value="洲/國家(英文)", inline=True)
                embed.add_field(name="範例:", value="Asia/Taipei", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")
        except:
            embed=discord.Embed(title="現在時間", description="格林威治天文臺", color=0x50648b)
            embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
            embed.add_field(name="請輸入參數:", value="洲/國家(英文)", inline=True)
            embed.add_field(name="範例:", value="Asia/Taipei", inline=True)
            embed.set_footer(text="有效地運用您寶貴的時光")
            
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))