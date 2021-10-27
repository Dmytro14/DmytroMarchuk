
    Створив папку lab_2 з README.md файлом.
    За допомогою пакетного менеджера PIP інсталював pipenv та створив ізольоване середовище для Python. Ознайомився з командаю pipenv -h.

pip install pipenv
pipenv --python 3.7
pipenv shell

    Встановив бібліотеку requests. Також встановив бібліотеку ntplib яка працює з часом.

pipenv install requests
pipenv install ntplib


    Створив файл app.py. 
    Переконався що програма працює правильно.

python app.py

========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  03:59:29 PM
Date is:  10-27-2021
success
