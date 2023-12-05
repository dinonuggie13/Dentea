import discord
from tokenbox import token
from discord.ext import commands
import asyncio
import lib
import time



bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())



## EVENTS
@bot.event
async def on_ready():
    print(f'Logged on.')



## COMMANDS
@bot.command()
async def timedmessage(ctx, *msg):

    meow = (" ".join(msg))
    listtotake = lib.sstlist(meow, "|")
    print(listtotake)
    time = int(listtotake[1])
    message = listtotake[0]

    await ctx.send(f"Timer has started! \"{message}\" will be sent in {time} seconds!")
    await asyncio.sleep(time)
    await ctx.send(message)


# Creates a new timer
# arguments:
#   timer_name: name of the new timer to make
#   time_in_secs: amount of seconds until timer completion
@bot.command()
async def meow(ctx, *args):
    meow = (" ".join(args))
    listtotake = lib.sstlist(meow, "|")

    timeinseconds = int(listtotake[1])
    timername = listtotake[0]

    if lib.checkfortimer(timername):
        await ctx.send("a timer with that name already exists")
    else:
        timeinseconds = int(timeinseconds)
        lib.addtimer(timeinseconds, timername)
        await ctx.send(f"timer {timername} added. {timeinseconds} seconds remaining.")
        await asyncio.sleep(timeinseconds)
        await ctx.send(f"{timername}'s time is up!, {timeinseconds} seconds passed")
        lib.deltimer(timername)


# Checks remaining time for specified timer
# arguments:
#   timer_name: name of timer to check
@bot.command()
async def woof(ctx, timername):
    if lib.checkfortimer(timername):
        timeleft = lib.timerdict["timers"][timername]["duration"] - (time.time() - lib.timerdict["timers"][timername]["time"])
        await ctx.send(f"{timeleft} remaining for {timername}")
    else: await ctx.send("invalid input")



## RUN BOT
bot.run(token)


