import discord
from discord.ext import commands
import time

api_key = '[TOKENHERE]'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def purge(ctx):
    message_limit = int(100)

    message_list = []
    async for x in bot.logs_from(ctx.message.channel, limit=message_limit):
        message_list.append(x)

    message_count = len(message_list)

    if message_count < 2:
        await bot.delete_message(x)
        print("Deleted ", message_count, " Message")
    elif message_count > 2:
        await bot.delete_messages(message_list)
        print("Deleted ", message_count, " Messages")

    message = "Cleared " + str(message_count) + " message(s) at " + time.strftime("%d/%m/%Y") + " " + \
              time.strftime("%H:%M:%S")
    bot.send_message(ctx.message.channel, message)

bot.run(api_key)
