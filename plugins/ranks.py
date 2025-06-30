from pyrogram import Client, filters

@Client.on_message(filters.command("رفع") & filters.group)
def promote(client, message):
    message.reply_text("تم رفع العضو بالرتبة المطلوبة.")
