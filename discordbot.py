from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='<')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send(f"コマンドは存在しません")
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    await ctx.send("```p?celarメッセージを全て消すコマンド```\n p?こんにちは　p?さようならで　挨拶！！")

  @bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick (reason=reason)
    embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"KICKが成功しました:{member.mention}",color=0xff0000)
    embed.add_field (name=f"{member.id}", value=f"{ctx.author.created_at}", inline=False)
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
        
@bot.event
async def on_member_join(member):
    channel = discord.utils.get (member.guild.text_channels, name='on_member_join')
    server=member.guild
    e=discord.Embed (description="サーバー入室ログ")
    e.add_field (name="参加ありがとうございます:", value=f"{member.mention}", inline=False)
    e.add_field (name="現在の人数:", value=server.member_count, inline=False)
    e.add_field (name="サーバー入室:", value=f"{member.joined_at}", inline=True)
    e.add_field (name="アカウント作成日:", value=f"{member.created_at}", inline=True)
    await channel.send (embed=e)
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
