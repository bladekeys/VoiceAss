####Исправить: понимает команды со второго раза
####Калькулятор работает только на сложение
###Пробо=лема с двоным запросом отображения заключается в том, что сначала мы активируем ункцию вызова, а уже после повторно саму функцию

import speech_recognition as sr
import os
import sys
import sysenv
import webbrowser
import pyttsx3
import re
import datetime
from fuzzywuzzy import fuzz
import pyowm
import requests
import wikipedia

import pygame


#"alias": ('марта', 'арта', 'мата', 'март'),
opts = {"tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как','сколько','поставь','переведи', "засеки",'запусти','сколько будет','открой','сколько будет', 'давай','включи'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
			 "weath": ('какая погода','погоду заокном','погода заокном', 'погоду', 'о погоде'),
			 "name" : ('свое имя','имя','как тебя зовут','как звать',),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "засеки время"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "останови"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутка", "прикол"),
             "calc": ('прибавить','умножить на','разделить на','в степени','вычесть','поделить','х','+','-','/'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи', 'выключи компьютер'),
             "conv": ("валюта", "конвертер","доллар",'руб','евро'),
             "internet": ('открой', 'вк', 'гугл', 'сайт', 'вконтакте', 'ютуб'),
			 "internet2": ('покажи в интернете', 'открой в интернете', 'покажи в google', 'открой в браузере', 'загугли'),
			 "internet3": ('почту', 'почта'),
			 "wiki": ('мне', 'про', 'расскажи про'),
			 "opsys": ('на пк','на компьютере','на машине','програумму','прогу','приложение'),
             "translator": ("переводчик","translate"),
			 "bye": ("до свидания"," пока","прощай","выключись ","выключайся"),
			 "music": ("музыку", "музыка"),
			 "say": ("прочитай", "озвучь", "зачиатай", "мои задания", "задание"),
             "deals": ("дела","делишки", 'как сам', 'как дела')}}


# привод озвучки
def talk(words):
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()
# озвучка
print("Привет, чем я могу помочь вам?")
talk("Привет, чем я могу помочь вам?")


def command():
	# определеем данные
	r = sr.Recognizer()
	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		print("")
		# Устанавливаем паузу между прослушиванием 1 сек
		r.pause_threshold = 0.5
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=0.5)
		# Полученные данные записываем в переменную audio
		# пока есть лишь mp3 звук
		audio = r.listen(source)

	try:
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		global zadanie
		zadanie = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + zadanie)

	except sr.UnknownValueError:
		talk("")
		zadanie = command()
		#global zadanie
	# В конце функции возвращаем string
	return  zadanie

#now = datetime.datetime.now()



# Данная функция служит для проверки текста,
# что сказал пользователь (zadanie - текст от пользователя)
def definition(zadanie):
	if zadanie.startswith(opts["tbr"]):
		cmd = zadanie
		for x in opts['tbr']:
			cmd = cmd.replace(x, "").strip()
		zadanie = cmd
		cmd = recognize_cmd(zadanie)
		execute_cmd(cmd['cmd'])

def recognize_cmd(zadanie):
	RC = {'cmd': '', 'percent': 0}
	for c, v in opts['cmds'].items():
		for x in v:
			vrt = fuzz.ratio(zadanie, x)
			if vrt > RC['percent']:
				RC['cmd'] = c
				RC['percent'] = vrt
	return RC








def execute_cmd(cmd):
	global startTime
	if cmd == 'ctime':
		now = datetime.datetime.now()
		print('Сейчас ' + str(now.hour) + " часов " + "и " + str(now.minute) + " минуты")
		talk('Сейчас' + str(now.hour) + "часов" + "и" + str(now.minute) + "минуты")
		#talk("Сейчас {0}:{1}".format(str(now.hour), str(now.minute)))
	elif cmd == 'internet':
		browser1()
	elif cmd == 'internet2':
		browser2()
	elif cmd == 'internet3':
		browser3()
	elif cmd == 'calc':
		print("5+5=10")
		calculator()
	#elif cmd == 'translator':
	#	translate()
	elif cmd == 'weath':
		weather()
	elif cmd == 'name':
		print("Меня зовут Марта")
		talk("Меня зовут Марта")
	elif cmd == 'wiki':
		TellOther()
	elif cmd == 'opsys':
		openSysApp()
	elif cmd == 'music':
		OpMus()
	elif cmd == 'say':
		say()
	elif cmd == 'bye':
		talk("До скорой встречи")
		sys.exit()

def say():
	talk("У вас есть одно Задание")
	talk("от Иванова Ивана")
	talk("Срок выполнения: 20.12.2020")
	talk("Сделать гайку")
	talk("приоритет 5 из 10")
	talk("Текст задания: Сделай мне 100 гаек")
	talk("Комментарий к заданию: но только красивыми и блестящими")
	talk("конец задания")
###### дописать
def OpMus():
	pygame.init()
	song = pygame.mixer.Sound('d:\Music\MusicMP3\Music\One_Republic_-_Good_Life(1).mp3')
	clock = pygame.time.Clock()
	song.play()
	while True:
		clock.tick(20)
	pygame.quit()

def openSysApp():
	#os.startfile(r'd:\Program Files (x86)\Steam\steam.exe')
	apps = {'d:\Program Files (x86)\Steam\steam.exe': ['steam', 'стим'], "C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe": ["фотошоп", "photoshop"],
			 "C:\Vova\AppData\Roaming\Spotify\Spotify.exe": ["spotify", "спотифай"],
			 "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe": ["google", "chrome", "гугл", "хром"],
			 "c:\Program Files\Windows Media Player\wmplayer.exe": ["медиа плеер", "media player", "медиаплеер", "mediaplayer"],
			 "D:\Program Files\iTunes\iTunes.exe": ["itunes", "айтюнс"]}
	app = zadanie.split()
	for k, v in apps.items():
		for i in v:
			if i not in app[-1].lower():
				open_app = None
			else:
				talk('Уже запускаю')
				#k= 'r'+"'"+k+"'"
				open_app = os.startfile(k)

				break
		if open_app is not None:
			break

def browser2():
	domain = str(zadanie)
	domain = (domain.replace('покажи в интернете', ''))
	print(domain)
	talk('Вот что удалось найти')
	url = 'https://yandex.ru/search/?text=' + domain
	webbrowser.open_new_tab(url)


def TellOther():
	reg_ex = re.search('расскажи про (.*)', command)
	try:
		if reg_ex:
			topic = reg_ex.group(1)
			ny = wikipedia.page(topic)
			print(ny.url)
			talk(ny.content[:500].encode('utf-8'))
	except Exception as e:
		talk(e)

def browser1():
	domain = str(zadanie)
	domain = (domain.replace('открой сайт ', ''))
	print(domain)
	talk('Уже открываю сайт')
	url = 'https://www.' + domain
	webbrowser.open_new_tab(url)


def browser3():
	url = 'https://mail.google.com/mail/u/0/#inbox'
	webbrowser.open_new_tab(url)




def browser():
    sites = {'https://www.youtube.com/':['youtube', 'ютуб'], "https://vk.com":["vk","вк"],  "https://ru.wikipedia.org": ["вики", "wiki"], "https://ru.aliexpress.com":["али", "ali", "aliexpress", "алиэспресс"], "http://google.com":["гугл","google"], "https://www.amazon.com":["амазон", "amazon"], "https://www.apple.com/ru":["apple","эпл"]}
    site = command().split()
    for k, v in sites.items():
        for i in v:
            if i not in site[-1].lower():
                open_tab = None
            else:
                open_tab = webbrowser.open_new_tab(k)
                break
        if open_tab is not None:
            break


def weather():
	s_city = "Moscow,RU"
	city_id = 524901
	appid = "ce8897da790757caa1e763de31f814de"
	try:
		res = requests.get("http://api.openweathermap.org/data/2.5/weather",
						   params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
		data = res.json()
	except Exception as e:
		print("Exception (weather):", e)
		pass
	talk("сейчас на улице в москве" + str(data['weather'][0]['description']) + "и" + str(data['main']['temp']) + "градусов")


def calculator():
    try:
        list_of_nums =zadanie.split()
        num_1,num_2 = int((list_of_nums[-3]).strip()), int((list_of_nums[-1]).strip())
        opers = [list_of_nums[0].strip(),list_of_nums[-2].strip()]
        for i in opers:
            if 'дел' in i or 'множ' in i or 'лож' in i or 'приба' in i or 'выч' in i or i == 'x' or i == '/' or i =='+' or i == '-' or i == '*':
                oper = i
                break
            else:
                oper = opers[-1]
        if oper == "+" or "ложа" or "приба" in oper:
            ans = num_1 + num_2
        elif oper == "-" or "выч" in oper:
            ans = num_1 - num_2
        elif oper == "х" or "множ" in oper:
            ans = num_1 * num_2
        elif oper == "/" or "дел" in oper:
            if num_2 != 0:
                ans = num_1 / num_2
            else:
                talk("Делить на ноль невозможно")
        elif "степень" or "в степени" in oper:
            ans = num_1 ** num_2

        talk("{0} {1} {2} = {3}".format(list_of_nums[-3], list_of_nums[-2], list_of_nums[-1], ans))
    except:
       talk("Скажите, например: Сколько будет 5+5?")


def translate():
	url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
	key = 'trnsl.1.1.20190227T075339Z.1b02a9ab6d4a47cc.f37d50831b51374ee600fd6aa0259419fd7ecd97'
	text = command().split()[1:]
	lang = 'en-ru'
	r = requests.post(url, data={'key': key, 'text': text, 'lang': lang}).json()
	try:
		command().speak(r["text"])
	except:
		command().speak("Обратитесь к переводчику, начиная со слова 'Переводчик'")

while True:
	definition(command())

# def makeSomething(zadanie):
# 	# Попросту проверяем текст на соответствие
# 	# Если в тексте что сказал пользователь есть слова
# 	# "открыть сайт", то выполняем команду
# 	if 'открой youtube' in zadanie:
# 		# Проговариваем текст
# 		talk("Уже открываю")
# 		# Указываем сайт для открытия
# 		url = 'https://www.youtube.com/'
# 		# Открываем сайт
# 		webbrowser.open(url)
#
# 	elif 'open reddit' in zadanie:
# 		reg_ex = re.search('open reddit (.*)', zadanie)
# 		url = 'https://www.reddit.com/'
# 		if reg_ex:
# 			subreddit = reg_ex.group(1)
# 			url = url + 'r/' + subreddit
# 		webbrowser.open(url)
# 		talk('The Reddit content has been opened for you Sir.')
# 	elif 'открой в интернете' in zadanie:
# 		# Проговариваем текст
# 		talk("Уже открываю")
# 		# Указываем сайт для открытия
# 		#url = 'https://yandex.ru/search/?lr=10735&text={}'.format('%x')
# 		# Открываем сайт
# 		webbrowser.open('https://yandex.ru/search/?lr=10735&text={}'.format('%x'))
#
# 	elif 'выключись' or 'выключайся' in zadanie:
# 		talk("Да, конечно, без проблем")
# 		sys.exit()
# 	elif 'как тебя зовут' in zadanie:
# 		talk("Меня зовут Марта")
# 	elif 'который сейчас час' in zadanie:
# 		talk('Сейчас' + str(now.hour) + "часов" + "и" + str(now.minute) + "минуты")
# 	elif "какая погода" in zadanie:
# 		talk("сейчас на улице в москве" + str(data['weather'][0]['description'])+ "и" +str(data['main']['temp']) + "градусов")
# 	elif "как твои дела" in zadanie:
# 		talk("Спасибо, неплохо. Не уверена, что я знаю, какими могут быть дела, ведь родилась я всего час назад")
# # Вызов функции для проверки текста будет
# # осуществляться постоянно, поэтому здесь
# # прописан бесконечный цикл while
# while True:
# 	makeSomething(command())