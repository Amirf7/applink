# import requests


from rubika import Socket, Bot
from rubika.filters import filters
import requests
import os

bot = Socket("")
sender = Bot("app", "")


@bot.handler(filters.PV, filters.text)
def handler(message):
    # message.show()
    p_des = open("caption.txt", "r").read()
    C_id = open("guid.txt", "r").read()
    subs = open("subscription.txt", "r").read()
    user_id = message.data.object_guid
    msg_text = message.data.message.text
    if user_id in subs:
        if "http://" in msg_text or "https://" in msg_text:
            message.reply("💯 در حال پردازش...")
            url = message.data.message.text

            # start Downloading File

            message.reply("🔸 دانلود شروع شد...")
            r = requests.get(url, allow_redirects=True)
            file_name = url.split("/")
            file_name = file_name[len(file_name) - 1]

            # Saving File

            open(file_name, 'wb').write(r.content)
            message.reply("✅ فایل مورد نظر با موفقیت دانلود و ذخیره شد!")

            # start Uploading File

            message.reply("🔸 آپلود شروع شد...")

            sender.sendDocument(C_id,
                                f"./{ file_name }", caption=f"{p_des}")

            message.reply("✅ فایل مورد نظر با موفقیت آپلود شد!")
            os.remove(file_name)
        if "!des" in msg_text:
            des = msg_text.replace("!des ", "")
            des_file = open("caption.txt", "w")
            des_file.write(des, chr="")
            message.reply("✅ کپشن مورد نظر در حافظه ربات ثبت شد!")

        if "!id" in msg_text:
            id = msg_text.replace("!id ", "")
            guid = sender.getInfoByUsername(
                f"{id}")["data"]["channel"]["channel_guid"]
            id_file = open("guid.txt", "w")
            id_file.write(guid)
            sender.join(guid)
            message.reply("✅ ربات در کانال عضو شد، لطفا ادمینش کنید و بعد لینکتون رو بفرستید")

        if "!id @" in msg_text:
            id = msg_text.replace("!id @", "")
            guid = sender.getInfoByUsername(
                f"{id}")["data"]["channel"]["channel_guid"]
            id_file = open("guid.txt", "w")
            id_file.write(guid)
            sender.join(guid)
            message.reply("✅ ربات در کانال عضو شد، لطفا ادمینش کنید و بعد لینکتون رو بفرستید")

        if msg_text == "!help":
            message.reply(
                "⁉️ ربات چجوری کار میکنه؟\n\n🌀 !id [ Channel GUID ]\n🌀 !des [ Post Caption ]\n\n⭕️ توجه داشته باشید ربات حتما توی چنل ادمین باشه ( برای عضویت ربات توی چنل به ادمین آیدی چنلو بدید )\n\n⭕️ آپلود دستور خاصی نداره، فقط باید لینک فایلو به بات بدید.\n\n💯 پشتیبانی و خرید اشتراک => @Karbala713")

        if user_id == "u0BqaGn0618f94c9434646d5195f1ae1":
            if "!add @" in msg_text:
                id = msg_text.replace("!add @", "")
                guid = sender.getInfoByUsername(
                    f"{id}")["data"]["user"]["user_guid"]
                sub_file = open("subscription.txt", "a")
                sub_file.write(f"\n{guid}")
                message.reply("✅ آیدی مورد نظر در حافظه ربات ثبت شد!")
                sender.sendMessage(
                    guid, "✅ شما در ربات ادمین شدید، برای دریافت دستورات !help رو ارسال کنید!")
    else:
        message.reply("""
        🔖 ╍ آپلودر فایل از طریق لینک ! 
 
 🔹 | برای استفاده از ربات لطفا 
 اشتراک خود را تهیه کنید . 
 
 • خرید اشتراک یک ماهه :
 | P'v : @Karbala713 """)
            