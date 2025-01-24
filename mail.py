from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

letter = ("""\
From: {sender}
To: {recipient}
Subject: {title}
Content-Type: {content_type}

{message}""")

sender = 'iotasamurai@ya.ru'
recipient = 'iotasamurai@ya.ru'
title = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'
message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

dvmn.org — это новая версия онлайн-курса..."""

letter = letter.format(sender=sender, 
	recipient=recipient, 
	title=title, 
	content_type=content_type, 
	message=message)

letter = letter.replace('%website%', 'https://dvmn.org/profession-ref-program/lenayrakova/l7XDv/')
letter = letter.replace('%friend_name%', 'Александр')
letter = letter.replace('%my_name%', 'Елена')
print(letter)

letter = letter.encode("UTF-8")
print(letter)

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
login = os.getenv('login')
password = os.getenv('password')

server.login(login, password)
server.sendmail(sender, recipient, letter)
server.quit()