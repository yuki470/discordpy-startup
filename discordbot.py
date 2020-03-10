from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='p?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed (title="pypy", description="COS BOT のヘルプ", color=0xeee657)
    embed.add_field (name="p?help", value="コマンドのヘルプ", inline=False)
    await ctx.send (embed=embed)
    
@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")

@bot.command()
async def clear(message):
    if message.author.guild_permissions.administrator:
        await message.channel.purge()
        await message.channel.send("削除しました")
    else:
        await message.channel.send("権限が無いです")
@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def fuck(ctx):
    await ctx.send('氏ね')
bot.run(token)
