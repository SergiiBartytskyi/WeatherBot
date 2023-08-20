import telebot
import requests
import json
import time

bot = telebot.TeleBot('6305804643:AAHz0ZQgngP26nZEXHmgYQdUNwzh0tI2qtY')
API = 'bd8b5fc6631b6c3fe812d61481cde799'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = round(data['main']['temp'])
        temp = int(temp)
        bot.reply_to(message, f'Зараз погода: {temp}℃')
    else:
        bot.reply_to(message, 'Невірна назва міста')

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(15)


