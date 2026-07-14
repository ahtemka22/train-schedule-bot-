import telebot
from config import TOKEN
import keyboards as kb
import handlers
import json
import os

bot = telebot.TeleBot(TOKEN)

USERS_FILE = "users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_user(user_id):
    users = load_users()
    users.add(user_id)
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(users), f, ensure_ascii=False, indent=2)


handlers.register_handlers(bot)


@bot.message_handler(commands=["start"])
def hi(message):
    user_id = message.from_user.id
    save_user(user_id)  # ← Добавляем сохранение

    bot.send_message(
        message.chat.id,
        "Привет! Выберите действие",
        reply_markup=kb.get_main_menu()
    )


@bot.message_handler(commands=["start"])
def hi(message):
    bot.send_message(
        message.chat.id,
        "Привет! Выберите действие",
        reply_markup=kb.get_main_menu()
    )


if __name__ == "__main__":
    print("Бот запущен!")
    bot.polling(none_stop=True)