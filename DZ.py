import telebot
from menuBot import Menu


def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "дз-1":
        dz1(bot, chat_id)

    elif ms_text == "дз-2":
        dz2(bot, chat_id)

    elif ms_text == "дз-3":
        dz3(bot, chat_id)

    elif ms_text == "дз-4":
        dz4(bot, chat_id)

    elif ms_text == "дз-5":
        dz5(bot, chat_id)

    elif ms_text == "дз-6":
        dz6(bot, chat_id)

    elif ms_text == "дз-7":
        dz7(bot, chat_id)

    elif ms_text == "дз-8":
        dz8(bot, chat_id)

    elif ms_text == "дз-9":
        dz9(bot, chat_id)




def Find_Response(bot, chat_id, responseID, name="", age="", message=""):
    if responseID == 4:
        bot.send_message(chat_id, text=f'Привет, {name}, тебе {age} лет')
    if responseID == 5:
        if age < 18:
            bot.send_message(chat_id, text=f'Маленький', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
        elif 18 < age <= 22:
            bot.send_message(chat_id, text=f'Молодой', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
        elif 22 < age <= 30:
            bot.send_message(chat_id, text=f'Взрослый', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
        elif 30 < age <= 65:
            bot.send_message(chat_id, text=f'Большой', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
        else:
            bot.send_message(chat_id, text=f'Старый', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
    if responseID == 6:
        if len(name) > 2:
            bot.send_message(chat_id, text=name[1:-1])
            bot.send_message(chat_id,text=name[::-1])
            bot.send_message(chat_id,text=name[-3:])
            bot.send_message(chat_id,text=name[:5], reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

        elif len(name) == 2:
            bot.send_message(chat_id,text=name[::-1])
            bot.send_message(chat_id,text=name[::-1])
            bot.send_message(chat_id,text=name[-3:])
            bot.send_message(chat_id,text=name[:5], reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

        else:
            bot.send_message(chat_id, text="Вводи корректно!", reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
    if responseID == 7:
        prz = 1
        sum = 0
        for i in range(1, age + 1):
            sum = sum + i
            prz = prz * i
        bot.send_message(chat_id, text=f'Длина твоего имени: {len(name)} \nСумма чисел твоего возраста: {sum} \nПроизведение чисел воз-а: {prz}', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)

    if responseID == 8:
        bot.send_message(chat_id, text=f'{str.upper(name)}, {str.lower(name)}, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup')
    if responseID == 9:
            space = " "
            dgts = '1234567890+-/.+'
            if space in name:
                bot.send_message(chat_id, text="Без пробелов")
                dz9(bot, chat_id)
            elif dgts in name:
                bot.send_message(chat_id, text="Без символов")
                dz9(bot, chat_id)
            else:
                if age <=0 or age>=150:
                    bot.send_message(chat_id, text="Нужен нормальный возраст", reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
                else:
                    bot.send_message(chat_id, text=f'Добро пожаловать, {name}! Я знаю, что тебе {age}', reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)




def dz1(bot, chat_id):
    n = "Елизавета"
    bot.send_message(chat_id, text=n)


def dz2(bot, chat_id):
    a = '18'
    n = f'Мне {a} лет'
    bot.send_message(chat_id, text=n)


def dz3(bot, chat_id):
    n = "Лиза " * 5
    bot.send_message(chat_id, text=n)


def dz4(bot, chat_id):
    msg = bot.send_message(chat_id, text="Как тебя зовут?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, dz4_1, chat_id, bot)


def dz4_1(message, chat_id, bot):
    name = message.text
    msg = bot.send_message(chat_id, text="Сколько тебе лет?")
    bot.register_next_step_handler(msg, inPut_int, bot, chat_id, responseID=4, name=name)


def dz5(bot, chat_id):
    msg = bot.send_message(chat_id, "Сколько тебе лет?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, inPut_int, bot, chat_id, responseID=5)


def dz6(bot, chat_id):
    msg = bot.send_message(chat_id, "Как тебя зовут?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, dz6_1, bot, chat_id)


def dz6_1(message, bot, chat_id, responseID = 6):
    name = message.text
    Find_Response(bot, chat_id, responseID, name)


def dz7(bot, chat_id):
    msg = bot.send_message(chat_id, text="Как тебя зовут?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, dz7_1, chat_id, bot)


def dz7_1(message, chat_id, bot):
    name = message.text
    msg = bot.send_message(chat_id, text="Сколько тебе лет?")
    bot.register_next_step_handler(msg, inPut_int, bot, chat_id, responseID=7, name=name)


def dz8(bot, chat_id):
    msg = bot.send_message(chat_id, "Как тебя зовут?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, dz8_1, bot, chat_id)


def dz8_1(message, bot, chat_id, responseID = 8):
    name = message.text
    inPut_int(message, bot, chat_id, responseID, name=name)


def dz9(bot, chat_id):
    msg = bot.send_message(chat_id, text="Как тебя зовут?", reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, dz9_1, bot, chat_id)


def dz9_1(message, bot, chat_id, responseID = 9):
    name = message.text
    msg = bot.send_message(chat_id, text="Сколько тебе лет?")
    bot.register_next_step_handler(msg, inPut_int, bot, chat_id, responseID=9, name=name)



def inPut_int(message, bot, chat_id, responseID, name=""):
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        Find_Response(bot, chat_id, responseID, name=name, age=var_int)
    except ValueError:
        bot.send_message(chat_id, text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...", reply_markup=Menu.getMenu("Главное меню").markup)







