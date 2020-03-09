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

@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")

@bot.command()
@commands.has_permissions(administrator=True)
async def set_members(ctx):
    role_basic = ctx.guild.get_role(ROLE_BASIC_ID)
    for member in ctx.guild.members:
        if not member.bot:
            await member.add_roles(role_basic)
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
