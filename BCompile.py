import discord
from discord.ext import commands
import os
import subprocess
import importlib
TOKEN = "NzgwODUxNDQ5MzE5NTIyMzM0.X71GlQ.DdhITk9e3JPQZqgkjqEQbrcC7kU"

client = discord.Client()

bot = commands.Bot(command_prefix='$')



@bot.command(help="Juste pour le fun :-) répète ce que tu lui dit")
async def say(ctx,arg):
    await ctx.send(arg)





@bot.command(help="Interpréter du code en python")
async def Py(ctx,arg):
    proc = subprocess.Popen(['python', 'Compile.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = open("log.txt","w+")
    p = open("Compile.py","w+")
    p.write(str(arg))  
    p.close()
   
    log.write(str(proc.communicate()[0]))
    log.close()
    await ctx.send("`" + arg + "\n" + "\n" + str(open("log.txt").read()) + "`")
    await ctx.send(file=discord.File("log.txt"))
  
   

@bot.command(help = "Compiler du code en Java")
async def Java(ctx,arg):
    j = open("Compile.java","w+")
    proc = subprocess.Popen(['java','Compile.java'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = open("log.txt","w+")
    j.write(arg)
    j.close
    log.write(str(proc.communicate()[0]))
    log.close()
    await ctx.send("`" + arg + "\n" + "\n" + str(open("log.txt").read()) + "`")
    await ctx.send(file=discord.File("log.txt"))

@bot.command(help="Compiler du code en Javascript")
async def Js(ctx,arg):
    Javscript = open("Compile.js","w+")
    proc = subprocess.Popen(['node','Compile.js'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = open("log.txt","w+")
    Javscript.write(arg)
    Javscript.close()
    log.write(str(proc.communicate()[0]))
    log.close()
    await ctx.send("`" + arg + str(open("log.txt").read()) + "`")
    await ctx.send(file=discord.File("log.txt"))





@bot.event

async def on_ready():
    print("Bot ready")
    await bot.change_presence(activity = discord.Game('around'))
    

bot.run(TOKEN)

 