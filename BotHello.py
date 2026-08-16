import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram.utils.markdown import hlink

API_TOKEN = "7093363299:AAGmVuo8xb2SB6_3I71E--vPxHQKZaFE5nc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.chat_member(ChatMemberUpdatedFilter(member_status_changed=IS_NOT_MEMBER >> IS_MEMBER))
async def on_user_join(event: ChatMemberUpdated):
    user = event.new_chat_member.user
    chat_id = event.chat.id
  
  # Настоящее упоминание с уведомлением: работает даже если у пользователя нет username
    mention = hlink(user.full_name, f"tg://user?id={user.id}")
 
    await bot.send_message(
        chat_id,
        f"""Привет, {mention}! Рада тебе 😍
Вся основная информация и материалы в этом сообщении >>>>> https://t.me/c/4493210142/4/29 ❤️‍🔥
Если у тебя есть какие-то вопросы, пиши сюда>>>> https://t.me/c/4493210142/4 , подскажу!)🎉""",
        parse_mode=ParseMode.HTML,
    )
    
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
