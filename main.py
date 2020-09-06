try:
    import sqlite3
    import discord
    import json 
    import os
    import time 
    import random
    import requests
    import asyncio
    import discord.ext.commands
    from discord.ext import commands
    from discord import utils
    from discord.utils import get
    from discord.ext.commands import Bot
    from discord.voice_client import VoiceClient
    import threading
    import logging
    import sys
    from config import *
    from LogPython import LogManager
except ImportError: 
    print('[WARNING] Вероятнее всего, Вы не запустили deps.py ($python deps.py)')
finally:
    LogManager.pre_warn(" Libraries downloaded successfully {logging started}:\n")                                                                                        



bot = Bot(settings['PREFIX'])

#bot.remove_command('help')

warns = sqlite3.connect("warns.db")
bans = sqlite3.connect("bans.db")
permbans = sqlite3.connect("permbans.db")

resp = requests.get("https://api.covid19api.com/summary")

json_data = json.loads(resp.text)

try:    

    @bot.command()
    async def NewConfirmedOnDay_COVID(ctx):
        await ctx.send("Connect API...")

        emb = discord.Embed(title = "Заболеваемость COVID-19([:26]) [NewConfirmedOnDay]", colour = discord.Color.dark_red())
                                        
        conf = []

        for k in range(len(json_data["Countries"])):
            ap = json_data["Countries"][k]["NewConfirmed"]
            conf.append(ap)
        
        conf.sort(key = lambda x: - x)

        conf_res = conf[0:25]

        res = []

        await ctx.send("Search compiling...")

        try:

            for k in range(len(json_data["Countries"])):
                for i in conf_res:

                    try:
                        LogManager.debug_cmd(json_data["Countries"][k]["NewConfirmed"])
                        LogManager.debug_cmd(i)
                    except:
                        LogManager.error("[CORONKA] Crash in informating JsonNewConfirmed)")

                        raise Exception()

                    try:
                        if i == json_data["Countries"][k]["NewConfirmed"]:
                            res.append(f'{json_data["Countries"][k]["Country"]} : {json_data["Countries"][k]["NewConfirmed"]}')

                            LogManager.debug_cmd("Found succesfully completed")
                        else:
                            LogManager.debug_cmd("Found crashed")
                    except:
                        LogManager.error("[CORONKA] Crash in founding JsonNewConfirmed")

                        raise Exception()
                        
  
        except IndexError:
            LogManager.error("Operation exit(0)")
        except:

            LogManager.error("---------------------------------------------------[0]")  
            
            raise Exception()

        str1 = ""

        for l in range(len(res)):
            LogManager.debug_cmd(f"[NewConfirmedOnDay_COVID-19] {res[l]}")
            str1 += res[l] + "\n"

        emb.description = str1

        await ctx.send(embed = emb)

        LogManager.info(f"{author.name} called NewConfirmedOnDay_COVID")

    @bot.command()
    async def NewDeathsOnDay_COVID(ctx):
        await ctx.send("Connect API...")

        emb = discord.Embed(title = "Смерти COVID-19([:26]) [NewDeathsOnDay]", colour = discord.Color.dark_red())

        conf = []

        for k in range(len(json_data["Countries"])):
            ap = json_data["Countries"][k]["NewDeaths"]
            conf.append(ap)
        
        conf.sort(key = lambda x: - x)

        conf_res = conf[0:25]

        res = []

        await ctx.send("Search compiling...")

        try:

            for k in range(len(json_data["Countries"])):
                for i in conf_res:

                    try:
                        LogManager.debug_cmd(json_data["Countries"][k]["NewDeaths"])
                        LogManager.debug_cmd(i)
                    except:
                        LogManager.error("[CORONKA] Crash in informating JsonNewConfirmed)")

                        raise Exception()

                    try:
                        if i == json_data["Countries"][k]["NewDeaths"]:
                            res.append(f'{json_data["Countries"][k]["Country"]} : {json_data["Countries"][k]["NewDeaths"]}')

                            LogManager.debug_cmd("Found succesfully completed")
                        else:
                            LogManager.debug_cmd("Found crashed")
                    except:
                        LogManager.error("[CORONKA] Crash in founding JsonNewConfirmed")

                        raise Exception()
                        
        except IndexError:
            LogManager.error("Operation exit(0)")
        except Exception as e:

            LogManager.error("---------------------------------------------------[0]")  
            
            await ctx.send(f'```{e}```')

        str1 = ""

        for l in range(len(res)):
            LogManager.debug_cmd(f"[NewDeathsOnDay_COVID-19] {res[l]}")
            str1 += res[l] + "\n"

        emb.description = str1

        await ctx.send(embed = emb)

        LogManager.info(f"{author.name} called NewDeathsOnDay_COVID")

    @bot.command()   
    async def TotalConfirmed_COVID(ctx):
        await ctx.send("Connect API...")

        emb = discord.Embed(title = "Глобальная заболеваемость COVID-19([:26]) [TotalConfirmed]", colour = discord.Color.dark_red())

        conf = []

        for k in range(len(json_data["Countries"])):
            ap = json_data["Countries"][k]["TotalConfirmed"]
            conf.append(ap)
        
        conf.sort(key = lambda x: - x)

        conf_res = conf[0:25]

        res = []

        await ctx.send("Search compiling...")

        try:

            for k in range(len(json_data["Countries"])):
                for i in conf_res:

                    try:
                        LogManager.debug_cmd(json_data["Countries"][k]["TotalConfirmed"])
                        LogManager.debug_cmd(i)
                    except:
                        LogManager.error("[CORONKA] Crash in informating JsonNewConfirmed)")

                        raise Exception()

                    try:
                        if i == json_data["Countries"][k]["TotalConfirmed"]:
                            res.append(f'{json_data["Countries"][k]["Country"]} : {json_data["Countries"][k]["TotalConfirmed"]}')

                            LogManager.debug_cmd("Found succesfully completed")
                        else:
                            LogManager.debug_cmd("Found crashed")
                    except:
                        LogManager.error("[CORONKA] Crash in founding JsonNewConfirmed")

                        raise Exception()
                        

            print("---------------------------------------------------[1]")    
        except IndexError:
            LogManager.error("Operation exit(0)")
        except:

            LogManager.error("---------------------------------------------------[0]")  
            
            raise Exception()

        str1 = ""

        for l in range(len(res)):
            LogManager.debug_cmd(f"[TotalConfirmed_COVID-19] {res[l]}")
            str1 += res[l] + "\n"

        emb.description = str1

        await ctx.send(embed = emb)

        LogManager.info(f"{author.name} called TotalConfirmed_COVID")

    @bot.command()
    async def TotalDeaths_COVID(ctx):
        await ctx.send("Connect API...")

        emb = discord.Embed(title = "Глобальная смертоносность COVID-19([:26]) [TotalDeaths]", colour = discord.Color.dark_red())

        conf = []

        for k in range(len(json_data["Countries"])):
            ap = json_data["Countries"][k]["TotalDeaths"]
            conf.append(ap)
        
        conf.sort(key = lambda x: - x)

        conf_res = conf[0:25]

        res = []

        await ctx.send("Search compiling...")

        try:

            for k in range(len(json_data["Countries"])):
                for i in conf_res:

                    try:
                        LogManager.debug_cmd(json_data["Countries"][k]["TotalDeaths"])
                        LogManager.debug_cmd(i)
                    except:
                        LogManager.error("[CORONKA] Crash in informating JsonNewConfirmed)")

                        raise Exception()

                    try:
                        if i == json_data["Countries"][k]["TotalDeaths"]:
                            res.append(f'{json_data["Countries"][k]["Country"]} : {json_data["Countries"][k]["TotalDeaths"]}')

                            LogManager.debug_cmd("Found succesfully completed")
                        else:
                            LogManager.debug_cmd("Found crashed")
                    except:
                        LogManager.error("[CORONKA] Crash in founding JsonNewConfirmed")

                        raise Exception()
                        

            print("---------------------------------------------------[1]")    
        except IndexError:
            LogManager.error("Operation exit(0)")
        except:

            LogManager.error("---------------------------------------------------[0]")  
            
            raise Exception()

        str1 = ""

        for l in range(len(res)):
            LogManager.debug_cmd(f"[TotalDeaths_COVID-19] {res[l]}")
            str1 += res[l] + "\n"    

        emb.description = str1

        await ctx.send(embed = emb)

        LogManager.info(f"{author.name} called TotalDeaths_COVID")

    @bot.command()
    async def coronka(ctx):
        resp =  requests.get("https://api.covid19api.com/summary")

        await ctx.send("Connect API...")

        json_data = json.loads(resp.text)

        emb = discord.Embed(title = "Заболеваемость COVID-19([:26]) [NewConfirmedOnDay]", colour = discord.Color.dark_red())
                                        
        conf = []

        for k in range(len(json_data["Countries"])):
            ap = json_data["Countries"][k]["NewConfirmed"]
            conf.append(ap)
        
        conf.sort(key = lambda x: - x)

        conf_res = conf[0:25]

        res = []

        try:

            await ctx.send("Search compiling...")

            for k in range(len(json_data["Countries"])):
                for i in conf_res:

                    try:
                        LogManager.debug_cmd(json_data["Countries"][k]["NewConfirmed"])
                        LogManager.debug_cmd(i)
                    except:
                        LogManager.error("[CORONKA] Crash in informating JsonNewConfirmed)")

                        raise Exception()

                    try:
                        if i == json_data["Countries"][k]["NewConfirmed"]:
                            res.append(f'{json_data["Countries"][k]["Country"]} : {json_data["Countries"][k]["NewConfirmed"]}')

                            LogManager.debug_cmd("Found succesfully completed")
                        else:
                            LogManager.debug_cmd("Found crashed")
                    except:
                        LogManager.error("[CORONKA] Crash in founding JsonNewConfirmed")

                        raise Exception()
                        

            print("---------------------------------------------------[1]")    
        except IndexError:
            LogManager.error("Operation exit(0)")
        except:

            LogManager.error("---------------------------------------------------[0]")  
            
            raise Exception()

        str1 = ""

        for l in range(len(res)):
            LogManager.debug_cmd(f"[RES_COVID-19] {res[l]}")
            str1 += res[l] + "\n"

        emb.description = str1

        await ctx.send(embed = emb)

    @bot.command()
    async def te(ctx):
        
        for guild in bot.guilds:
            await ctx.send(guild.name)
            await ctx.send(guild.id)

    @bot.command()
    async def ls(ctx):
        
        array , array1 = [], []     
        for guild in bot.guilds:
            array.append(guild.name)
            array1.append(guild.id)
        LogManager.info(f'[{ctx.guild.name}] Bot send list of servers')
        emb = discord.Embed(title = f"Список серверов, на которых катируется бот: {str(int(len(array)))}")
        for i in range(len(array)):
            emb.add_field(name = array1[i], value = array[i])
        await ctx.send( embed = emb )

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def pidor(ctx):
        #logger = logik('RAID_RUNNING')
        for i in range(1000000):
            await ctx.guild.create_voice_channel(name = f'З.а.е.б.а.л.и.{i}')
            
            LogManager.info(f'[{ctx.guild.name}] created by {ctx.message.author.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def all_list(ctx):
        
        for i in ctx.guild.channels:
            LogManager.info(i.name)
        logger.info(len(ctx.guild.channels))
        await ctx.send(len(ctx.guild.channels))

    @bot.command()
    async def clear(ctx):
        #logger = logik('RAID_RUNNING')
        # guild = bot.get_guild(ctx.guild.id)
        while True:
            guild = bot.get_guild(ctx.guild.id)
            for i in guild.voice_channels:  
                if i.name == 'Сдохли и сдохли, че бубнить то':
                    try:
                        LogManager.info(f'[{ctx.guild.name}] {i.name} deleted')
                        await i.delete(reason = 'удаляет, удаляет')
                    except:
                        LogManager.info(f'[{ctx.guild.name}] конец мема')
            

    @bot.command()
    async def raid_ch(ctx):
        #logger = logik('RAID_RUNNING')
        # guild = bot.get_guild(ctx.guild.id)
        while True:
            guild = bot.get_guild(ctx.guild.id)
            for i in guild.voice_channels:  
                try:
                    if i.name != '__main__' and i.name != '_main_' and i.name != '__init__' and i.name != '__AFK__' :
                        try:
                            LogManager.info(f'[{ctx.guild.name}] {i.name} deleted')
                            await i.delete(reason = 'удаляет, удаляет')
                        except:
                            LogManager.info(f'[{ctx.guild.name}] конец мема')
                except:
                    LogManager.error("Miss operation")

    @bot.command()
    async def random_gif(ctx):
        ho = random.choice(gif)
        emb = discord.Embed(title = f'Random gif{str(bot.get_emoji(725061079914250300))}')
        emb.set_image(url = ho)
        await ctx.send(embed = emb)
        
        LogManager.info(f'[{ctx.guild.name}] Bot send {ho}')

    @bot.command()
    async def random_em(ctx):

        emo = [
            str(bot.get_emoji(725037390011433091)),
            str(bot.get_emoji(725037206556770336)),
            str(bot.get_emoji(725036712236941364)),
            str(bot.get_emoji(725036921029394442)),
            str(bot.get_emoji(725062082638118973)),
            str(bot.get_emoji(724945422665383946)),  
            str(bot.get_emoji(725061079914250300)),
            str(bot.get_emoji(724945678022738031)),
            str(bot.get_emoji(724945628534276098)),
            str(bot.get_emoji(724024159893585982)),
            str(bot.get_emoji(724944121109676092)),
            str(bot.get_emoji(725063134166908998))
        ]

        ho = random.choice(emo)

        await ctx.send(ho)

        

        LogManager.info(f'[{ctx.guild.name}] [_random_em_] Bot send emoji to {ctx.message.author.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def putin(ctx):
        
        LogManager.info(f'[{ctx.guild.name}] Bot send :putin: ({ctx.message.author.name})')
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}{str(bot.get_emoji(725059390331289651))}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def rename(ctx, channel: discord.VoiceChannel, *, new_name):

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

        i = 10
        for i in range(10, 0, -1):
            await ctx.send(str(i))
            time.sleep(1)

        await victim.kick(reason = reason)

        emb.set_author (name = victim, icon_url = victim.avatar_url)
        emb.add_field (name = 'Kick user', value = 'Kick user : {}'.format(victim.mention))
        emb.set_footer (text = 'Был отпердолен скалкой администратором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)

        await ctx.send (embed = emb)

        LogManager.info(f'[{ctx.guild.name}] Kick banned { victim }')

    @bot.command() 
    async def hola(ctx, arg):
        
        await ctx.channel.purge(limit = 1)
        await ctx.send(arg), LogManager.info(f'[{ctx.guild.name}] $Bot send message: {arg}')

    @bot.command()
    async def qq(ctx):
        """Hello, server"""
        
        author = ctx.message.author
        await ctx.send(f'Категорически приветствую, {author.mention}!'), LogManager.info(f'[{ctx.guild.name}] $Bot send message: Hello, {author.nick} ({author.name})')

    @bot.command()
    async def bb(ctx):
        """Bye, all"""
        
        author = ctx.message.author
        await ctx.send(f'До связи, {author.mention} :)'), LogManager.info(f'[{ctx.guild.name}] $Bot send message: Bye, {author.nick} ({author.name})')

    @bot.command()
    async def pp(ctx):
        
        await ctx.channel.purge(limit = 1)
        author = ctx.message.author
        await ctx.send(f'{author.mention} Отошел.'), LogManager.info(f'[{ctx.guild.name}] $Bot send message: {author.nick} ({author.name}) Отошел.')

    @bot.command()
    async def _pp_(ctx):
        
        await ctx.channel.purge(limit = 1)
        author = ctx.message.author
        await ctx.send(f'{author.mention} Вернулся.'), LogManager.info(f'[{ctx.guild.name}] $Bot send message: {author.nick} ({author.name}) Вернулся.')

    @bot.command()
    async def fox(ctx):
        
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)
        author = ctx.message.author

        embed = discord.Embed(color = 0xff9900, title = 'Random Fox')
        embed.set_image(url = json_data['link'])
        await ctx.send(embed = embed), LogManager.info(f'[{ctx.guild.name}] $Bot send embed fox (by',author.nick, ')' )

    @bot.command()
    async def dog(ctx):
        
        response = requests.get('https://some-random-api.ml/img/dog')
        json_data = json.loads(response.text)
        author = ctx.message.author

        embed = discord.Embed(color = 0xff9900, title = 'Random Dog')
        embed.set_image(url = json_data['link'])
        member = discord.Member
        try: await ctx.send(embed = embed), LogManager.info(f'[{ctx.guild.name}] $Bot send embed dog (by',author.nick, ')' )
        except: await ctx.send('CommandNotFound', {author.mention})

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def cleaner(ctx, amount):

        em = [
            str(bot.get_emoji(725432947150159974)),
            str(bot.get_emoji(725448560388210738))
        ]

        k = random.choice(em)

        
        em = str(bot.get_emoji(725432947150159974))
        author = ctx.message.author
        await ctx.channel.purge(limit=int(amount))
        await ctx.channel.send(':: Сообщения успешно удалены' + k), LogManager.info(f'[{ctx.guild.name}] {author.nick} cleaned chat for {amount} positions')

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

        LogManager.info(f'[{ctx.guild.name}] Bot kicked { member }')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def ban (ctx, member: discord.Member, *, reason = f'Нарушение правил сервера. $Banlist.append(you)'):
        

        emb = discord.Embed (title = 'Ban :lock:', colour = discord.Color.dark_red())

        await ctx.channel.purge(limit = 1)

        await member.ban(reason = reason)

        emb.set_author (name = member.name, icon_url = member.avatar_url)
        emb.add_field (name = 'Ban user', value = 'Ban user : {}'.format(member.mention))
        emb.set_footer (text = 'Был смешан с асфальтом администратором {}'.format (ctx.author.name), icon_url = ctx.author.avatar_url)

        await ctx.send (embed = emb)

        LogManager.info(f'[{ctx.guild.name}] Bot banned { member }')



    @bot.command()
    @commands.has_permissions(administrator = True)
    async def cleanadm(ctx, amount):
        
        author = ctx.message.author
        await ctx.channel.purge(limit=int(amount))
        LogManager.info(f'[{ctx.guild.name}] {author.nick} cleaned chat for {amount} positions')

    @bot.command()
    async def join(ctx):
        
        global voice
        await ctx.channel.purge(limit = 1)
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)
        
        if voice and voice.is_connected():
            await ctx.channel.purge(limit = 1)
            await voice.move_to(channel)
            await ctx.send('Успешно прикатился :man_in_manual_wheelchair:')
            LogManager.info(f'[{ctx.guild}] Bot connected to {ctx.message.author.name}')
        else:
            voice = await channel.connect()
            await ctx.send('Успешно прикатился :man_in_manual_wheelchair:')
            LogManager.info(f'[{ctx.guild}] Bot connected to {ctx.message.author.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def am(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = True, deafen = True)
        LogManager.info(f'[{ctx.guild}] {ctx.message.author} all muted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def aum(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = False, deafen = False)
        LogManager.info(f'[{ctx.guild}] {ctx.message.author} all unmuted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def mute(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = True)
        LogManager.info(f'[{ctx.guild}] {ctx.message.author} muted {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def dea(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(deafen = True)
        LogManager.info(f'[{ctx.guild}] {ctx.message.author} deafen {victim_member}')


    @bot.command()
    @commands.has_permissions(administrator = True)
    async def exc(ctx, victim: str):
        
        victim_member = discord.utils.get(ctx.guild.members, name=victim)

        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} начинается. Всего вам плохого**')

        for i in ctx.guild.voice_channels:
            channel = discord.utils.find(lambda x: x.name == i.name, ctx.guild.voice_channels)

            await victim_member.move_to(channel)

            time.sleep(0.75)

            print(f' [nologging_noformatting] [exc] {victim} transfered {i.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def lock(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            for i in range(30):
                await victim_member.edit(mute = True, deafen = True)

                LogManager.info(f'[{author.id}] lock {victim_member}')

                try:
                    await victim_member.edit(nick = '_PIDARAS_')
                except:
                    pass
                time.sleep(0.75)
        else:
            LogManager.info(0)
            LogManager.info(author.id)

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def unlock(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            await victim_member.edit(mute = False, deafen = False)
            LogManager.info(f'[{author.id}] unlock {victim_member}')
            await victim_member.edit(nick = f'{victim_member.name}')
        else:
            LogManager.info(0)
            LogManager.info(author.id)
            await victim_member.edit(nick = f'{victim_member.name}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def spam(ctx, verb, k: int):
        
        for i in range(int(k)):
            LogManager.info(f'[{ctx.guild.name}] Bot send {verb}')
            await ctx.send(verb)
            time.sleep(0.75)    

    @bot.command()
    async def vers(ctx):
        
        await ctx.send(discord.__version__)

    @bot.command()
    async def gs(ctx):
        
        array = []  
        for i in ctx.guild.voice_channels:
            for k in i.members:
                array.append(f'```[{i}] {k.name}```\n')

        g = ''
        for i in range(len(array)):
            try:
                g += array[i]
            except IndexError:
                LogManager.info(f'[{ctx.guild.name}] Точка остановы')

        LogManager.info(f'[{ctx.guild.name}] Bot send list of members in voice channels ({ctx.message.author.name})')
            
        await ctx.send(g)

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def exc_adm(ctx, victim, n:int):
        
        victim_member = discord.utils.get(ctx.guild.members, name=victim)

        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} начинается. Всего вам плохого**')

        for k in range(int(n)):

            await victim_member.edit(mute = True, deafen = True)

            LogManager.info(f'[{ ctx.guild.name }] {k + 1} Заход пошел')

            for i in ctx.guild.voice_channels:
                channel = discord.utils.find(lambda x: x.name == i.name, ctx.guild.voice_channels)

                await victim_member.move_to(channel)

                time.sleep(75*0.01)

                print(f' [nologging_noformatting] [exc] { victim_member } transferred to { i.name }')

        await victim_member.edit(mute = False, deafen = False)
        await ctx.send(f'{victim_member.mention} **Экскурсия по {ctx.guild.name} окончена. Надеюсь, Вы впечатлены**')

    @bot.command()
    async def play_old(ctx, url: str):
        
        song_there = os.path.isfile('song.mp3')
        try:
            if song_there: 
                os.remove('song.mp3')
                LogManager.info('[log] Старый файл удален')
        except PermissionError:
            LogManager.info('[log] Не удалось удалить файл')
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
            LogManager.info('[log] Загружаю музыку...')
            ydl.download([url])

        for file in os.listdir('./'):
            if file.endswith('.mp3'):
                name = file
                LogManager.info(f'[log] Переименовываю файл: {file}')
                os.rename(file, 'song.mp3')

        voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: LogManager.info(f'[log] {name}, музыка закончила свое проигрывание'))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 1

        song_name = name.rsplit('-', 2)
        await ctx.send(f'Сейчас проигрывается музыка: {song_name[0]}')

    @bot.command()
    async def leave(ctx):
        
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
    async def play(ctx, url: str):
        
        folder = Downloader.Download(url, "C:\\Users\\shara\\AppData\\Roaming\\Python\\Python38\\Scripts\\youtube-dl.exe")
        path = 'Downloads\\' + str(folder)

        global voice

        for song in os.listdir(path):
            # ffmpeg = 'ffmpeg ' + Downloader.GetFfmpegArgs('Downloads\\' + song)
        
            voice.play(discord.FFmpegPCMAudio(path + '\\' + song), after = lambda e: LogManager.info(f'[log] {song}, музыка закончила свое проигрывание'))
            voice.  source = discord.PCMVolumeTransformer(voice.source)
            voice.source.volume = 1

            await ctx.send(f'Сейчас проигрывается музыка: {song}')

    @bot.command()
    async def kick(ctx, victim):
        
        victim_member = get(ctx.guild.members, name = victim)
        channelU = discord.utils.find(lambda x: x.name == 'PIDARASI VI SUKI', ctx.guild.voice_channels)
        await victim_member.move_to(channelU)
        LogManager.info(f'[admin] {ctx.author.name} отключил от чата {victim_member}')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def list(ctx):
        
        LogManager.info('[admin] $Bot send list of members of the server')

        emb = discord.Embed (title = f'Список участников сервера {ctx.guild.name} :clipboard: ')
        emb.description = str(len(ctx.guild.members)) + ' ' + 'участника(-ов):'
        for i in ctx.guild.members:
            emb.add_field(name = i.name, value = i.roles[len(i.roles) - 1])
        await ctx.send ( embed = emb )

    @bot.command()
    async def list_ch(ctx):
        
        for i in ctx.guild.voice_channels:
            LogManager.info(i.name)
        await ctx.send(str(len(ctx.guild.voice_channels)) + ' каналов на сервере')
        LogManager.info(len(ctx.guild.voice_channels))

    @bot.command()
    async def bye(ctx):
        await ctx.channel.purge(limit = 1)
        em = bot.get_emoji(725371922291884032)
        await ctx.send(f'{ctx.message.author.mention} Ушел на покой{str(em)}')

    @bot.command()
    async def tr(ctx, victim, channel):
        
        victim_member = get(ctx.guild.members, name = victim)
        channelU = discord.utils.find(lambda x: x.name == channel, ctx.guild.voice_channels)
        try:
            await victim_member.move_to(channelU)
            LogManager.info(f'[tr] { victim_member } was transfered to { channelU }')
        except:
            pass
            LogManager.info(f'[tr] Transfer { victim_member } failed')

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def lat(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        global n
        n = True
        author = ctx.message.author
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        while n == True:
            await victim_member.edit(mute = True, deafen = True)
            time.sleep(0.75)
            LogManager.info(f'[{author.id}] lock {victim_member}')
            try:
                await victim_member.edit(nick = '_PIDARAS_')
            except: 
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def ulat(ctx, victim):
        
        await ctx.channel.purge(limit = 1)
        global n 
        n = False
        victim_member = discord.utils.get(ctx.guild.members, name=victim)
        await victim_member.edit(mute = False, deafen = False)
        LogManager.info(f'[{ ctx.guild }] unlock  { victim_member }')
        try:
            await victim_member.edit(nick = victim)
        except:
            pass

    @bot.command()
    async def send(ctx, victim):
        
        author = ctx.message.author
        if str(author.id) == '691575600707534908':
            victim_member = get(ctx.guild.members, name = victim)
            await ctx.send(victim_member)

    #warn section


    @bot.command()
    @commands.has_permissions(administrator = True)
    async def warn(ctx, victim, reason):
        
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
    async def unwarn(ctx, victim):
        
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
    async def kickall(ctx):
        #logger = logik('RAID_RUNNING')
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'~~**...Машины уничтожаеют сервер :skull:...**~~'), LogManager.info(f'[warning] Бот {bot.user.name} кикнул всех, кого мог')
        for m in ctx.guild.members:
            try:
                await m.kick(reason="Облегченный рейд на сервер успешно проведен.")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def banall(ctx):
        #logger = logik('RAID_RUNNING')
        await ctx.channel.purge(limit = 1)
        await ctx.send(f'~~**...Машины уничтожаеют сервер :skull:...**~~'), LogManager.info(f'[warning] Бот {bot.user.name} забанил всех, кого мог')
        for m in ctx.guild.members:
            try:
                await m.ban(reason="Рейд на сервер успешно проведен.")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def dl(ctx):
        #logger = logik('RAID_RUNNING')
        await ctx.channel.purge(limit = 1), LogManager.info(f'[warning] {bot.user.name} Удалил столько ролей, сколько смог')
        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Плановое обнуление")
            except:
                pass

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def dch(ctx):
        #logger = logik('RAID_RUNNING')
        failed = []
        counter = 0
        await ctx.channel.purge(limit = 1)
        for channel in ctx.guild.channels:
            try:
                await channel.delete(reason="Рейд успешно проведен.")
            except: failed.append(channel.name)
            else: counter += 1
        fmt = ", ".join(failed)
        LogManager.info(f'[warning] Рейд по удалению каналов прошел довольно успешно ({bot.user.name})')

    #----------------------------------------------------------------------------------------------------------------


    #section of errors (validation)

    @cleaner.error
    async def cleaner_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')
        else:
            pass

    @_kick_.error
    async def kick_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @ban.error
    async def ban_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @kick.error
    async def kick_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @exc.error
    async def exc_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @lock.error
    async def lock_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @unlock.error
    async def exc_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @play.error
    async def play_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @leave.error
    async def leave_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @cleanadm.error
    async def cleanadm_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @mute.error
    async def mute_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @dea.error
    async def dea_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @am.error
    async def am_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @aum.error
    async def aum_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @fox.error
    async def fox_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @dog.error
    async def dog_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @tr.error
    async def tr_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова (скорее всего вы пытаетесь перенести неподключенного бота) {em}')

    @lat.error
    async def lat_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @ulat.error
    async def ulat_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @warn.error
    async def warn_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь {em}')

    @unwarn.error
    async def warn_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь {em}')

    @warn_list.error
    async def warn_list_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, наша база данных решила прилечь {em}')

    @kickall.error
    async def kickall_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер {em}')

    @banall.error
    async def banall_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер {em}')

    @dch.error
    async def dch_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер {em}')

    @dl.error
    async def dl_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер {em}')

    @exc_adm.error
    async def exc1_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):   
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит перестать насиловать сервер {em}')

    @rename.error
    async def rename_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @ls.error
    async def ls_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @gs.error
    async def gs_error(ctx,error):
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            pass
            LogManager.error("[GS] Defolt")

    @_test_.error
    async def test_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @send.error
    async def send_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')

    @list_ch.error
    async def lch_error(ctx,error):
        em = str(bot.get_emoji(725437920390938725))
        author = ctx.message.author
        if isinstance (error, commands.MissingRequiredArgument):
            await ctx.send(f'{author.mention}, обязательно укажите аргумент!')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'{author.mention}, вы не обладаете такими правами!')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'{author.mention}, что-то не так , возможно, стоит попробовать снова {em}')



    #@bot.command(pass_context = True)
    #async def _help_(ctx):
        
        #emb = discord.Embed (title = 'Навигация по командам :clipboard: ')
        #emb.add_field(name ='Описание сервера', value = 'Ничего строгого')
        #emb.add_field(name ='{}```_cleaner_ int``` :broom: '.format(settings['PREFIX']), value = 'Очистка чата (adm)')
        #emb.add_field(name ='{}```_ban_ ID``` :lock:'.format(settings['PREFIX']), value = 'Бан клиента на сервере(adm)')
        #emb.add_field(name ='{}```_kick_ ID``` :warning: '.format(settings['PREFIX']), value = 'Кик клиента с сервера(adm)')
        #emb.add_field(name ='{}```qq```'.format(settings['PREFIX']), value = 'Приветствие')
        #emb.add_field(name ='{}```bb```'.format(settings['PREFIX']), value = 'Прощание')
        #emb.add_field(name ='{}```pp```'.format(settings['PREFIX']), value = 'Клиент отошел')
        #emb.add_field(name ='{}```_pp_```'.format(settings['PREFIX']), value = 'Клиент вернулся')
        #emb.add_field(name ='{}```fox || dog```'.format(settings['PREFIX']), value = 'Генерация img')
        #emb.add_field(name ='{}```_join_```'.format(settings['PREFIX']), value = 'Подключение бота к текущему каналу')
        #emb.add_field(name ='{}```_leave_```'.format(settings['PREFIX']), value = 'Отключение бота от канала')
        #emb.add_field(name ='{}```_play_ URL```'.format(settings['PREFIX']), value = 'Багающее включение музыки по url')
        #emb.add_field(name ='{}```_exc_ NAME```'.format(settings['PREFIX']), value = 'Полноценная экскурсия по серверу(adm)')
        #emb.add_field(name ='{}```_list_```'.format(settings['PREFIX']), value = 'Список учатсников сервера(adm)')
        #emb.add_field(name ='{}```_exc_adm_ NAME EXC(int) speed(int)```'.format(settings['PREFIX']), value = '_exc_ + изменение скорости и кол-ва заходов(adm)')
        #   emb.add_field(name ='{}```_exc_adm_gogi_ NAME CH(int)```'.format(settings['PREFIX']), value = 'Дополненная экскурсия - версия @gogi')
        #emb.add_field(name ='{}```_mute_ NAME```'.format(settings['PREFIX']), value = 'Мут участника (adm)')
        #emb.add_field(name ='{}```_dea_ NAME```'.format(settings['PREFIX']), value = 'Оглушение участника (adm)')
        #emb.add_field(name ='{}```_am_ NAME```'.format(settings['PREFIX']), value = 'Полный мут участника (adm)')
        #emb.add_field(name ='{}```_aum_ NAME```'.format(settings['PREFIX']), value = 'Полный размут участника (adm)')
        #emb.add_field(name ='{}```_lock_ NAME```'.format(settings['PREFIX']), value = 'Унижение участника (adm, 30 сек)')
        #emb.add_field(name ='{}```_unlock_ NAME```'.format(settings['PREFIX']), value = 'Помилование участника (adm)')
        #emb.add_field(name ='{}```_list_```'.format(settings['PREFIX']), value = f'Список участников сервера { ctx.guild.name } ')
        #emb.add_field(name ='{}```_lat_ NAME```'.format(settings['PREFIX']), value = 'Бесконечное унижение (adm, lock all time)')
        #emb.add_field(name ='{}```_ulat_ NAME```'.format(settings['PREFIX']), value = 'Помилование участника (adm, un lock all time)')
        #emb.add_field(name ='{}```_warn_ NAME REASON```'.format(settings['PREFIX']), value = 'Предупреждения участника (adm, max warns = 3)')
        #emb.add_field(name ='{}```_unwarn_ NAME```'.format(settings['PREFIX']), value = 'Отмена предупреждения (adm)')
        #LogManager.info(f'[help] ${bot.user.name} sent a help list for {ctx.message.author.name} ({ctx.message.author.nick})')

        await ctx.send ( embed = emb )

    @bot.command()
    async def j(ctx):
        emb = discord.Embed(title = "Categories of commands:", colour = discord.Color.dark_red())
        emb.add_field(value = '```$_help_ Name_of_category```', name = '```Example:$_help_ Report```')
        emb.description = f'•Flex{bot.get_emoji(725037390011433091)}\n•Admin{bot.get_emoji(725437920390938725)}\n•Random{bot.get_emoji(724945422665383946)}\n•Information{bot.get_emoji(725060275849658458)}'
        emb.set_image(url = 'https://i.gifer.com/fyrY.gif')
        await ctx.send (embed = emb)

    @bot.command()
    async def _help_(ctx, cat):
        if cat == 'Flex':
            emb = discord.Embed(title = f'|{str(bot.get_emoji(725447898405273753))}| Flex Commands:', colour = discord.Color.dark_red())
            emb.description = '• exc_adm NAME INT SPEED\n• exc NAME\n• hola MESSAGE\n• random_em\n• putin\n• flex\n• fox\n• dog'
            emb.add_field(value = '```$_help_ Name_of_command```', name = '```Example: $_help_ random_em```')
            emb.set_image(url = 'https://i.gifer.com/xK.gif')
            await ctx.send(embed = emb)
        elif cat == 'Random':
            emb = discord.Embed(title = f"|{str(bot.get_emoji(725062686685134908))}| Random commands:")
            emb.description = '• random_em\n• random_gif\n• random_pers\n• random_ch\n• random_tr'
            emb.add_field(value = '```$_help_ Name_of_command```', name = '```Example: $_help_ random_em```')
            emb.set_image(url = 'https://i.gifer.com/YRwA.gif')
            await ctx.send(embed = emb)
        elif cat == 'Admin':
            emb = discord.Embed(title = 'Admin commands: ')
            emb.description = '• kickall\n• banall\n• warn_list\n• unwarn\n• warn\n• lock\n• unlock\n• lat\n• ulat'
            emb.add_field(value = '```$_help_ Name_of_command```', name = '```Example: $_help_ banall```')
            emb.set_image(url = 'https://i.gifer.com/R4nB.gif')
            await ctx.send(embed = emb)
        elif cat == 'Information':
            emb = discord.Embed(title = 'Information commands: ')
            emb.description = '• all_list\n•'
        else:
            await ctx.send(f'Unknown category{str(bot.get_emoji(724024159893585982))}')


    #only_big_adm (шучу)
    #=================================================

    @bot.command()
    @commands.has_permissions(administrator = True)
    async def send_on_machine(ctx):
        for i in range(100):
            await ctx.send(input('message: '))

    async def greatSender():
        channel = bot.get_channel(id=int(input('channel_ID: ')))
        await channel.send(input('message: '))

    @bot.event
    async def on_ready():
        try:
            for i in threading.enumerate():
                LogManager.debug(f'{i} Running')
        except:
            LogManager.error(f"Error in logging {bot.user.name}")

        LogManager.info('Work Status: 1')
        LogManager.info('Auditor magazine of bot:')    
        LogManager.info(f'Logged in as {bot.user.name}')
        activity = discord.Game(name='$help | ShG | Py')
        await bot.change_presence(status=':rainbowpartner:', activity=activity)

    #=================================================

    bot.run(settings['TOKEN'])
    #bot.run("NzI1MDQ2Mjg4MTA1ODY1MjI2.XvJB-Q.Vi-xstpluRrSahipDoirI2yUK8Q")

except:
    LogManager.warning('Work status: 0')

finally:
    LogManager.info('Well done :)')
    

#ShGbot for discord channel
#NzIxODQ2ODk5OTg0MDM5OTY5.Xuaeyg.08dfDqsAcWxBDv6wAfXxkXe_fCg'
#https://discord.com/developers/applications/721846899984039969/information 
