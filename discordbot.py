from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='>')
token = os.environ['DISCORD_BOT_TOKEN']

ID_CHANNEL_README = 0 686880408545132589  
ID_ROLE_WELCOME = 0 687553310055727104  

@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:  
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)  
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)  
        await channel.send('いらっしゃいませ！')  
        
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
