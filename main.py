try:
    import sqlite3 #commit 24.06.2020
    import discord
    import json
    import subprocess
    import os
    import time
    import random
    import requests
    import asyncio
    import youtube_dl
    import discord.ext.commands
    from discord.ext import commands
    from config import settings
    from discord import utils
    from discord.utils import get
    from discord.ext.commands import Bot
    from discord.voice_client import VoiceClient
    import clr
    import threading
except ImportError: 
    print('Вероятнее всего, Вы не запустили deps.py ($python deps.py)')

bot = Bot(settings['PREFIX'])

bot.remove_command('help')

warns = sqlite3.connect("warns.db")
bans = sqlite3.connect("bans.db")
permbans = sqlite3.connect("permbans.db")

clr.AddReference('MusicDownloader')

from MusicDownloader import Downloader

try:

    @bot.command()
    async def _rename_(ctx, channel: discord.VoiceChannel, *, new_name):
        await channel.edit(name=new_name)

    @bot.event
    async def on_command_error(ctx, error):
        em = bot.get_emoji(724944121109676092)
        if isinstance(error, commands.CommandNotFound ):
            await ctx.send(f'**{ctx.message.author.mention}, данная команда не обнаружена**{str(em)}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _jojo_(ctx, victim: discord.Member, reason = "Доигрался, вот тебе ролевые игры"):
        emb = discord.Embed (title = 'Kick :lock:', colour = discord.Color.dark_red())
        author = ctx.message.author
        i = 10
        for i in range(10, 0, -1):
            await ctx.send(str(i))
            time.sleep(1)

        emb.set_author (name = victim, icon_url = victim.avatar_url)
        emb.add_field (name = 'Kick user', value = 'Kick user : {}'.format(victim.mention))
        emb.set_footer (text = 'Был отпердолен скалкой администратором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)

        await ctx.send (embed = emb)

        print(f'[{ctx.guild.name}] Kick banned { victim }')

        await victim.kick(reason = reason)

    @bot.command() 
    async def _hola_(ctx, arg):
        await ctx.channel.purge(limit = 1)
        await ctx.send(arg), print(f'[{ctx.guild.name}] $Bot send message: {arg}')

    @bot.command()
    async def qq(ctx):
        """Hello, server"""
        author = ctx.message.author
        await ctx.send(f'Категорически приветствую, {author.mention}!'), print(f'[{ctx.guild.name}] $Bot send message: Hello, {author.nick} ({author.name})')

    @bot.command()
    async def bb(ctx):
        """Bye, all"""
        author = ctx.message.author
        await ctx.send(f'До связи, {author.mention} :)'), print(f'[{ctx.guild.name}] $Bot send message: Bye, {author.nick} ({author.name})')

    @bot.command()
    async def pp(ctx):
        await ctx.channel.purge(limit = 1)
        author = ctx.message.author
        await ctx.send(f'{author.mention} Отошел.'), print(f'[{ctx.guild.name}] $Bot send message: {author.nick} ({author.name}) Отошел.')

    @bot.command()
    async def _pp_(ctx):
        await ctx.channel.purge(limit = 1)
        author = ctx.message.author
        await ctx.send(f'{author.mention} Вернулся.'), print(f'[{ctx.guild.name}] $Bot send message: {author.nick} ({author.name}) Вернулся.')

    @bot.command()
    async def fox(ctx):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)
        author = ctx.message.author

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed), print(f'[{ctx.guild.name}] $Bot send embed fox (by',author.nick, ')' )

    @bot.command()
    async def dog(ctx):
        response = requests.get('https://some-random-api.ml/img/dog')
        json_data = json.loads(response.text)
        author = ctx.message.author

        embed = discord.Embed(color = 0xff9900, title = 'Random Dog')
        embed.set_image(url = json_data['link'])
        member = discord.Member
        try: await ctx.send(embed = embed), print(f'[{ctx.guild.name}] $Bot send embed dog (by',author.nick, ')' )
        except: await ctx.send('CommandNotFound', {author.mention})

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _cleaner_(ctx, amount):
        author = ctx.message.author
        await ctx.channel.purge(limit=int(amount))
        await ctx.channel.send(':: Сообщения успешно удалены'), print(f'[{ctx.guild.name}] {author.nick} cleaned chat for {amount} positions')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _kick_ (ctx, member: discord.Member, *, reason = None):
        emb = discord.Embed (title = 'Kick :warning:', colour = discord.Color.dark_red())

        await ctx.channel.purge(limit = 1)
                        
        await member.kick(reason = reason)

        emb.set_author (name = member.name, icon_url = member.avatar_url)
        emb.add_field (name = 'Kick user', value = 'Kicked user : {}'.format(member.mention))
        emb.set_footer (text = 'Был опасхален администратором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)

        await ctx.send (embed = emb)

        print(f'[{ctx.guild.name}] Bot kicked { member }')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _ban_ (ctx, member: discord.Member, *, reason = f'Нарушение правил сервера. $Banlist.append(you)'):
        emb = discord.Embed (title = 'Ban :lock:', colour = discord.Color.dark_red())

        await ctx.channel.purge(limit = 1)

        await member.ban(reason = reason)

        emb.set_author (name = member.name, icon_url = member.avatar_url)
        emb.add_field (name = 'Ban user', value = 'Ban user : {}'.format(member.mention))
        emb.set_footer (text = 'Был смешан с асфальтом администратором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)

        await ctx.send (embed = emb)

        print(f'[{ctx.guild.name}] Bot banned { member }')



    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _cleanadm_(ctx, amount):
        author = ctx.message.author
        await ctx.channel.purge(limit=int(amount))
        print(f'[{ctx.guild.name}] {author.nick} cleaned chat for {amount} positions')

    @bot.command()
    async def _join_(ctx):
        global voice
        await ctx.channel.purge(limit = 1)
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)
        
        if voice and voice.is_connected():
            await ctx.channel.purge(limit = 1)
            await voice.move_to(channel)
            await ctx.send('Успешно прикатился :man_in_manual_wheelchair:')
            print(f'[{ctx.guild}] Bot connected to {ctx.message.author.name}')
        else:
            voice = await channel.connect()
            await ctx.send('Успешно прикатился :man_in_manual_wheelchair:')
            print(f'[{ctx.guild}] Bot connected to {ctx.message.author.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _am_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = True, deafen = True)
        print(f'[{ctx.guild}] {ctx.message.author} all muted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _aum_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = False, deafen = False)
        print(f'[{ctx.guild}] {ctx.message.author} all unmuted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _mute_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = True)
        print(f'[{ctx.guild}] {ctx.message.author} muted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _dea_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(deafen = True)
        print(f'[{ctx.guild}] {ctx.message.author} deafen {victim_member}')


    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _exc_(ctx, victim):
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} начинается. Всего вам плохого**')
        for i in ctx.guild.voice_channels:
            channel = discord.utils.find(lambda x: x.name == i.name, ctx.guild.voice_channels)
            await victim_member.move_to(channel)
            time.sleep(0.75)
            print(f'[exc] ${ victim_member } transferred in { i.name }')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _lock_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            for i in range(30):
                await victim_member.edit(mute = True, deafen = True)
                print(f'[{author.id}] lock {victim_member}')
                try:
                    await victim_member.edit(nick = '_PIDARAS_')
                except:
                    pass
                time.sleep(0.75)
        else:
            print(0)
            print(author.id)

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _unlock_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            await victim_member.edit(mute = False, deafen = False)
            print(f'[{author.id}] unlock {victim_member}')
            await victim_member.edit(nick = f'{victim_member.name}')
        else:
            print(0)
            print(author.id)
            await victim_member.edit(nick = f'{victim_member.name}')

    @bot.command()
    async def _vers_(ctx):
        await ctx.send(discord.__version__)

    @bot.command()
    async def _gs_(ctx):
        array = list()
        emb = discord.Embed(title = 'PIDARASI')
        for i in ctx.guild.voice_channels:
            for k in i.members:
                array.append(f'```[{i}] {k.name}```\n')

        g = ''
        for i in range(len(array)):
            try:
                g += array[i]
            except IndexError:
                print(f'[{ctx.guild.name}] Точка остановы')

        print(f'[{ctx.guild.name}] Bot send list of members in voice channels ({ctx.message.author.name})')
            
        await ctx.send(g)

    nn = True

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _exc_adm_(ctx, victim):
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        voice = get(bot.voice_clients, guild = ctx.guild)
        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} начинается. Всего вам плохого**')
        while nn == True:
            for k in range(10):
                await victim_member.edit(mute = True, deafen = True)
                print(f'[{ ctx.guild.name }] {k + 1} Заход пошел')
                for i in ctx.guild.voice_channels:
                    channel = discord.utils.find(lambda x: x.name == i.name, ctx.guild.voice_channels)
                    await victim_member.move_to(channel)
                    time.sleep(75*0.01)
                    print(f'[exc] { victim_member } transferred to { i.name }')
        await victim_member.edit(mute = False, deafen = False)
        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} окончена. Надеюсь, Вы впечатлены**')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _stop_exc_(ctx, victim):
        victim_member = discord.utils.get(ctx.guild.members, name=victim) 
        nn = False
        print('Точка остановы')
        await victim_member.move_to(ctx.guild.afk_channel)
        await ctx.send(f'{victim_member.mention}, **Принудительная остановка**')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _exc_adm_gogi_(ctx, name1: str, n: int):
            victim_member = discord.utils.get(ctx.guild.members, name=name1)
            await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} начинается. Всего вам плохого**')
            while n > 0:
                for i in ctx.guild.voice_channels:
                    channel = discord.utils.find(lambda x: x.name == i.name, ctx.guild.voice_channels)
                    await victim_member.move_to(channel)
                    time.sleep(0.75)
                    print(f'[exc adm] ${ victim_member } transferred in { i.name }')
                    print(n)
                    n -= 1
            await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} окончена. Надеюсь, Вы впечатлены**')

    @bot.command()
        async def _play_old_(ctx, url: str):
            song_there = os.path.isfile('song.mp3')
            try:
                if song_there: 
                    os.remove('song.mp3')
                    print('[log] Старый файл удален')
            except PermissionError:
                print('[log] Не удалось удалить файл')
            await ctx.send('Пожалуйста, ожидайте')

            voice = get(bot.voice_clients, guild = ctx.guild)

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors' : [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'   
                }]
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print('[log] Загружаю музыку...')
                ydl.download([url])

            for file in os.listdir('./'):
                if file.endswith('.mp3'):
                    name = file
                    print(f'[log] Переименовываю файл: {file}')
                    os.rename(file, 'song.mp3')

            voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
            voice.source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1

            song_name = name.rsplit('-', 2)
            await ctx.send(f'Сейчас проигрывается музыка: {song_name[0]}')

    @bot.command()
    async def _leave_(ctx):
        global voice
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)
        
        if voice and voice.is_connected():
            await voice.disconnect()
            await ctx.send('Успешно откатился :camel:')
        else:
            await voice.disconnect()
            await ctx.send('Успешно откатился :camel:')

    @bot.command()
    async def _play_(ctx, url: str):
        folder = Downloader.Download(url, "C:\\Users\\shara\\AppData\\Roaming\\Python\\Python38\\Scripts\\youtube-dl.exe")
        path = 'Downloads\\' + str(folder)

        global voice

        for song in os.listdir(path):
            # ffmpeg = 'ffmpeg ' + Downloader.GetFfmpegArgs('Downloads\\' + song)
        
            voice.play(discord.FFmpegPCMAudio(path + '\\' + song), after = lambda e: print(f'[log] {song}, музыка закончила свое проигрывание'))
            voice.  source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1

            await ctx.send(f'Сейчас проигрывается музыка: {song}')

    @bot.command()
    async def kick(ctx, victim):
        victim_member = get(ctx.guild.members, name = victim)
        channelU = discord.utils.find(lambda x: x.name == 'PIDARASI VI SUKI', ctx.guild.voice_channels)
        await victim_member.move_to(channelU)
        print(f'[admin] {ctx.author.name} отключил от чата {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _list_(ctx):
        print('[admin] $Bot send list of members of the server')
        list_memb = list()
        emb = discord.Embed (title = f'Список участников сервера {ctx.guild.name} :clipboard: ')
        emb.description = str(len(ctx.guild.members)) + ' ' + 'участника(-ов):'
        for i in ctx.guild.members:
            emb.add_field(name = i.name, value = i.roles[len(i.roles) - 1])
        await ctx.send ( embed = emb )

    @bot.command()
    async def _list_ch_(ctx):
        for i in ctx.guild.voice_channels:
            print(i.name)

    @bot.command()
    async def _ls_(ctx):
        array , array1 = list(), list()
        for guild in bot.guilds:
            array.append(guild.name)
            array1.append(guild.id)
        print(*array, sep = '\\\\')
        emb = discord.Embed(title = "Список серверов, на которых катируется бот:")
        for i in range(len(array)):
            emb.add_field(name = array1[i], value = array[i])
        await ctx.send( embed = emb )

    @bot.command()
    async def _tr_(ctx, victim, channel):
        victim_member = get(ctx.guild.members, name = victim)
        channelU = discord.utils.find(lambda x: x.name == channel, ctx.guild.voice_channels)
        try:
            await victim_member.move_to(channelU)
            print(f'[tr] { victim_member } was transfered to { channelU }')
        except:
            pass
            print(f'[tr] Transfer { victim_member } failed')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _lat_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        global n
        n = True
        author = ctx.message.author
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        while n == True:
            await victim_member.edit(mute = True, deafen = True)
            time.sleep(0.75)
            print(f'[{author.id}] lock {victim_member}')
            try:
                await victim_member.edit(nick = '_PIDARAS_')
            except: 
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _ulat_(ctx, victim):
        await ctx.channel.purge(limit = 1)
        global n 
        n = False
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = False, deafen = False)
        print(f'[{ ctx.guild }] unlock  { victim_member }')
        try:
            await victim_member.edit(nick = victim)
        except:
            pass

    @bot.command()
    async def _send_(ctx, victim):
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            victim_member = get(ctx.guild.members, name = victim)
            await ctx.send(victim_member)

    #warn section


    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _warn_(ctx, victim, reason):
        w = warns.cursor()
        try:
            w.execute('SELECT * FROM ' + '"' + str(ctx.guild.name) + '"')
            warns.commit()
        except:
            w.execute('CREATE TABLE ' + '"' + str(ctx.guild.name) + '"' + '(name text, reason text, "issued by" text, quantity integer)')
            warns.commit()
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        w.execute('SELECT name FROM ' + '"' + str(ctx.guild.name) + '"')
        victim_member = get(ctx.guild.members, name = victim)
        b = w.fetchall()
        b = str(b)
        d1 = b.find(victim)
        e = str(author).find('$')
        author = str(author)[0:e]
        if victim_member == None :
            await ctx.send(f'Такого участника нет на сервере!')
        else:
            if d1 < 0:
                a = ('INSERT INTO ' + '"' + str(ctx.guild.name) + '"' + ' VALUES(' + "'" + str(victim) + "', " + "'" + str(reason) + "', " + "'" + str(author) + "', " + "'" + '1' + "')")
                w.execute(a)
                await ctx.send(f'Участник {victim_member.mention} полчулил варн')
            else:
                a = ('SELECT quantity FROM ' + '"' + str(ctx.guild.name)  + '"' + ' WHERE name = ' + '"'  + str(victim) + '"')
                w.execute(a)
                b = w.fetchall()
                b = str(b)
                d = int(b[2])
                a1 = ('UPDATE ' + '"' + str(ctx.guild.name) + '"' + ' SET reason = ' + '"' + str(reason) + '"' + ' where name = ' + '"' + str(victim) + '"')
                a2 = ('UPDATE ' + '"' + str(ctx.guild.name) + '"' + ' SET "issued by" = ' + '"' + str(author) + '"' + ' where name = ' + '"' + str(victim) + '"')
                a3 = ('UPDATE ' + '"' + str(ctx.guild.name) + '"' + ' SET quantity = ' + '"' + str(int(d) + 1) + '"' + ' where name = ' + '"' + str(victim) + '"')
                w.execute(a1)
                w.execute(a2)
                w.execute(a3)
                await ctx.send(f'Участник {victim_member.mention} полчулил варн')
                if int(d) + 1 >= mw:
                    await victim_member.kick(reason = 'кик по причине:' + str(mw) + '/' + str(mw) + 'варнов')
                    w.execute('DELETE FROM ' + '"' + str(ctx.guild.name) + '"' + ' where name = ' + "'" + str(victim) + "'")
                    await ctx.send(f'был кикнут администратором{author.mention} за максимальное количество варнов')
        warns.commit()

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _unwarn_(ctx, victim):
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        w = warns.cursor()
        w.execute('SELECT name FROM ' + '"' + str(ctx.guild.name) + '"')
        b = w.fetchall()
        b = str(b)
        d1 = b.find(victim)
        e = str(author).find('#')
        author = str(author)[0:e]
        if victim_member == None :
            await ctx.send(f'Такого участника нет на сервере!')
        else:
            if d1 < 0:
                await ctx.send(f'У {victim_member.mention} нету варнов')
            else:
                a = ('SELECT quantity FROM ' + '"' + str(ctx.guild.name) + '"' + ' WHERE name = ' + '"'  + str(victim) + '"')
                w.execute(a)
                b = w.fetchall()
                b = str(b)
                d = int(b[2])
                a1 = ('UPDATE' + '"' + str(ctx.guild.name) + '"' + 'SET quantity = ' + '"' + str(int(d) - 1) + '"' + ' where name = ' + '"' + str(victim) + '"')
                w.execute(a1)
                if d - 1 == 0:
                    w.execute('DELETE FROM ' + '"' + str(ctx.guild.name) + '"' + ' where name =' + "'" + str(victim) + "'")
                await ctx.send(f'Варн с участника {victim_member.mention} был успешо снят')
        warns.commit()

    @bot.command()
    @commands.has_permissions()
    async def warn_list(ctx, victim):
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        mw = 3
        w = warns.cursor()
        w.execute('SELECT name FROM ' + '"' + str(ctx.guild.name) + '"')
        b = w.fetchall()
        b = str(b)
        d1 = b.find(victim)
        if d1 > 0:
            a = ('SELECT name, quantity FROM ' + '"' + str(ctx.guild.name) + '"')
            w.execute(a)
            d = w.fetchall()
            d = str(d)
            b = d.find(victim)
            e = len(victim) + b + 3
            await ctx.send(f'У {victim_member.mention}' + str(d[e]) +' из ' + str(mw))
        else:
            await ctx.send(f'У {victim_member.mention} нету варнов')

    @bot.command()
    async def _test_(ctx, victim):
        victim_member = get(ctx.guild.members, name = victim)
        if victim_member == None:
            await ctx.send('Кто это???')
        else:
            await ctx.send(f'{ victim_member.id } существует')

    #no_use_this_pls
    #----------------------------------------------------------------------------------------------------------------

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _kickall_(ctx):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'~~**...Машины уничтожаеют сервер :skull:...**~~'), print(f'[warning] Бот {bot.user.name} кикнул всех, кого мог')
        for m in ctx.guild.members:
            try:
                await m.kick(reason="Облегченный рейд на сервер успешно проведен.")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _banall_(ctx):
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'~~**...Машины уничтожаеют сервер :skull:...**~~'), print(f'[warning] Бот {bot.user.name} забанил всех, кого мог')
        for m in ctx.guild.members:
            try:
                await m.ban(reason="Рейд на сервер успешно проведен.")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _dl_(ctx):
        await ctx.channel.purge(limit = 1), print(f'[warning] {bot.user.name} Удалил столько ролей, сколько смог')
        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Плановое обнуление")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def _dch_(ctx):
        failed = []
        counter = 0
        await ctx.channel.purge(limit = 1)
        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason="Рейд успешно проведен.")
            except: failed.append(channel.name)
            else: counter += 1
        fmt = ", ".join(failed)
        print(f'[warning] Рейд по удалению каналов прошел довольно успешно ({bot.user.name})')

    #----------------------------------------------------------------------------------------------------------------


    #section of errors (validation)

    @_cleaner_.error
    async def cleaner_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')
        else:
            pass

    @_kick_.error
    async def kick_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_ban_.error
    async def ban_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @kick.error
    async def kick_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_exc_.error
    async def exc_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_lock_.error
    async def lock_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_unlock_.error
    async def exc_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_exc_.error
    async def exc_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_exc_adm_gogi_.error
    async def exc2_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_play_.error
    async def play_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_leave_.error
    async def leave_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_cleanadm_.error
    async def cleanadm_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_mute_.error
    async def mute_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_dea_.error
    async def dea_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_am_.error
    async def am_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_aum_.error
    async def aum_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @fox.error
    async def fox_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @dog.error
    async def dog_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_tr_.error
    async def tr_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова (скорее всего вы пытаетесь перенести неподключенного бота) :dart:')

    @_lat_.error
    async def lat_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_ulat_.error
    async def ulat_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_warn_.error
    async def warn_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь :dart:')

    @_unwarn_.error
    async def warn_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь :dart:')

    @warn_list.error
    async def warn_list_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь :dart:')

    @_kickall_.error
    async def kickall_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер :dart:')

    @_banall_.error
    async def banall_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер :dart:')

    @_dch_.error
    async def dch_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер :dart:')

    @_dl_.error
    async def dl_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер :dart:')

    @_exc_adm_.error
    async def exc1_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):   
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер :dart:')

    @_rename_.error
    async def rename_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_ls_.error
    async def ls_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_gs_.error
    async def gs_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_test_.error
    async def test_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_send_.error
    async def send_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @_list_ch_.error
    async def lch_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова :dart:')

    @bot.command(pass_context = True)
    async def   _help_(ctx):
        emb = discord.Embed (title = 'Навигация по командам :clipboard: ')
        emb.add_field(name ='Описание сервера', value = 'Ничего строгого')
        emb.add_field(name ='{}```_cleaner_ int``` :broom: '.format(settings['PREFIX']), value = 'Очистка чата (adm)')
        emb.add_field(name ='{}```_ban_ ID``` :lock:'.format(settings['PREFIX']), value = 'Бан клиента на сервере(adm)')
        emb.add_field(name ='{}```_kick_ ID``` :warning: '.format(settings['PREFIX']), value = 'Кик клиента с сервера(adm)')
        emb.add_field(name ='{}```qq```'.format(settings['PREFIX']), value = 'Приветствие')
        emb.add_field(name ='{}```bb```'.format(settings['PREFIX']), value = 'Прощание')
        emb.add_field(name ='{}```pp```'.format(settings['PREFIX']), value = 'Клиент отошел')
        emb.add_field(name ='{}```_pp_```'.format(settings['PREFIX']), value = 'Клиент вернулся')
        emb.add_field(name ='{}```fox || dog```'.format(settings['PREFIX']), value = 'Генерация img')
        emb.add_field(name ='{}```_join_```'.format(settings['PREFIX']), value = 'Подключение бота к текущему каналу')
        emb.add_field(name ='{}```_leave_```'.format(settings['PREFIX']), value = 'Отключение бота от канала')
        #emb.add_field(name ='{}```_play_ URL```'.format(settings['PREFIX']), value = 'Багающее включение музыки по url')
        emb.add_field(name ='{}```_exc_ NAME```'.format(settings['PREFIX']), value = 'Полноценная экскурсия по серверу(adm)')
        emb.add_field(name ='{}```_list_```'.format(settings['PREFIX']), value = 'Список учатсников сервера(adm)')
        emb.add_field(name ='{}```_exc_adm_ NAME EXC(int) speed(int)```'.format(settings['PREFIX']), value = '_exc_ + изменение скорости и кол-ва заходов(adm)')
        #   emb.add_field(name ='{}```_exc_adm_gogi_ NAME CH(int)```'.format(settings['PREFIX']), value = 'Дополненная экскурсия - версия @gogi')
        emb.add_field(name ='{}```_mute_ NAME```'.format(settings['PREFIX']), value = 'Мут участника (adm)')
        emb.add_field(name ='{}```_dea_ NAME```'.format(settings['PREFIX']), value = 'Оглушение участника (adm)')
        emb.add_field(name ='{}```_am_ NAME```'.format(settings['PREFIX']), value = 'Полный мут участника (adm)')
        emb.add_field(name ='{}```_aum_ NAME```'.format(settings['PREFIX']), value = 'Полный размут участника (adm)')
        emb.add_field(name ='{}```_lock_ NAME```'.format(settings['PREFIX']), value = 'Унижение участника (adm, 30 сек)')
        emb.add_field(name ='{}```_unlock_ NAME```'.format(settings['PREFIX']), value = 'Помилование участника (adm)')
        emb.add_field(name ='{}```_list_```'.format(settings['PREFIX']), value = f'Список участников сервера { ctx.guild.name } ')
        emb.add_field(name ='{}```_lat_ NAME```'.format(settings['PREFIX']), value = 'Бесконечное унижение (adm, lock all time)')
        emb.add_field(name ='{}```_ulat_ NAME```'.format(settings['PREFIX']), value = 'Помилование участника (adm, un lock all time)')
        emb.add_field(name ='{}```_warn_ NAME REASON```'.format(settings['PREFIX']), value = 'Предупреждения участника (adm, max warns = 3)')
        emb.add_field(name ='{}```_unwarn_ NAME```'.format(settings['PREFIX']), value = 'Отмена предупреждения (adm)')
        print(f'[help] ${bot.user.name} sent a help list for {ctx.message.author.name} ({ctx.message.author.nick})')
        await ctx.send ( embed = emb )

    #only_big_adm (шучу)
    #=================================================

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def send_on_machine(ctx):
        await ctx.send(input('message: '))

    async def greatSender():
        channel = bot.get_channel(id=int(input('channel_ID: ')))
        await channel.send(input('message: '))

    @bot.event
    async def on_ready():
        print('\n')
        for i in threading.enumerate():
            print(f'{i} Running')
        print('\nWork Status: 1\n\nAuditor magazine of bot:\n')
        print(f'\nLogged in as {bot.user.name}')
        activity = discord.Game(name='$_help_ | ShG')
        await bot.change_presence(status=':rainbowpartner:', activity=activity)

    #=================================================

    bot.run(settings['TOKEN'])

except: print('\nWork status: 0')

finally:
    print('\nWell done :)\n')
    

#D✔Бот for discord channel
#NzIxODQ2ODk5OTg0MDM5OTY5.Xuaeyg.08dfDqsAcWxBDv6wAfXxkXe_fCg'
#https://discord.com/developers/applications/721846899984039969/information 
