
import requests
import random
from PIL import Image, ImageDraw


def getRandomROFL():
    from random import randint
    import bs4
    array = []
    anek = requests.get("http://anekdotme.ru/anekdot/random")
    soup = bs4.BeautifulSoup(anek.text, "html.parser")
    result = soup.select(".anekdot_text")
    for finalResult in result:
        array.append(finalResult.getText().strip())
    return array[0]


def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Рассказать анекдот!":
        bot.send_message(chat_id, text=getRandomROFL())



