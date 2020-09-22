import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "`Cobalah bercermin, maka kamu akan tau arti segalanya bagiku.`",
    "`Jika mencintaimu adalah tindakan yang melanggar hukum, aku pasti telah menjadi terpidana dengan hukuman paling lama.`",
    "`IKAN HIU LAGI LAPER, I LOP YU POREPER`",
    "`Pada rekah senyummu, disitulah seluruhnya rinduku tertuju.`",
    "`Jika kamu ibarat bunga, aku akan menjadi pot sebagai tempatmu tumbuh menjadi indah.`",
    "`Memang benar rindu adalah candu. Sehari saja tak bersamamu rasanya seperti ingin mati karena overdosis rindu.`",
    "`Bolehkah aku memandangmu? Aku hanya ingin melihat masa depanku.`",
    "`Bahkan dalam gelap gulitanya malam, wajahmu tetaplah bersinar di anganku.`",
    "`Taukah kamu pelangi yang sering kupandangi ketika hujan reda? Ia malu menampakkan dirinya lagi setelah kuceritakan tentang keindahanmu.`",
  )

@run_async
def gombal(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /gombal
"""

__mod_name__ = "GOMBAL"

CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(CRNA_HANDLER)
