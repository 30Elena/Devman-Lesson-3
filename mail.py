from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

letter = """\
From: {sender}
To: {recipient}
Subject: {title}
Content-Type: {content_type}

{message}"""

sender = 'iotasamurai@ya.ru'
recipient = 'iotasamurai@ya.ru'
title = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'
message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = letter.format(sender=sender, 
	recipient=recipient, 
	title=title, 
	content_type=content_type, 
	message=message)

letter = letter.replace('%website%', 'https://dvmn.org/profession-ref-program/lenayrakova/l7XDv/')
letter = letter.replace('%friend_name%', 'Александр')
letter = letter.replace('%my_name%', 'Елена')

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
login = os.getenv('login')
password = os.getenv('password')

server.login(login, password)
server.sendmail(sender, recipient, letter)
server.quit()