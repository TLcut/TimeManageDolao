import discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import json,datetime,uuid,pytz


class Task(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.channel = None
        self.data = None
        self.clock.start()

    def cog_unload(self):
        self.clock.cancel()

    @tasks.loop(seconds=5)
    async def clock(self):
        try:
            with open("cmds/items.json",mode="r") as file:
                self.data = json.load(file)
            timezone=pytz.timezone("Asia/Taipei")
            now_time = datetime.datetime.now(timezone).strftime('%H%M')
            
            for idx,word in enumerate(self.data["timering"]):
                if now_time == word[0]:
                    self.channel = self.bot.get_channel(word[1])
                    embed=discord.Embed(title="鬧鐘", description="嗶嗶嗶!叮叮叮!咚咚嚨咚鏘!", color=0x50648b)
                    embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                    embed.add_field(name="時間到囉!", value=f"{now_time[:2]}點{now_time[2:]}分呦!", inline=True)
                    embed.set_footer(text="有效地運用您寶貴的時光")
                    await self.channel.send(embed = embed)
                    del self.data["timering"][idx]
                    break
                    
            for idx,word in enumerate(self.data["willsay"]):
                if now_time == word[0]:
                    self.channel = self.bot.get_channel(word[2])
                    await self.channel.send(f"{word[1]}")
                    del self.data["willsay"][idx]
                    break
                
            with open("cmds/items.json",mode="w") as file:
                json.dump(self.data,file)
        except:
                pass
    
    @discord.slash_command(name = "ac",description = "設定一個鬧鐘")
    async def ac(self,ctx:discord.ApplicationContext,hr:int,min:int):
        timezone=pytz.timezone("Asia/Taipei")
        if len(str(hr)) == 2 and hr <= 24 and min < 60 and min >= 0 and hr >= 0 and hr*60 + min > int(datetime.datetime.now(timezone).strftime('%H'))*60 + int(datetime.datetime.now(timezone).strftime('%M')):

            only_id = str(uuid.uuid1())
            only_data = None
            
            with open("cmds/items.json",mode="r") as file:
                self.data = json.load(file)
                
            self.data["timering"].append((str(hr)+str(min),ctx.channel.id,only_id))
    
            with open("cmds/items.json",mode="w") as file:
                json.dump(self.data,file)
            
            timezone=pytz.timezone("Asia/Taipei")      
            now_time = datetime.datetime.now(timezone).strftime('%H%M')
            now_time = int(now_time[:2])*60 + int(now_time[2:])
            goal_time = hr*60 + min
            
            difference = abs(goal_time - now_time)
            
            embed=discord.Embed(title="計時器", description="正在計時中", color=0x50648b)
            embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
            embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
            embed.set_footer(text="有效地運用您寶貴的時光")
            
            await ctx.respond(f"Set on {hr}點{min}分")
            will_edit_message = await ctx.respond(embed = embed)
            run = True
            
            while run:
                timezone=pytz.timezone("Asia/Taipei")

                now_time = datetime.datetime.now(timezone).strftime('%H%M')
                now_time = int(now_time[:2])*60 + int(now_time[2:])
                difference = abs(goal_time - now_time)
                
                embed=discord.Embed(title="計時器", description="正在計時中", color=0x50648b)
                embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")
                
                await will_edit_message.edit(embed = embed)
                with open("cmds/items.json",mode="r") as file:
                    only_data = json.load(file)
                for _timer in only_data["timering"]:
                    if only_id == _timer[2]:
                        run = True
                        break
                    else:
                        run = False
    
    @discord.slash_command(name = "fs",description = "讓機器人定時說話")
    async def fs(self,ctx:discord.ApplicationContext,hr:int,min:int,content):
        try:
            
            timezone=pytz.timezone("Asia/Taipei")
            if len(str(hr)) == 2 and hr <= 24 and min < 60 and min >= 0 and hr >= 0 and hr*60 + min > int(datetime.datetime.now(timezone).strftime('%H'))*60 + int(datetime.datetime.now(timezone).strftime('%M')):
                
                only_id = str(uuid.uuid1())
                only_data = None
                with open("cmds/items.json",mode="r") as file:
                    self.data = json.load(file)
                self.data["willsay"].append((str(hr)+str(min),content,ctx.channel.id,only_id))
                with open("cmds/items.json",mode="w") as file:
                    json.dump(self.data,file)
                timezone=pytz.timezone("Asia/Taipei")         
                now_time = datetime.datetime.now(timezone).strftime('%H%M')
                now_time = int(now_time[:2])*60 + int(now_time[2:])
                goal_time = hr*60 + min

                difference = abs(goal_time - now_time)

                embed=discord.Embed(title="定時說話器", description="正在計時中", color=0x50648b)
                embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")
                
                await ctx.respond(f"Set on {hr}點{min}分")
                will_edit_message = await ctx.respond(embed=embed)
                
                run =True
                while run:
                    timezone=pytz.timezone("Asia/Taipei")

                    now_time = datetime.datetime.now(timezone).strftime('%H%M')
                    now_time = int(now_time[:2])*60 + int(now_time[2:])
                    difference = abs(goal_time - now_time)
                    
                    embed=discord.Embed(title="定時說話器", description="正在計時中", color=0x50648b)
                    embed.set_author(name="時間管理俠",icon_url="https://cdn.discordapp.com/app-icons/1066037350813151362/1e8ab1aee21485086cea9c0bcc1449a4.png")
                    if not now_time == datetime.datetime.now(timezone).strftime('%H%M') == msg[0]:
                        embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                    else:
                        embed.add_field(name="剩餘時間", value=f"已經到囉!", inline=True)
                    embed.set_footer(text="有效地運用您寶貴的時光")
                    await will_edit_message.edit(embed = embed)
                    with open("cmds/items.json",mode="r") as file:
                        only_data = json.load(file)
                    for _timer in only_data["willsay"]:
                        if only_id == _timer[3]:
                            run = True
                            break
                        else:
                            run = False
        except:
            pass

def setup(bot):
    bot.add_cog(Task(bot=bot))