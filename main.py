import telebot
from telebot import types
keyboard1 = telebot.types.ReplyKeyboardMarkup()
bot = telebot.TeleBot("5361499356:AAHRjzxLJlf3FE0ma6tild9F-pDYH7p4_ZI")

@bot.message_handler(commands=['start'])
def start_message(message):
    mess = f'Вітаємо вас {message.from_user.first_name}! Зараз ви розміщуєте заявку на подачу реклами на нашому радіо.'
    bot.send_message(message.chat.id, mess, reply_markup=keyboard1)
    bot.send_message(message.chat.id, 'Вкажіть свій ПІБ', reply_markup=keyboard1)
    bot.register_next_step_handler(message, get_phone)

@bot.message_handler(commands=['phone'])
def get_phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Надіслати номер телефону", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Залиште свій номер телефону, щоб наш менеджер зміг вам зетелефонувати", reply_markup=keyboard)
    bot.register_next_step_handler(message, get_answer)

@bot.message_handler(commands=['answer'])
def get_answer(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Декілька Місяців")
    item2 = types.KeyboardButton("Від року та більше")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 'Вибір тривалості розміщення реклами: \n', reply_markup=markup)
    bot.register_next_step_handler(message, get_radio)

@bot.message_handler(commands=['radio'])
def get_radio(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Radio ROKS — слухати онлайн", url='https://play.tavr.media/radioroks/')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Ваша заявка прийнята!', reply_markup=keyboard1)
    bot.send_message(message.chat.id, "Натискайте на кнопку та слухайте радіо онлайн", reply_markup=markup)


bot.polling(none_stop=True)
