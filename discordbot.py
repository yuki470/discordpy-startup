from discord.ext import commands
import os
import traceback
import random
import queue


answer_set = queue.Queue(maxsize=30)
current_ans =''
current_ques = ''

bot = commands.Bot(command_prefix='>')
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
  

if not discord.opus.is_loaded():
    discord.opus.load_opus("heroku-buildpack-libopus")


@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    """Botをボイスチャンネルに入室させます。"""
    voice_state = ctx.author.voice

    if (not voice_state) or (not voice_state.channel):
        await ctx.send("先にボイスチャンネルに入っている必要があります。")
        return

    channel = voice_state.channel

    await channel.connect()
    print("connected to:",channel.name)


@bot.command(aliases=["disconnect","bye"])
async def leave(ctx):
    """Botをボイスチャンネルから切断します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    await voice_client.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command()
async def play(ctx):
    """指定された音声ファイルを流します。"""
    voice_client = ctx.message.guild.voice_client

    if not voice_client:
        await ctx.send("Botはこのサーバーのボイスチャンネルに参加していません。")
        return

    if not ctx.message.attachments:
        await ctx.send("ファイルが添付されていません。")
        return

    await ctx.message.attachments[0].save("tmp.mp3")

    ffmpeg_audio_source = discord.FFmpegPCMAudio("tmp.mp3")
    voice_client.play(ffmpeg_audio_source)

    await ctx.send("再生しました。")


@bot.command(aliases=['q'])
@commands.dm_only() # DM以外でこのコマンドを入力するとエラーを吐く
async def question(ctx,arg):
    global current_ans
    if answer_set.full():
        await ctx.send('キューがいっぱいだにゃ')
    else:
        answer_set.put(arg.replace(' ','_'))
        if current_ans == '':
            current_ans = answer_set.get()
        await ctx.send('問題を受け付けたにゃ')

# エラーの処理
@question.error
async def question_error(ctx,error):
    if isinstance(error, commands.errors.PrivateMessageOnly):
        await ctx.send(f'{ctx.author.mention}`/q`はDM限定だにゃー')    
    
# /answer または /a と発言したら正誤判定する処理 
@bot.command(aliases=['a'])
async def answer(ctx,arg):
    global current_ans
    global current_ques
    listed_arg = list(arg)
    if current_ans == '':
        await ctx.send('DMに`/q`で問題を送るにゃ')
    elif arg == current_ans:
        current_ans = ''
        current_ques = ''
        if not answer_set.empty():
            current_ans = answer_set.get()
        await ctx.send(f'{ctx.author.mention} 正解だにゃ')
    elif len(current_ans) != len(listed_arg):
        await ctx.send(f'{ctx.author.mention} ぶっぶー！長さが違うにゃ')
    else:
        cnt = 0
        for i in range(len(current_ans)):
            if current_ans[i] == listed_arg[i]:
                cnt+=1
        await ctx.send(f'{ctx.author.mention} ぶっぶー！ **'+ str(cnt) +'** 文字あってるにゃ')
        
        
 # /start または /s と発言したらスタートする処理
@bot.command(aliases=['s'])
async def start(ctx):
    global current_ans
    global current_ques
    if current_ans =='':
        await ctx.send('DMに`/q`で問題を送るにゃ')
    else:
        text = sorted(current_ans)
        if current_ques == '':
            current_ques = ''.join()
        await ctx.send('問題は **'+ current_ques +'** だにゃ')       
 
    
@bot.command()
async def fuck(ctx):
    await ctx.send('氏ね')
bot.run(token)
