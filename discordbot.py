from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='>')
token = os.environ['DISCORD_BOT_TOKEN']


        
@client.command()  
@commands.has_permissions(administrator=True)  
async def set_members(ctx):  
    for member in ctx.guild.members:  
        if not member.bot:  
            role = discord.utils.find(lambda r: r.name == 'member', ctx.guild.roles)  
            await member.add_roles(role)  
            
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
async def fuck(ctx):
    await ctx.send('氏ね')
bot.run(token)
