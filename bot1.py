from pyrogram import Client, filters 

bot = Client(
    "BOT1",
    api_id = 27597038,
    api_hash = "993bc08139eeab5e80addfa3546db8c0",
    bot_token = "7403510787:AAE3YjUfuWN79PufOzbUoJpBd4ydpKtvB7o"
)

@bot.on_message(filters.command('start') & filters.private)
def command1(bot, message):
    bot.send_message(message.chat.id, "Vanakaam, samse samse naalu pathruba.")
@bot.on_message(filters.command('help'))
def command1(bot, message):
    message.reply_text("Achacho!, Enachu Yaam iruka Bayamen")
@bot.on_message(filters.text)
def echobot(client, message):
    message.reply_text(message.text)
print("I AM ALIVE")

bot.run()
