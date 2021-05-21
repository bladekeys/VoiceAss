import datetime
import speech_recognition as sr

class TaskCard:
    permanent = True
    information = False
    task = False
    group = '2'
    deadline = '3'
    real_time = 'Не выполнено'
    send_time = ''
    author = ''
    header = '4'
    priority = 5
    task_type = 'Технологическая'
    status = 'new'
    comment = '2'
    text_task = '1'

    def _init_(self):
        self.permanent = True
        self.status = 'new'


    def set_def(self, author):
        self.permanent = True
        self.status = 'new'
        self.author = author


    def set_card(self, author):
        print("Какой тип задания?\n1. Постоянное\n2. Информация\n3. Задание\n> ")
        ans = int(input())
        if ans == 1:
            self.permanent = True
        elif ans == 2:
            self.information = True
        else:
            self.task = True

        print("Назначьте испонителя:\n> ")
        self.group = input()

        print("Назначьте срок выполнения:\n> ")
        self.deadline = input()

        now = datetime.datetime.now()
        self.send_time = str(now)

        self.author = author

        print("Введите заголовок:\n> ")
        self.header = input()

        print("Введите приоритет от 1 до 10:\n> ")
        self.priority = int(input())

        print("Введите тип задачи:\n1. Технологическая\n2. Техническая\n3. Организационная\n> ")
        ans = int(input())
        if ans == 1:
            self.task_type = "Технологическая"
        elif ans == 2:
            self.task_type = "Техническая"
        else:
            self.task_type = "Организационная"
        self.status = 'new'

        print("Введите задание:\n> ")
        self.text_task = input()

        print("Введите коментарий к заданию:\n> ")
        self.comment = input()



    def set_card_by_voice(self, author):
        main.talk("Какой тип задания?\n1. Постоянное\n2. Информация\n3. Задание\n> ")

        ans = int(input())
        if ans == 1:
            self.permanent = True
        elif ans == 2:
            self.information = True
        else:
            self.task = True

        main.talk("Назначьте испонителя:\n> ")
        self.group = convert_voice_to_str()

        main.talk("Назначьте срок выполнения:\n> ")
        self.deadline = convert_voice_to_str()

        now = datetime.datetime.now()
        self.send_time = str(now)

        self.author = author

        main.talk("Введите заголовок:\n> ")
        self.header = convert_voice_to_str()

        main.talk("Введите приоритет от 1 до 10:\n> ")
        self.priority = int(convert_voice_to_str())

        main.talk("Введите тип задачи:\n1. Технологическая\n2. Техническая\n3. Организационная\n> ")
        ans = int(convert_voice_to_str())
        if ans == 1:
            self.task_type = "Технологическая"
        elif ans == 2:
            self.task_type = "Техническая"
        else:
            self.task_type = "Организационная"
        self.status = 'new'

        main.talk("Введите задание:\n> ")
        self.text_task = convert_voice_to_str()

        main.talk("Введите коментарий к заданию:\n> ")
        self.comment = convert_voice_to_str()


    def say_the_card(self):
        string = self.convert_to_string()
        main.talk(string)


    def print(self):
        if self.permanent:
            print("Постоянное задание")
        elif self.information:
            print("Информация")
        else:
            print("Задание")
        print("Группа: " + self.group)
        if self.real_time:
            print("Срок выполнения: " + self.real_time)
        print("Время постановки задачи: " + self.send_time)
        print("Автор задания: " + self.author)
        print("Заголовок: " + self.header)
        print("Приоритет задания: " + str(self.priority) + "/10")
        print("Тип задания: " + self.task_type)
        print("Статус задания: " + self.status)
        print("Текст задания: " + self.text_task)
        print("Комментарий к заданию: " + self.comment)


    def convert_to_string(self):
        result = ''
        if self.permanent:
            result+="Постоянное задание\n"
        elif self.information:
            result+="Информация\n"
        else:
            result+="Задание\n"
        result+="Группа: " + self.group+"\n"
        if self.real_time:
            result+="Срок выполнения: " + self.real_time+"\n"
        else:
            result += "Срок выполнения: Не выполнено" + "\n"
        result+="Время постановки задачи: " + self.send_time+"\n"
        result+="Автор задания: " + self.author+"\n"
        result+="Заголовок: " + self.header+"\n"
        result+="Приоритет задания: " + str(self.priority) + "/10"+"\n"
        result+="Тип задания: " + self.task_type+"\n"
        result+="Статус задания: " + self.status+"\n"
        result+="Текст задания: " + self.text_task+"\n"
        result+="Комментарий к заданию: " + self.comment+"\n"
        return result


    def set_status(self, status):
        if status == 'ready':
            now = datetime.datetime.now()
            self.real_time = str(now)
        self.status = status

def convert_string_to_card(string):
    field_list = string.split('\n')
    tc = TaskCard()
    if field_list[0].startswith('Постоянное задание'):
        tc.permanent = True
    elif field_list[0].startswith('Информация'):
        tc.information = True
    elif field_list[0].startswith('Задание'):
        tc.task = True
    tc.group = field_list[1][8:]
    tc.real_time = field_list[2][17:]
    tc.send_time = field_list[3][25:]
    tc.author = field_list[4][15:]
    tc.header = field_list[5][11:]
    tc.priority = int(field_list[6][19:].split('/')[0])
    tc.task_type = field_list[7][13:]
    tc.status = field_list[8][16:]
    tc.text_task = field_list[9][15:]
    tc.comment = field_list[10][23:]
    return tc


def compare_cards(crd, card):
    if (
        crd.permanent == card.permanent and
        crd.information == card.information and
        crd.task == card.task and
        crd.group == card.group and
        crd.deadline == card.deadline and
        crd.real_time == card.real_time and
        crd.send_time == card.send_time and
        crd.author == card.author and
        crd.header == card.header and
        crd.priority == card.priority and
        crd.task_type == card.task_type and
        crd.comment == card.comment and
        crd.text_task == card.text_task
            ):
            if crd.status != card.status:
                return 1
            else:
                return 0
    return 2


def convert_voice_to_str():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
    zadanie = r.recognize_google(audio, language="ru-RU").lower()
    return zadanie
# tc = TaskCard()
# tc.set_card(author='Начальник')
# string = tc.convert_to_string()
# tc1 = convert_string_to_card(string)
# tc1.print()
