import discord
from discord.ext import commands
import json
import asyncio
import os
import keep_alive

with open("./cmds/items.json",mode="r") as file:
    data = json.load(file)

intent = discord.Intents.all()
bot = commands.Bot(command_prefix=">",intents=intent,help_command=None)

@bot.tree.command(name="help")
async def help(interaction:discord.Integration):
    embed=discord.Embed(title="幫助清單", description="時間就是金錢，我們必須珍惜時光，好得到更多錢", color=0x50648b)
    embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
    embed.add_field(name="幫助欄位", value="\>help", inline=True)
    embed.add_field(name="計時器", value="\>鬧鐘 時分", inline=True)
    embed.add_field(name="定時說話器", value="\>未來要說 時分 內容", inline=True)
    embed.add_field(name="清除定時器", value="\>刪除鬧鐘", inline=True)
    embed.add_field(name="清除定時說話器", value="\>刪除未來要說", inline=True)
    embed.add_field(name="跟我打乒乓球", value="\>ping", inline=True)
    embed.add_field(name="得知現在時間", value="\>now 洲名/國家", inline=True)
    embed.set_footer(text="有效地運用您寶貴的時光")
    await interaction.response.send_message(embed = embed,ephemeral = False)
    
@bot.tree.command(name="bot_info")
async def bot_info(interaction:discord.Integration):
    number_of_channel = 0
    for guild in bot.guilds:
        for channel in guild.text_channels:
            number_of_channel += 1
    number_of_member = guild.member_count
    embed=discord.Embed(title="機器人資訊", description="正在為大家服務", color=0x50648b)
    embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
    embed.add_field(name="受到眾多伺服器的信賴", value=f"目前正在{number_of_channel}個伺服器，共有{number_of_member}位成員!", inline=True)
    embed.set_footer(text="有效地運用您寶貴的時光")
    await interaction.response.send_message(embed = embed,ephemeral = False)
    
async def main():
    for filename in os.listdir("./cmds"):
        if filename.endswith("py"):
            await bot.load_extension(f"cmds.{filename[:-3]}")
    await bot.start(data["token"])
    
if __name__=="__main__":
    keep_alive.keep_alive()
    asyncio.run(main())