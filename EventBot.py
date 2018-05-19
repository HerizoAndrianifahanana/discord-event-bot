#!/cygdrive/c/ProgramData/Miniconda3/python
import discord
import sqlite3
import DB

print("LAUNCHING BOT")

TOKEN = 'changeme'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!event new'):
		print(type(message.channel))
	#	server = client.get_server(message.server.id)
	#	chan = server.get_channel(message.channel.id)
		title = message.content[len('!event new'):]
		DB.newActivity(title)
		await client.send_message(chan, 'New activity set')
		
	elif message.content == '!event all':
		send = '\n'.join([x[0] for x in DB.getAllActivities()])
		print(send)
		await client.send_message(message.channel, send)
		

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
