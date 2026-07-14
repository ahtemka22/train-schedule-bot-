from utils import get_next_trains, get_travel_time, when_to_go_out
from telebot import types
import keyboards as kb
from config import STATION_K_IN_DZR, STATION_K_IN_MINSK, SCHEDULE_DZR_TO_MINSK, SCHEDULE_MINSK_TO_DZR, API
from storage import user_location


def calculate_and_send(message, station_lat, station_lon, schedule, bot):
    user_lat, user_lon = user_location[message.chat.id]

    travel_time = get_travel_time(API, user_lat, user_lon, station_lat, station_lon)

    if travel_time is None:
        bot.send_message(message.chat.id, "Ошибка расчета")
        return

    exit_time, train_time = when_to_go_out(schedule, travel_time)

    if exit_time is None:
        bot.send_message(
            message.chat.id,
            f"До станции {travel_time} минут\nСегодня не успеваете"
        )
    else:
        bot.send_message(
            message.chat.id,
            f"Поезд в {train_time}\nИдти {travel_time} минут\nВыйти в {exit_time}"
        )

    bot.send_message(
        message.chat.id,
        "Вернулись в меню",
        reply_markup=kb.get_main_menu()
    )


def register_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == "3 ближайших поезда")
    def handler_trains(message):
        bot.send_message(
            message.chat.id,
            "Выберите направление",
            reply_markup = kb.get_tree_nearest_trains()
        )

    @bot.message_handler(func=lambda message: message.text == "Расписание: Дзержинск -> Минск")
    def handler_f_dz(message):
        trains = get_next_trains(SCHEDULE_DZR_TO_MINSK, 3)

        if not trains:
            bot.send_message(message.chat.id, "Сегодня больше нет поездов")

        else:
            response = ""
            for i, t in enumerate(trains, 1):
                response += f"{i}. Время отправления -- {t}\n"

            bot.send_message(message.chat.id, response)

        bot.send_message(
            message.chat.id,
            "Вернулись в главное меню",
            reply_markup=kb.get_main_menu()
        )

    @bot.message_handler(func=lambda message: message.text == "Расписание: Минск -> Дзержинск")
    def handler_f_m(message):
        trains = get_next_trains(SCHEDULE_MINSK_TO_DZR, 3)

        if not trains:
            bot.send_message(message.chat.id, "Сегодня больше нет поездов")

        else:
            response = ""
            for i, t in enumerate(trains, 1):
                response += f"{i}. Время отправления -- {t}\n"

            bot.send_message(message.chat.id, response)

        bot.send_message(
            message.chat.id,
            "Вернулись в главное меню",
            reply_markup=kb.get_main_menu()
        )

    @bot.message_handler(func=lambda message: message.text == "Отправить GPS")
    def handler_gps(message):
        bot.send_message(
            message.chat.id,
            "Нажмите кнопку ниже, что бы отправить геопозицию:",
            reply_markup=kb.get_location_request()
        )

    @bot.message_handler(content_types=["location"])
    def handle_location(message):
        lat = message.location.latitude
        lon = message.location.longitude

        user_location[message.chat.id] = (lat, lon)

        remove_markup = types.ReplyKeyboardRemove()

        bot.send_message(
            message.chat.id,
            f"GPS получен! \n Широта: {lat:.6f}\n Долгота: {lon:.6g}",
            reply_markup=remove_markup
        )

        bot.send_message(
            message.chat.id,
            "Вернулись в главное меню",
            reply_markup=kb.get_main_menu()
        )

    @bot.message_handler(func=lambda message: message.text == "Расчет")
    def handler_direction(message):
        if message.chat.id not in user_location:
            bot.send_message(
                message.chat.id,
                "Сначала отправьте GPS"
            )
            return

        bot.send_message(
            message.chat.id,
            "Выберите направление",
            reply_markup=kb.get_direction_menu()
        )

    @bot.message_handler(func=lambda message: message.text == "Минск -> Дзержинск")
    def handler_minsk_to_dzr(message):
        calculate_and_send(message,
                           STATION_K_IN_MINSK[0],
                           STATION_K_IN_MINSK[1],
                           SCHEDULE_MINSK_TO_DZR,
                           bot
        )

    @bot.message_handler(func=lambda message: message.text == "Дзержинск -> Минск")
    def handler_dzr_to_minsk(message):
        calculate_and_send(message,
                           STATION_K_IN_DZR[0],
                           STATION_K_IN_DZR[1],
                           SCHEDULE_DZR_TO_MINSK,
                           bot
        )

    @bot.message_handler(func=lambda message: message.text == "Назад")
    def handler(message):
        bot.send_message(
            message.chat.id,
            "Вернулись в главное меню",
            reply_markup=kb.get_main_menu()
        )











