from loader import dp
from aiogram.types import ContentTypes, Message
from pathlib import Path
manzil = Path().joinpath('Mediafiles')
manzil.mkdir(parents=True,exist_ok=True)

@dp.message_handler(content_types=ContentTypes.VIDEO)
#@dp.message_handler(content_types='video')
async def send_video(v:Message):
    await v.video.download( destination=manzil)
    await v.reply("Vidoe yuklab olindi ")
@dp.message_handler(content_types=ContentTypes.DOCUMENT)
#@dp.message_handler(content_types='document')
async def send_video(v:Message):
    await v.document.download(destination=manzil)
    file_idd = v.document.file_id
    await v.answer(file_idd)
@dp.message_handler(commands='document')
async def send_file(m:Message):
    id  = 'BQACAgIAAxkBAAILZWFb69-4EPRrDYaa2Ka3L7GdiQxWAALlEAACHH_hSp-nVh4Ndjj-IQQ'
    await m.reply_document(id, caption='bu dacument id orqali jonatildi')

@dp.message_handler(content_types=ContentTypes.STICKER)
#@dp.message_handler(content_types='video')
async def send_video(v:Message):
    await v.sticker.download( destination=manzil)
    await v.reply("Vidoe yuklab olindi ")