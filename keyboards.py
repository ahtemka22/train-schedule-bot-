from telebot import types


def get_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton("Отправить GPS"),
        types.KeyboardButton("3 ближайших поезда"),
        types.KeyboardButton("Расчет")
    )
    return markup


def get_location_request():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("Отправить геопозицию", request_location=True))
    return markup


def get_direction_menu(resize_keyboard=True, row_width=2):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        types.KeyboardButton("Минск -> Дзержинск"),
        types.KeyboardButton("Дзержинск -> Минск"),
        types.KeyboardButton("Назад")
    )
    return markup


def get_tree_nearest_trains():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(types.KeyboardButton("Расписание: Минск -> Дзержинск"),
               types.KeyboardButton("Расписание: Дзержинск -> Минск"),
               types.KeyboardButton("Назад")
               )
    return markup

