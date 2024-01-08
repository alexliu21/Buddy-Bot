import tweepy as tw
import discord as ds
from discord.ext import commands
import time
import datetime
import random
import csv
from dotenv import load_dotenv

load_dotenv()

# discord API client
bot = commands.Bot(command_prefix='%',description="This bot is used to append more values to the lists of first/last "
												  "names and quotes that @Hacogdoches will randomly draw from and tweet.")

#twitter API client
#tclient = tw.Client(bearer_token="",
#                   consumer_key="",
#                   consumer_secret="",
#                   access_token="",
#                   access_token_secret=""
#)

firstNames = []
lastNames = []
quotes = []

# commands
@bot.command()
async def last(ctx,name):
	print(name)
	await ctx.channel.send("Last name added to list.")
	with open('lastNames.csv', 'a', newline='') as l:
		writer = csv.writer(l, quoting=csv.QUOTE_MINIMAL)
		writer.writerow([name])
@bot.command()
async def first(ctx,name):
	await ctx.channel.send("First name added to list.")
	with open('`firstNames.csv', 'a', newline='') as f:
		writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
		writer.writerow([name])
@bot.command()
async def quote(ctx,qt):
	await ctx.channel.send("Quote added to list.")
	with open('quotes.csv', 'a', newline='') as g:
		writer = csv.writer(g, quoting=csv.QUOTE_MINIMAL)
		writer.writerow([qt])
@bot.command()
async def blackjack(ctx):
	await ctx.channel.send("Gambling is illegal.")
@bot.command()
async def tw(ctx):
	with open('firstNames.csv') as r:
		firstNames = list(csv.reader(r))
	#print(firstNames)
	with open('lastNames.csv') as t:
		lastNames = list(csv.reader(t))
	#print(lastNames)
	with open('quotes.csv') as q:
		quotes = list(csv.reader(q))
	randName = random.choice(firstNames)[0] + ' ' + random.choice(lastNames)[0] + ', ' + random.choice(quotes)[0]
	await ctx.channel.send(randName)
	print(randName)
	#tclient.create_tweet(text=randName)
@bot.command()
async def send(ctx,arg):
	tclient.create_tweet(text=arg)
bot.run("") # insert discord access token here
