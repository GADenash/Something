import telebot, wikipedia, re
bot = telebot.TeleBot('5773596797:AAFBo2QOHixwXsonrtqPk9NU58DhCNsI2zI')
wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('=='in x):
                if (len((x.strip()))>3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)','', wikitext2)
        return wikitext2
    except Exception as e:
        return 'К сожалению я не нашёл то что ты просил найти в Википедии:('
@bot.message_handler(commands = ["start"])
def start(m, res = False):
    bot.send_message(m.chat.id, 'Привет:) Я Телеграмм бот, ты можешь ввести мне любое слово, а я найду его значение в Википедии.')
@bot.message_handler(content_types = ["text"])
def handle_text(message):
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'Приет' or message.text == 'приет' or message.text == 'Првет' or message.text == 'првет' or message.text == 'Ghbdtn' or message.text == 'ghbdtn' or message.text == 'Ghdtn' or message.text == 'Ghbdn' or message.text == 'ghbtn' or message.text == 'ghbdn' or message.text == 'Пр вет':
        bot.send_message(message.from_user.id, 'Привет:) Что ты хочешь найти в Википедии?;)')
    else:
        bot.send_message(message.chat.id, getwiki(message.text))
bot.polling(none_stop= True, interval=0)