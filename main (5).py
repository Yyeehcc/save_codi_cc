import telebot
from telebot import types

BOT_TOKEN = "6528971358:AAEj9drgjeXTT0CFBmvwGBlyWyJWQOlikfM"
bot = telebot.TeleBot(BOT_TOKEN)

name = ""
age = ""
phone = ""

@bot.message_handler(commands=['start']) 


def start_message(message):
    bot.send_message(message.from_user.id, "Привет! я телебот который помогу тебе зарегистрироваться на курс! Оставь свои данные и мы с тобой свяжемя! :) ")
    bot.send_message(message.from_user.id, "Напиши свое ФИО:")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
  global name
  name = message.text
  print(name)
  bot.send_message(message.from_user.id, "Напиши свой возраст")
  bot.register_next_step_handler(message, get_phone)
  
  
def get_phone(message): 
  global age
  age = message.text
  print(age)
  bot.send_message(message.from_user.id, "Напиши свой номер   телефона:")
  bot.register_next_step_handler(message, confirm)
  
def confirm(message):
  phone = message.text
  print(phone)

  keyboard = types.InlineKeyboardMarkup()
  key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
  keyboard.add(key_yes)
  key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
  keyboard.add(key_no)
  bot.send_message(message.from_user.id, "Имя: " + name + "\nвозраст: "+ age +"\nНомер телефона: "+phone, reply_markup= keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
  if call.data == "yes":
    bot.send_message(call.message.chat.id, "Отлично! Теперь мы свяжемся с вами")
    a=call.message.text


    with open("data.txt", "a") as file:
      file.write(f"{a} \n \n")
  
  
bot.polling()



#bot.polling()