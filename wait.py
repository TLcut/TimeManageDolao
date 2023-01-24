import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime,pytz,json

class Main(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        

        

        

        
    @discord.slash_command(name="bot_info",description = "機器人的資訊")
    async def bot_info(self,ctx):
        number_of_channel = 0
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                number_of_channel += 1
        number_of_member = guild.member_count
        embed=discord.Embed(title="機器人資訊", description="正在為大家服務", color=0x50648b)
        embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
        embed.add_field(name="受到眾多伺服器的信賴", value=f"目前正在{number_of_channel}個伺服器，共有{number_of_member}位成員!", inline=True)
        embed.set_footer(text="有效地運用您寶貴的時光")
        await ctx.respond(embed = embed,ephemeral = False)

    

        
def setup(bot):
    bot.add_cog(Main(bot=bot))