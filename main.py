import telebot
from telebot import types
import botGames
import menuBot
from menuBot import Menu
import DZ
import fun
import db

bot = telebot.TeleBot('5554645849:AAFhX5DgFmIO0-cJEH6jl9F_wr5GVDuF_g4')

@bot.message_handler(commands="start")
def command(message):
    chat_id = message.chat.id
    txt_message = f"Привет, {message.from_user.first_name}! Что делаем?"
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    cur_user = menuBot.Users.getUser(chat_id)
    if cur_user is None:
        cur_user = menuBot.Users(chat_id, message.json["from"])



    subMenu = menuBot.goto_menu(bot, chat_id, ms_text)
    if subMenu is not None:

        if subMenu.name == "Игра в 21":
            game21 = botGames.newGame(chat_id, botGames.Game21(jokers_enabled=True))
            text_game = game21.get_cards(2)
            bot.send_media_group(chat_id, media=game21.mediaCards)
            bot.send_message(chat_id, text=text_game)

        elif subMenu.name == "Игра КНБ":
            gameRPS = botGames.newGame(chat_id, botGames.GameRPS())
            bot.send_photo(chat_id, photo=gameRPS.url_picRules, caption=gameRPS.text_rules, parse_mode='HTML')

        return

    cur_menu = Menu.getCurMenu(chat_id)
    if cur_menu is not None and ms_text in cur_menu.buttons:
        module = cur_menu.module

        if module != "":
            exec(module + ".get_text_messages(bot, cur_user, message)")

        if ms_text == "Помощь":
            send_help(bot, chat_id)



    else:
        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду: " + ms_text)
        menuBot.goto_menu(bot, chat_id, "Главное меню")



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    chat_id = call.message.chat.id
    message_id = call.message.id
    cur_user = menuBot.Users.getUser(chat_id)
    if cur_user is None:
        cur_user = menuBot.Users(chat_id, call.message.json["from"])

    tmp = call.data.split("|")
    menu = tmp[0] if len(tmp) > 0 else ""
    cmd = tmp[1] if len(tmp) > 1 else ""
    par = tmp[2] if len(tmp) > 2 else ""

    if menu == "GameRPSm":
        botGames.callback_worker(bot, cur_user, cmd, par, call)



def send_help(bot, chat_id):
    bot.send_message(chat_id, "Автор: Чайкина Елизавета")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Можете со мной связаться:", url="https://vk.com/chaikis")
    markup.add(btn1)
    img = open('resources/me.jpg', "r+b")
    bot.send_photo(chat_id, img, reply_markup=markup)

    bot.send_message(chat_id, "Активные пользователи :")
    for el in menuBot.Users.activeUsers:
        bot.send_message(chat_id, menuBot.Users.activeUsers[el].getUserHTML(), parse_mode='HTML')




bot.polling(none_stop=True, interval=0)
