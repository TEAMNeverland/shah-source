import os
from pyrogram import Client, filters

# فحص إذا ملف الإعداد موجود، وإذا لا يتم إنشاؤه
if not os.path.exists("config.py"):
    print("🔧 إعداد أولي لسورس الشاه")
    bot_token = input("أرسل توكن البوت: ")
    dev_id = input("أرسل آيدي المطور الأساسي: ")

    with open("config.py", "w") as f:
        f.write(f'TOKEN = "{bot_token}"\nDEV_ID = {dev_id}\n')

from config import TOKEN, DEV_ID

# تشغيل البوت
app = Client("shah_bot", api_id=12345, api_hash="your_api_hash", bot_token=TOKEN)

# استيراد الأوامر
import plugins.start
import plugins.ranks

if __name__ == "__main__":
    print("💠 Bot is running...")
    app.run()
