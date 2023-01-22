import discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import json,datetime
import uuid
import asyncio

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
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                self.data = json.load(file)
            now_time = datetime.datetime.now().strftime('%H%M')
            
            for idx,word in enumerate(self.data["timering"]):
                if now_time == word[0]:
                    self.channel = self.bot.get_channel(word[1])
                    await self.channel.send("Time's up!")
                    del self.data["timering"][idx]
                    break
                    
            for idx,word in enumerate(self.data["willsay"]):
                if now_time == word[0]:
                    self.channel = self.bot.get_channel(word[2])
                    await self.channel.send(f"{word[1]}")
                    del self.data["willsay"][idx]
                    break
                
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
        except:
                pass
    
    @commands.command()
    async def timer(self,ctx,msg):
        if len(str(msg)) == 4 and msg.isdigit() and int(msg) > int(datetime.datetime.now().strftime('%H%M')):
            
            
            only_id = str(uuid.uuid1())
            only_data = None
            
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                self.data = json.load(file)
                
            self.data["timering"].append((msg,ctx.channel.id,only_id))
    
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
            
            now_time = datetime.datetime.now().strftime('%H%M')
            now_time = int(now_time[:2])*60 + int(now_time[2:])
            goal_time = int(msg[:2])*60 + int(msg[2:])
            
            difference = abs(goal_time - now_time)
            
            embed=discord.Embed(title="計時器", description="正在計時中", color=0x50648b)
            embed.set_author(name="時間管理俠")
            embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
            embed.set_footer(text="有效地運用您寶貴的時光")
                
            will_edit_message = await ctx.send(embed = embed)
            run = True
            
            while run:
                now_time = datetime.datetime.now().strftime('%H%M')
                now_time = int(now_time[:2])*60 + int(now_time[2:])
                difference = abs(goal_time - now_time)
                
                embed=discord.Embed(title="計時器", description="正在計時中", color=0x50648b)
                embed.set_author(name="時間管理俠")
                embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")
                
                await asyncio.sleep(1)
                await will_edit_message.edit(embed = embed)
                with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                    only_data = json.load(file)
                for _timer in only_data["timering"]:
                    if only_id == _timer[2]:
                        run = True
                        break
                    else:
                        run = False
            
    @commands.command()
    async def del_timer(self,ctx):
        with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
            self.data = json.load(file)
        self.data["timering"] = []
        with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
            json.dump(self.data,file)
        await ctx.send("Timers clear!")
    
    @commands.command()
    async def will_say(self,ctx,*msg):
        try:
            if len(msg[0]) == 4 and msg[0].isdigit() and msg[1:] != None and int(msg[0]) > int(datetime.datetime.now().strftime('%H%M')):
                
                only_id = str(uuid.uuid1())
                only_data = None
                send_msg = msg[1]
                try:
                    for word in msg[2:]:
                        send_msg += " "+word
                except:
                    pass
                with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                    self.data = json.load(file)
                self.data["willsay"].append((msg[0],send_msg,ctx.channel.id,only_id))
                with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                    json.dump(self.data,file)
                
                now_time = datetime.datetime.now().strftime('%H%M')
                now_time = int(now_time[:2])*60 + int(now_time[2:])
                goal_time = int(msg[0][:2])*60 + int(msg[0][2:])

                difference = abs(goal_time - now_time)

                embed=discord.Embed(title="定時說話器", description="正在計時中", color=0x50648b)
                embed.set_author(name="時間管理俠")
                embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                embed.set_footer(text="有效地運用您寶貴的時光")

                will_edit_message = await ctx.send(embed=embed)
                
                run =True
                while run:
                    now_time = datetime.datetime.now().strftime('%H%M')
                    now_time = int(now_time[:2])*60 + int(now_time[2:])
                    difference = abs(goal_time - now_time)
                    
                    embed=discord.Embed(title="定時說話器", description="正在計時中", color=0x50648b)
                    embed.set_author(name="時間管理俠")
                    embed.add_field(name="剩餘時間", value=f"{round(difference/60)}時{difference%60}分", inline=True)
                    embed.set_footer(text="有效地運用您寶貴的時光")
                    
                    await asyncio.sleep(1)
                    await will_edit_message.edit(embed = embed)
                    with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                        only_data = json.load(file)
                    for _timer in only_data["willsay"]:
                        if only_id == _timer[3]:
                            run = True
                            break
                        else:
                            run = False
        except:
            pass
        
    @commands.command()
    async def del_will_say(self,ctx):
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                self.data = json.load(file)
            self.data["willsay"] = []
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
            await ctx.send("willsay clear!")

async def setup(bot):
    await bot.add_cog(Task(bot=bot)) 