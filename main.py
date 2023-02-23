# -*- coding: utf-8 -*-
# bot by w1cee

import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

TOKEN = 'TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Just send the name of the city, and get current weather! ')


@bot.message_handler(content_types=['text'])
def text(message):
    config_dict = get_default_config()
    config_dict['language'] = 'eng'  # Language setting
    place = message.text  # Variable to record the city
    owm = OWM('1374cdbe6ac74415b62253caf8b3c67b')  # Your key from the open weather map site
    mgr = owm.weather_manager()  # Initializing owm.weather_manager()
    observation = mgr.weather_at_place(place)
    # Initializing mgr.weather_at_place() And passing the country and city as a parameter there
    w = observation.weather
    status = w.detailed_status  # Find out the weather status in the city and write it to the status variable
    humidity = w.humidity  # Find out the Humidity and write it to the humidity variable
    temperature = w.temperature('celsius')['temp']  # Find out the temperature and write it to the temperature variable

    bot.send_message(
        message.chat.id,
        (
            (
                (
                    (
                        (
                            (
                                f"In the city {str(place)} now {str(status)}"
                                + "\nTemperature is "
                            )
                            + str(round(temperature))
                            + " degrees Celsius"
                        )
                        + "\nHumidity is "
                    )
                    + str(humidity)
                    + "%"
                )
                + "\nWind speed is "
            )
            + str(w.wind()['speed'])
            + " meters per second"
        ),
    )


bot.infinity_polling()
