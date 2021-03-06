import os
from aiotg import Bot

bot = Bot(os.environ["API_TOKEN"])


@bot.command(r"/echo (.+)")
def echo(chat, match):
    return chat.reply(match.group(1))


if __name__ == '__main__':
    bot.run()
