from discord.ext import commands
import os
import traceback
import random


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def celar(message):
    if message.author.guild_permissions.administrator:
        await message.channel.purge()
        await message.channel.send("削除しました")
    else:
        await message.channel.send("権限が無いです")
      
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def think(ctx):
    await ctx.send('🤔')    
  
@bot.command()
async def multiply(ctx, one: int, two: int):
    """ 数を掛ける """
    await ctx.send(one * two)

@bot.command()
async def square(ctx, number: int):
    """ 数を二乗する """
    # `!multiply <number> <number>` と同じ
    await ctx.invoke(multiply, number, number)

    
@bot.command()
async def fuck(ctx):
    await ctx.send('氏ね')
bot.run(token)
