from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message)
    # /test と打った場合のみ反応するように
    if message.content != '/test':
        return

    # message インスタンスから guild インスタンスを取得
    guild = message.guild 

    # ユーザとBOTを区別しない場合
    member_count = guild.member_count
    await message.channel.send(f'メンバー数：{member_count}')

    # ユーザのみ
    user_count = sum(1 for member in guild.members if not member.bot)
    await message.channel.send(f'ユーザ数：{user_count}')

    # BOTのみ
    bot_count = sum(1 for member in guild.memers if member.bot)
    await message.channel.send(f'BOT数：{bot_count}')
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def fuck(ctx):
    await ctx.send('氏ね')
bot.run(token)
