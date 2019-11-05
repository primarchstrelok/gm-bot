# Work with Python 3.6
import discord
import sys
import urllib.request
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext import commands

#discord app token
TOKEN = ''

client = commands.Bot(command_prefix = "!")

#status declaration
STATUS = dict(
player1={'head': 'healthy', 'torso': 'healthy', 'neck': 'healthy', 'larm': 'healthy', 'rarm': 'healthy', 'lleg': 'healthy', 'rleg': 'healthy'},
player2={'head': 'healthy', 'torso': 'healthy', 'neck': 'healthy', 'larm': 'healthy', 'rarm': 'healthy', 'lleg': 'healthy', 'rleg': 'healthy'},
)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print('---------------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')

#@client.command(pass_context=True)
#async def help(ctx):
#    helpinfo = open(r"help.txt","r")
#    await client.say(helpinfo)

@client.command(pass_context=True)
async def hello(ctx):
    await client.say("Hello {}".format(ctx.message.author.mention))

@client.command(pass_context=True)
async def nani(ctx):
    await client.say("The Fuck? {}".format(ctx.message.author.mention))

@client.command(pass_context=True)
async def gold(ctx):
    target = ctx.message.content[len('!gold '):]
    if target == '':
        gold = 1337
    elif target == '':
        gold = 9001
    goldoutput = target + ' has ' + str(gold) + ' Gold'
    await client.send_message(ctx.message.channel, goldoutput)

#Mutiple bodypart injury tracking
#Set Status
@client.command(pass_context=True)
async def setstatus(ctx):
    statusargs = ctx.message.content[len('!setstatus '):]
    #character determination 
    #if name in request set character target to name
    if '' in statusargs:
        character = ''
    elif '' in statusargs:
        character = ''
    #body parts
    if 'head' in statusargs:
        part = 'head'
    elif 'neck' in statusargs:
        part = 'neck'
    elif 'torso' in statusargs:
        part = 'torso'
    elif 'larm' in statusargs:
        part = 'larm'
    elif 'rarm' in statusargs:
        part = 'rarm'
    elif 'lleg' in statusargs:
        part = 'lleg'
    elif 'rleg' in statusargs:
        part = 'rleg'
    #damage levels
    if 'healthy' in statusargs:
        health = 'healthy'
    elif 'moderate' in statusargs:
        health = 'moderate'
    elif 'serious' in statusargs:
        health = 'serious'
    STATUS[character]={part:health}
    output = 'Set ' + character + ' ' + part + ' ' + health
    await client.send_message(ctx.message.channel, output)
    print(STATUS[character][part])

@client.command(pass_context=True)
async def status(ctx):
    statusargs = ctx.message.content[len('!status '):]
    #character determination
    #if name in request set character target to name
    if '' in statusargs:
        character = ''
    elif '' in statusargs:
        character = ''
    #body parts
    if 'head' in statusargs:
        part = 'head'
    elif 'neck' in statusargs:
        part = 'neck'
    elif 'torso' in statusargs:
        part = 'torso'
    elif 'larm' in statusargs:
        part = 'larm'
    elif 'rarm' in statusargs:
        part = 'rarm'
    elif 'lleg' in statusargs:
        part = 'lleg'
    elif 'rleg' in statusargs:
        part = 'rleg'
    output = STATUS[character][part]
    await client.send_message(ctx.message.channel, output)

#pulls top posts from subreddit
@client.command(pass_context=True)
async def top(ctx):
    if ctx.message.content.startswith("!top"):
        subred = ctx.message.content[len('!top '):]
        url = sys.argv[1] if len(sys.argv) > 1 else ("https://www.reddit.com/r/" + subred + "/")
        conn = urllib.request.urlopen(url + ".json")
        data = conn.read()
        conn.close()
        data = json.loads(data)
        loop = 0
        preface = "These are the hottest posts from r/" + subred
        await client.send_message(ctx.message.channel, "**" + preface + "**")
        for sub in (tsub["data"] for tsub in data["data"]["children"]):
            output =  ("{0}\n - {1} ({2}|{3})".format(sub["title"], sub["score"], sub["ups"], sub["downs"]))
            await client.send_message(ctx.message.channel, output)
            loop += 1
            if loop >= 5:
                return

#watching the game
@client.command()
async def wasup():
    await client.say("Wassssup")

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)