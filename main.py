import dns, pymongo, asyncio, discord, requests, json, os, time, threading, csv, subprocess
the_old_message = "There is no message, the bot must have just started up!"
from db import *
from discord.ext import commands
from PyDictionary import PyDictionary

dictionary = PyDictionary() 
from random_word import RandomWords

r = RandomWords()
from random import randint, sample

print(dictionary.meaning('word'))
print("\x1B[H\x1B[J")
global text
text = "PawskSmujwNjsohsrbhbad"
the_time = time.time()
print(the_time)
stop = False
reader = csv.reader(open('output.csv', 'r'))
users = {}
for row in reader:
	k, v = row
	users[k] = v
print(users)
bot = commands.Bot(command_prefix='$')
bot.remove_command("help")
print("e")
from discord.ext.commands import CommandNotFound


def f(f_stop):
	w = csv.writer(open("output.csv", "w"))
	for key, val in users.items():
		w.writerow([key, val])
	if not f_stop.is_set():
		threading.Timer(60, f, [f_stop]).start()


f_stop = threading.Event()
f(f_stop)


#------------LOGIN MESSAGE---------#
@bot.event
async def on_ready():
	activity = discord.Activity(name='The Bee Movie',
	                            type=discord.ActivityType.watching)
	await bot.change_presence(activity=activity)
	print(len(bot.guilds))
	for guild in bot.guilds:
		print(guild.name)
	print("now")
	text_channel_list = []
	for guild in bot.guilds:
		print(guild.name)

		channel_printed = False
		for channel in guild.channels:
			#print(await channel.create_invite(max_age=3000))
			if channel_printed == False:
				#print(await channel.create_invite(max_age=3000))
				channel_printed == True
			print(channel)
			print(channel.id)
			if channel.type == 'Text':
				print(channel.id)
				a = bot.get_channel(channel.id)
				print(await a.create_invite(max_age=300))
				print(channel)
				text_channel_list.append(channel)

	print(text_channel_list)
	des = 857108811483709456
	print(des)
	channel = bot.get_channel(des)
	#print(await channel.create_invite(max_age=300))

	print('We have logged in')


#---------exec------------#
@bot.command()
async def execute(ctx, *, command: str):
	if ctx.author.id == 433376107727683590:
		exec(command)
	else:
		await ctx.send("You do not have premision to use this.")


#----------REACTIONS------------#
@bot.event
async def on_message(message):
	try:
		if "egg" in message.content:
			await message.add_reaction("🧀")

		elif "GD" in message.content:
			await message.channel.send("My creator?")
	except Exception as E:
		await message.channel.send(E)
		raise
	await bot.process_commands(message)


#---------OS.RUN---------#
@bot.command(name="run")
async def run(ctx, command):
	if ctx.author.id == 433376107727683590:

		o = subprocess.run([command],
		                   stdout=subprocess.PIPE).stdout.decode('utf-8')
		if (len(o) > 2000):
			await ctx.send(o[0:1900])
		else:
			await ctx.send(o)

	else:
		await ctx.send("You do not have premision to use this.")


#----------RANDOM WORD-----------#
@bot.command()
async def word(ctx):
	d = r.get_random_word()
	x = "Your random word is: " + d
	await ctx.send(x)


#------PING PONG----------#
@bot.command()
async def ping(ctx):
	await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))


#---------SHUFFLE---------------#
@bot.command()
async def shuffle(ctx, param: str):
	await ctx.send(''.join(sample(param, len(param))))


@bot.command()
async def secret(ctx):
	await ctx.send(":eyes:")


@bot.command()
async def no(ctx):
	await ctx.send('yes')


#-----------UNDELETE---------#
@bot.event
async def on_message_delete(message):
	global the_old_message
	the_old_message = message.content


@bot.command()
async def UnDo(ctx):
	await ctx.send(the_old_message)


#------------IMAGES?-----------#
@bot.command()
async def height(ctx):
	await ctx.send("The height is {}".format(ctx.message.attachments))


@bot.command()
async def enlarge(ctx, user: discord.User):
	if not user:
		return  # Can't find the user, then quit
	pfp = user.avatar_url
	embed = discord.Embed(title="Enlarged Image",
	                      description='{}'.format(ctx.author.mention),
	                      color=0xecce8b)
	embed.set_image(url=(pfp))
	await ctx.send(embed=embed)


#-------------MONEY----------------#
#----------THEIVE--------------#
@bot.command()
async def steal(ctx, user: discord.User):
	if str(ctx.author.id) in users:
		if str(user.id) in users:
			if int(users[str(user.id)]) > 500 and int(users[str(
			    ctx.author.id)]) > 500:
				if randint(1, 4) == 4:
					amount_stolen = randint(1, int(users[str(user.id)]) - 250)
					await ctx.send(
					    "Steal success! You robbed {} money from them. ".
					    format(amount_stolen))
					users[str(user.id)] = str(
					    int(users[str(user.id)]) - amount_stolen)
					users[str(ctx.author.id)] = str(
					    int(users[str(ctx.author.id)]) + amount_stolen)
				else:
					amount_fined = randint(0, 500)
					await ctx.send(
					    "You failed, and you were fined {} bucks from the police. Better luck next time!"
					    .format(amount_fined))
					users[str(ctx.author.id)] = str(
					    int(users[str(ctx.author.id)]) - amount_fined)

			else:
				await ctx.send(
				    "Cmon, dont rob someone who doesnt have much money! Wait until they has over 500. Either this, or YOU dont have over 500 bucks. Maybe bet some more?"
				)
		else:
			await ctx.send(
			    "The user you are trying to steal from is not setup!")
	else:
		await ctx.send("You are not set up! Run $setup.")


#-------SETUP-------#
@bot.command()
async def setup(ctx):
	if str(ctx.author.id) in users:
		await ctx.send("You are already setup!")
	else:
		users[str(ctx.author.id)] = "0"
		await ctx.send("Success. Run $daily to get your daily!")


#------BAL-------#
@bot.command()
async def bal(ctx):
	if str(ctx.author.id) in users:
		await ctx.send("Your balance is {}".format(users[str(ctx.author.id)]))
	else:
		await ctx.send("Run $setup to use this command")


#----------BET----------#
@bot.command()
async def bet(ctx, amount: int):
	if str(ctx.author.id) in users:
		if (int(users[str(ctx.author.id)]) >= amount):
			chance = randint(1, 10)
			if (chance > 5):
				await ctx.send(
				    "You have won. You rolled {} which is greater than 5. You are now at {} money"
				    .format(chance,
				            int(users[str(ctx.author.id)]) + amount))
				users[str(
				    ctx.author.id)] = int(users[str(ctx.author.id)]) + amount
			else:
				await ctx.send(
				    "You lost, because you rolled a {} which is less than 5".
				    format(chance))
				users[str(
				    ctx.author.id)] = int(users[str(ctx.author.id)]) - amount
		else:
			await ctx.send("Not enough money")
	else:
		await ctx.send("You are not setup, run $setup")


#-------DAILY---------#
@bot.command()
async def daily(ctx):
	if str(ctx.author.id) in users:
		await ctx.send(
		    "Daily has been added. + 100. This puts you at {}".format(
		        int(users[str(ctx.author.id)]) + 100))
		w = int(users[str(ctx.author.id)]) + 100
		users[str(ctx.author.id)] = str(w)
	else:
		await ctx.send("Please set up your money with $setup")
		await ctx.send(ctx.author.id)


#-----------TEST-----------#
@bot.command()
async def test(ctx):
	f = open("test.txt", "r")
	e = f.read()
	f.seek(0)
	await ctx.send(f.read())
	f.close()
	n = int(e) + 1
	p = open("test.txt", "w")
	p.write(str(n))
	p.close()


#------------UPTIME-----------------#
@bot.command()
async def uptime(ctx):
	t = "The bot has been up for " + str(time.time() - the_time) + " seconds."
	await ctx.send(t)


#--------------COUNTER----------------#
@bot.command()
async def count(ctx):
	a = "The current count is: " + str(Check())
	Save()
	b = "After adding one, it is: " + str(Check())
	await ctx.send(a)
	await ctx.send(b)


#-------------8-BALL--------------#
@bot.command(name="8ball")
async def ball(ctx, arg):
	messages = [
	    "Buy your own 8-Ball!", "Yes", "Thats a yes", "Obviously", "Certanly",
	    "No, mate", "No", "Uhhhh no", "No Way", "Its possible", "maybe?",
	    "IDK", "Try again ~~later~~ never", "spooky",
	    "Why are you bothering me?", "TBH IDK", "I refuse to answer that"
	]
	x = "You asked: '" + arg + "'. My answer is: " + messages[randint(
	    0,
	    len(messages) - 1)]
	await ctx.send(x)


#---------------DEFINITION----------#
@bot.command()
async def definition(ctx, arg: str):
	try:
		await ctx.send(dictionary.meaning(arg))
	except:
		await ctx.send("Nothing matching the search!")


#-----------RANDOM-------------#
@bot.command()
async def random(ctx, arg1: int, arg2: int):
	try:
		import random
		await ctx.send(str(random.randint(arg1, arg2)))
	except:
		await ctx.send("Make sure you are using two ints!")


#------------RANDOMURL-------------#
@bot.command()
async def randomURL(ctx):
	await ctx.send("Fetching a random URL...")
	from googlesearch import search

	import string
	import random

	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))

	query = id_generator(4)

	for j in search(query, num=1, stop=1, pause=3):
		await ctx.send(j)


#---------STOP BEES---------#
@bot.command()
async def stop(ctx):
	global stop
	stop = True


#-----------FEEDBACK-----------#
@bot.command()
async def contact(ctx, param):
	word = text[0:2] + text[3] + text[5] + text[9] + text[13] + text[
	    16] + text[21]
	client = pymongo.MongoClient(
	    "mongodb+srv://Person:" + word +
	    "@cluster0-u4jiy.mongodb.net/test?retryWrites=true&w=majority")
	db = client.beeBot

	col = db.beeBotContact
	try:
		send = [{"message": param}]
		col.insert_many(send)
		await ctx.send("Succes!!")
	except:
		await ctx.send("Make sure you out the full message in quotes!")
	client.close()


#------------HELP-------------#
@bot.command(name="help")
async def message(ctx):
	await ctx.send("""
  Bee Movie Bot
  $bee - says the bee movie
  $stop - stops the bee move [BETA]
  $definition <word> - gets the definition of <word>
  $contact 'message' - make sure the message is in single quotes, and this sends a message to the creator of the bot!
  $8ball 'message' - make sure the message is in single quotes! This will give you an 8ball response based on your message
  $help - shows commands
  $randomURL - fetches a random url!
  $random <first num> <second num> - gets a random number between frist num and second num
  $count - a clicker that anybody can veiw the total number if counts on!
  $uptime - veiw the amount of uptime
  $word - Get a random word!
  -------MONEY-[ALPHA]----------
  $setup - sets up money commands
  $steal @"mention" - steals from whoever you mention
  $bet <amount> - bets the amount you put
  $daily - gets daily
  Expect More Soon! Have a 'bee' day!
  - GD;
  """)


#------------SHUTDOWN-------------#
@bot.command()
async def shutdown(ctx):
	if ctx.author.id == 433376107727683590:
		await ctx.send("okay")
		await bot.logout()
	else:
		await ctx.send("You do not have premision to use this.")


#----------BEE--------------#
@bot.command()
async def bee(ctx):
	await ctx.send('Uh oh! Bee move time...')
	with open('bee.txt') as fp:
		line = fp.readline()
		cnt = 1
		while line:
			if (line.strip() == ""):
				line = fp.readline()
				cnt += 1
			else:
				await asyncio.sleep(1)
				await ctx.send("{}".format(line.strip()))
				line = fp.readline()
				cnt += 1
				global stop
				if (stop == True):
					await ctx.send("Stopped")
					stop = False
					break


#----------END OF COMMANDS---------#
from keep_alive import keep_alive

keep_alive()
import os

bot.run(os.getenv("BOT_KEY"), bot=True)
