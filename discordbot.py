from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_message(message):  
    if message.content == '/members':
        print(message.guild.members)
    if message.content == '/roles':
        print(message.guild.roles':   
    if message.content == '/text_channels':
        print(message.guild.text_channels) 
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    if message.content == '/category_channels':
        print(message.guild.categories)
bot.run(token)
