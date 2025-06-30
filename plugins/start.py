from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
def start_command(client, message):
    message.reply_text("أهلًا بك في سورس الشاه 👑")
