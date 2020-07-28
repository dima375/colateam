import discord
from discord.ext import commands
import datetime
import asyncio
from discord.utils import get
import random
from discord.utils import get
import os


PREFIX = '.'


client = commands.Bot( command_prefix = PREFIX )
client.remove_command("help")


@client.event

async def on_ready():
	print( 'BOT connect' )

	await client.change_presence( status = discord.Status.online, activity = discord.Game( '.help' ) )


@client.event
async def on_member_join( member: discord.Member ):
	time_now = datetime.datetime.now().strftime("%H:%M")
	channel = client.get_channel( 728523420400353381 )
	emb = discord.Embed( title ='_**ЗАШЁЛ НА СЕРВЕР**_:wink:', description = f"**Информация о новом пользователе:\n `{member.name}`**  ({member.mention})**зашёл на наш крутой сервер!**:wave:", colour = discord.Color.red() )
	emb.set_thumbnail(url=member.avatar_url)
	emb.set_footer( text = f"ID участника: {member.id}" )

	await channel.send( embed = emb ) 

@client.event

async def on_member_remove( member: discord.Member ):
	time_now = datetime.datetime.now().strftime("%H:%M")
	channel = client.get_channel( 732638194092474500 )
	emb = discord.Embed( title = '_**ПОКИНУЛ СЕРВЕР**_:sob:', description = f"**Информация о пользователе:\n `{member.name}`** ({member.mention})**покинул наш крутой сервер!**", colour = discord.Color.red() ) 
	emb.set_thumbnail(url= member.avatar_url )
	emb.set_footer( text = f"ID участника: {member.id}" )

	await channel.send( embed = emb )

# Clear message
@client.command( pass_context = True )
@commands.has_any_role('Library Devs', 'Moderators',725345713327964190)

async def clear( ctx, amount : int ):
	await ctx.channel.purge( limit = amount )
	await ctx.channel.purge( limit = 1 )
	
# Ping
@client.command( pass_context = True )

async def ping(ctx):
	emb = discord.Embed( title = '**PONG**', colour = discord.Color.red() ) 
	await ctx.send( embed = emb )

# Info
@client.command( pass_context = True )

async def info( ctx):
	emb = discord.Embed( title = 'Cola_BOT', description = 'Привет! Меня зовут Cola_BOT!\n Я прикольный бот для развлечения с разными вкусностями.Мой префикс ``.`` Чтобы узнать мои функции пропиши ``.help``', colour = discord.Color.red(), timestamp=ctx.message.created_at )

	emb.set_thumbnail( url = 'https://pngicon.ru/file/uploads/cocacola.png' )
	emb.add_field( name = 'Сделано:', value = '10.07.2020' )
	emb.add_field( name = 'Мой создатель:', value = '_𝓓𝓘𝓡𝓔𝓚_#2117', )
	emb.set_footer( text = f"Спасибо за использование нашего бота: {ctx.author.name}", icon_url = ctx.author.avatar_url )
	await ctx.channel.purge( limit = 1 )
	await ctx.send( embed = emb )


@client.command()
async def love( ctx, member: discord.Member = None ):
    emb = discord.Embed( title = f"``{ctx.author}`` обнял игрока ``{member}``", colour = discord.Color.red(), timestamp=ctx.message.created_at ) 	
     
    emb.set_image( url = 'https://avatars.mds.yandex.net/get-pdb/477388/6e284a6c-00e7-4afe-a55f-6d36fca8a177/s1200' )
    emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    await ctx.channel.purge( limit = 1 )        
    await ctx.send( embed = emb )


@client.command()
async def battle( ctx, member: discord.Member = None ):
    if member is None:
        await ctx.send('С кем ты хочешь перестреляться !')
    else:
        a = random.randint(1,2)
        if a == 1:
            emb = discord.Embed( title = f"Победитель - ``{ctx.author}``", color = discord.Color.green() )
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - ``{member}``", color = discord.Color.red() )
            await ctx.send( embed = emb )
        elif member.id == ctx.author.id:
            emb = discord.Embed( title = f"Вы не можете с собой сражаться !", color = discord.Color.red() )
            await ctx.send( embed = emb )
        else:
            emb = discord.Embed( title = f"Победитель - ``{member}``", color = discord.Color.green() )
            await ctx.send( embed = emb )

            emb = discord.Embed( title = f"Проигравший - ``{ctx.author}``", color = discord.Color.red() )
            await ctx.send( embed = emb )

# ServerInfo
@client.command()
async def server(ctx):
	members = ctx.guild.members
	online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
	offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
	idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
	dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
	allchannels = len(ctx.guild.channels)
	allvoice = len(ctx.guild.voice_channels)
	alltext = len(ctx.guild.text_channels)
	allroles = len(ctx.guild.roles)
	embed = discord.Embed(title=f"{ctx.guild.name}", colour = discord.Color.red(), timestamp=ctx.message.created_at)
	await ctx.channel.purge(limit = 1)
	embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
	embed.description=(
		f":timer: Сервер создали **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
		f":flag_white: Регион **{ctx.guild.region}\n\n Глава сервера __{ctx.guild.owner}__\n\n"
		f":tools: Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
		f":green_circle: Онлайн: **{online}**\n\n"
		f":white_circle: Оффлайн: **{offline}**\n\n"
		f":yellow_circle: Отошли: **{idle}**\n\n"
		f":red_circle: Не трогать: **{dnd}**\n\n"
		f":shield: Уровень верификации: **{ctx.guild.verification_level}**\n\n"
		f":bank: Всего каналов: **{allchannels}**\n\n"
		f":loud_sound: Голосовых каналов: **{allvoice}**\n\n"
		f":keyboard: Текстовых каналов: **{alltext}**\n\n"
		f":briefcase: Всего ролей: **{allroles}**\n\n"
		f":slight_smile: Людей на сервере **{ctx.guild.member_count}\n\n"
	)

	embed.set_thumbnail(url=ctx.guild.icon_url)
	embed.set_footer(text=f"ID: {ctx.guild.id}")
	embed.set_footer(text=f"ID Пользователя: {ctx.author.id}")
	await ctx.send(embed=embed)

# Ball
@client.command( pass_context = True )

async def ball( ctx, *, arg):
	words = [ 'Да:thumbsup:', 'Да, конечно:ok_hand:', 'Возможно:wink:', 'Нет:thumbsdown:', 'Нет, конечно:confused:', '100%', 'Не знаю', 'Думаю да:fingers_crossed:', 'Думаю нет', 'Не:punch:']
	r_words = random.choice(words)

	await ctx.send( f'{r_words}')

# Google 
@client.command()
async def google(ctx, *, question):
	url = 'https://google.gik-team.com/?q=' + str(question).replace(' ', '+')
	await ctx.send(f'Так как кое кто не умеет гуглить, я сделал это за него.\n{url}') 

# Kick
@client.command( pass_context = True )
@commands.has_any_role('Library Devs', 'Moderators', 725345713327964190 )
async def kick( ctx, member: discord.Member, reason):
	if member == ctx.message.author:
		await ctx.send(embed = discord.Embed(description = "_**Ты не можешь кикнуть сам себя!**_", colour = discord.Color.orange() ))
		return await ctx.send( embed = emb )

	channel = client.get_channel( 732639862947053588)
	emb = discord.Embed( title = 'Kick:no_entry_sign:', colour = discord.Color.blue(), timestamp=ctx.message.created_at ) 

	await member.kick( reason = reason)

	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Модератор:',value = ctx.message.author.mention )
	emb.add_field( name = 'Нарушитель:',value = member.mention )
	emb.add_field( name = 'Причина:',value = reason )
	emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
	await member.kick()
	await ctx.channel.purge( limit = 1 )
	await channel.send( embed = emb )

# Ban
@client.command( pass_context = True )
@commands.has_any_role('Library Devs', 'Moderators', 725345713327964190 )
async def ban( ctx, member : discord.Member=None, *, reason=None):

	if not member:
		await ctx.send(embed = discord.Embed(description = "_**Укажите юзера**_", colour = discord.Color.orange() ))
		return await ctx.send( embed = emb )

	if member.id == ctx.message.author.id or member.id == ctx.message.guild.me.id:
		emb = discord.Embed( title = '_**Ты не можешь банить роли или себя**_', color = discord.Color.orange() )
		return await ctx.send( embed = emb )

	channel = client.get_channel( 'Library Devs', 'Moderators',732639862947053588)
	emb = discord.Embed( title = 'Ban:no_entry_sign:', colour = discord.Color.blue(), timestamp=ctx.message.created_at )

	await ctx.channel.purge( limit = 1 )

	await member.ban( reason = reason )
  
	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Модератор:',value = ctx.message.author.mention )
	emb.add_field( name = 'Нарушитель:',value = member.mention )
	emb.add_field( name = 'Причина:',value = reason )
	emb.set_thumbnail( url = 'https://1.bp.blogspot.com/-G1DIvx0Msjo/VQMgzX8n4sI/AAAAAAAAACc/5H-pc3WpLSw/s1600/banned.png')
	emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
	await member.ban()
	await channel.send( embed = emb )

# User
@client.command(aliases=['юзер', 'юзеринфо', 'user'])
async def __userinfo( ctx, member: discord.Member):
    roles = member.roles
    role_list = ""
    for role in roles:
        role_list += f"<@&{role.id}> "
    emb = discord.Embed(title=f'Информация о пользователе {member}', colour =discord.Color.red(), timestamp=ctx.message.created_at)
    emb.set_thumbnail(url=member.avatar_url)
    emb.add_field(name='ID', value=member.id)
    emb.add_field(name='Имя', value=member.name)
    emb.add_field(name='Высшая роль', value=member.top_role)
    emb.add_field(name='Тег', value=member.discriminator)
    emb.add_field(name='Присоеденился к серверу', value=member.joined_at.strftime('%Y.%m.%d \n %H:%M:%S'))
    emb.add_field(name='Присоеденился к Discord', value=member.created_at.strftime("%Y.%m.%d %H:%M:%S"))
    emb.add_field(name='Роли', value= len(member.roles))
    emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
    await ctx.send(embed = emb)

# Time
@client.command( pass_context = True )


async def time( ctx ):
	emb = discord.Embed( title = 'Time', colour = discord.Color.red(), url = 'https://time.is/ru/Kyiv')
	
	emb.set_author( name = client.user.name, icon_url = client.user.avatar_url )
	emb.set_footer( text = f"Спасибо за использование нашего бота: {ctx.author.name}", icon_url = ctx.author.avatar_url )
	emb.set_image( url = 'https://s3.tproger.ru/uploads/2015/10/clock-1-770x270.jpg' )
	emb.set_thumbnail( url = 'https://s3.tproger.ru/uploads/2015/10/clock-1-770x270.jpg')

	now_date = datetime.datetime.now()

	emb.add_field( name = 'Time', value = 'time : {}'.format(  now_date ) )

	await ctx.channel.purge( limit = 1 )

	await ctx.send( embed = emb )

# Mute
@client.command( pass_context = True )
@commands.has_any_role( 'Library Devs', 'Moderators',725345713327964190)
async def mute( ctx, member: discord.Member, time: int,reason ):
	if member == ctx.message.author:
		emb = discord.Embed( title = '_**Ты не можешь замьютить сам себя!**_', color = discord.Color.orange() )
		return await ctx.send( embed = emb )

	mute_role = discord.utils.get( ctx.message.guild.roles, name = 'MutE' )
	if mute_role in member.roles:
		await ctx.send(embed = discord.Embed(description = f"_**:warning: Данный пользователь {member.mention} уже замьючен!**_", colour = discord.Color.orange() ))
		return await ctx.send( embed = emb )

	channel = client.get_channel(732639862947053588)
	guild = ctx.guild
	perms = discord.Permissions(send_messages=False)
	emb = discord.Embed( title = "Mute :no_entry_sign:", colour = discord.Color.blue(), timestamp=ctx.message.created_at )
	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Модератор:', value = ctx.message.author.mention )
	emb.add_field( name = 'Нарушитель:', value = member.mention )
	emb.add_field( name = 'Время(сек):', value = time )
	emb.add_field( name = 'Причина:', value = reason )
	emb.set_footer( text = 'Спасибо за использование нашего бота{} '.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
	await member.add_roles( mute_role )
	await channel.send( embed = emb )
	await asyncio.sleep( time )
	await member.remove_roles( mute_role )

# JB-mute
@client.command( pass_context = True )
@commands.has_any_role('Library Devs', 'Moderators',725345713327964190)
async def jbmute( ctx, member: discord.Member, time: int,reason ):

	if member == ctx.message.author:
		emb = discord.Embed( title = '_**Ты не можешь замьютить `сам себя`!**_', color = discord.Color.orange() )
		return await ctx.send( embed = emb )

	jbmute_role = discord.utils.get( ctx.message.guild.roles, name = 'JB-MutE' )
	if mute_role in member.roles:
		await ctx.send(embed = discord.Embed(description = f"_**:warning: Данный пользователь {member.mention} уже замьючен!**_", colour = discord.Color.orange() ))
		return await ctx.send( embed = emb )
	channel = client.get_channel(732639862947053588)
	guild = ctx.guild
	perms = discord.Permissions(send_messages=False)
	emb = discord.Embed( title = "JB-Mute", colour = discord.Color.blue(), timestamp=ctx.message.created_at)
	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Модератор:', value = ctx.message.author.mention )
	emb.add_field( name = 'Нарушитель:', value = member.mention )
	emb.add_field( name = 'Время(сек):', value = time )
	emb.add_field( name = 'Причина:', value = reason )
	emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
	await member.add_roles( jbmute_role )
	await channel.send( embed = emb )
	await asyncio.sleep( time )
	await member.remove_roles( jbmute_role )

# Unmute
@client.command( pass_context = True )
@commands.has_any_role('Library Devs', 'Moderators',725345713327964190)

async def unmute( ctx, member: discord.Member ):
	channel = client.get_channel(732639862947053588)
	mute_role = discord.utils.get( ctx.guild.roles, name = 'MutE' )
	jbmute_role = discord.utils.get( ctx.guild.roles, name = 'JB-MutE' )
	emb = discord.Embed( title = "Unmute:white_check_mark:", colour = discord.Color.blue(), timestamp = ctx.message.created_at )
	emb.set_author( name = member.name, icon_url = member.avatar_url )
	emb.add_field( name = 'Модератор:', value = ctx.message.author.mention )
	emb.add_field( name = 'Нарушитель:', value = member.mention )
	emb.set_footer( text = 'Спасибо за использование нашего бота{}'.format( ctx.author.name ), icon_url = ctx.author.avatar_url )
	await channel.send( embed = emb )
	await member.remove_roles( mute_role)
	await member.remove_roles( jbmute_role)

# Help
@client.command( pass_context = True )


async def help ( ctx ): 
	emb = discord.Embed( title = '_Навигация по командам_',value = None, colour = discord.Color.red(), timestamp= ctx.message.created_at )

	emb.set_thumbnail( url = 'https://pngicon.ru/file/uploads/cocacola.png' )
	emb.add_field( name = 'Информация:', value = '``.help`` ``.info`` ``.time`` ``.server`` ``.user``' )
	emb.add_field( name = 'Модерация:', value = '``.mute`` ``.jbmute`` ``.ban`` ``.kick`` ``.clear``', inline = False )
	emb.add_field( name = 'Весёлое:', value = '``.ball`` ``.battle`` ``.love``', inline = False)
	emb.add_field( name = 'Утилиты:', value = '``.google``', inline = False)
	emb.set_footer( text = f"Спасибо за использование нашего бота: {ctx.author.name}", icon_url = ctx.author.avatar_url )
	
	await ctx.channel.purge( limit = 1 )

	await ctx.send( embed = emb )

# Get token
token = os.environ.get('BOT_TOKEN')