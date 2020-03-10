from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='>')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

bot.remove_command('help')

@bot.command()
embed=discord.Embed(title="このbotのprefixは>です", color=0x2e4bd8)
embed.set_author(name="Help")
embed.add_field(name="その他コマンド", value=">celarでメッセージを消去します/n※このコマンドは管理者のみ", inline=True)
await self.bot.say(embed=embed)

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
