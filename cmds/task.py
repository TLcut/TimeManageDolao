import discord
from discord.ext import commands,tasks
from core.classes import Cog_Extension
import json,asyncio,datetime,time

class Task(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.channel = self.bot.get_channel(1066232019513786448)
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
            if now_time in self.data["timering"]:
                await self.channel.send("times up!")
                del self.data["timering"][self.data["timering"].index(now_time)]
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
        except:
                pass
    
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"set channel:{self.channel.mention}")
    
    @commands.command()
    async def timer(self,ctx,msg):
        if len(str(msg)) == 4 and msg.isdigit():
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                self.data = json.load(file)
            self.data["timering"].append(msg)
            
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
            await ctx.send(f"Timer set on {str(msg)}")
            
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
            if len(msg[0]) == 4 and msg[0].isdigit() and msg[1:] != None:
                send_msg = msg[1]
                try:
                    for word in msg[2:]:
                        send_msg += " "+word
                except:
                    pass
                await ctx.send(f"{msg[0]} will send '{send_msg}'")
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="r") as file:
                self.data = json.load(file)
            self.data["willsay"].append((msg[0],send_msg))
            with open("C:\\Users\\User\\Documents\\GitHub\\TimeManageDolao\\items.json",mode="w") as file:
                json.dump(self.data,file)
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