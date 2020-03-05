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
    if message.author.bot:
        return

    voice = await client.join_voice_channel(client.get_channel("Discord voice channel ID"))
    if message.content == ("lecture"):
        player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=aFI1SItR8tg')
        player.start()

    if message.content == ("bgm"):
        player = voice.create_ffmpeg_player('bgm.mp3')
        player.start()

bot.run(token)
