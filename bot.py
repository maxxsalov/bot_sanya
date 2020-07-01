import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, """Хэлоу, {0.first_name}!\nМеня зовут <b>{1.first_name}</b>, 
    бот созданный для шуток над Санями. Напиши мне \"Саня\" и я скину мемасик""".format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == 'Саня' or 'саня':
        number = random.randint(1, 12)
        mem = open('mem/' + str(number) + '.jpg', 'rb')
        bot.send_photo(message.chat.id, mem)
    else:
        bot.send_message(message.chat.id, 'Сорян, моя твоя не понял :(')


# Run
bot.polling(none_stop=True)
