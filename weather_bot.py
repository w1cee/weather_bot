# -*- coding: utf-8 -*-
# bot by w1cee

import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Напишите название города')


@bot.message_handler(content_types=['text'])
def text(message):
    place = message.text
    config_dict = get_default_config()  # Инициализация get_default_config()
    config_dict['language'] = 'ru'  # Установка языка
    place = message.text  # Переменная для записи города
    country = message.text  # Переменная для записи страны/кода страны
    country_and_place = place + ", " + country  # Запись города и страны в одну переменную через запятую

    owm = OWM('API TOKEN')  # Ваш ключ с сайта open weather map
    mgr = owm.weather_manager()  # Инициализация owm.weather_manager()
    observation = mgr.weather_at_place(country_and_place)
    # Инициализация mgr.weather_at_place() И передача в качестве параметра туда страну и город

    w = observation.weather

    status = w.detailed_status  # Узнаём статус погоды в городе и записываем в переменную status
    w.wind()  # Узнаем скорость ветра
    humidity = w.humidity  # Узнаём Влажность и записываем её в переменную humidity
    temp = w.temperature('celsius')['temp']  # Узнаём температуру в градусах по цельсию и записываем в переменную temp

    bot.send_message(message.chat.id,
                     "В городе " + str(place) + " сейчас " + str(status) +  # Выводим город и статус погоды в нём
                     "\nТемпература " + str(
                         round(
                             temp)) + " градусов по цельсию" +  # Выводим температуру с округлением в ближайшую сторону
                     "\nВлажность составляет " + str(humidity) + "%" +  # Выводим влажность в виде строки
                     "\nСкорость ветра " + str(
                         w.wind()['speed']) + " метров в секунду"  # Узнаём и выводим скорость ветра
                     )


bot.infinity_polling()
