
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


    Встановив бібліотеку pytest.

pipenv install pytest

   Запустив тести та переконався що тести виконались успішно:

pytest tests/tests.py

================================ test session starts =================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/dmytro/Стільниця/reps/DmytroMarchuk/Lab_2
collected 5 items                                                                    

tests/tests.py .....                                                           [100%]

================================= 5 passed in 1.10s ==================================

exclamation (Захист) У програмі дописав функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Доброго дня/ночі;
def home_work(t):
    if 'PM' in t:
        print("Доброї ночі")
    if 'AM' in t:
        print("Доброго ранку")
exclamation (Захист) Написав тест що буде перевіряти правильність виконання функції;
  def test_home_work(self):
        # Ваш захист
        self.assertEqual(home_work("20:20:20 PM"), "Доброї ночі")
        self.assertEqual(home_work("10:10:10 AM"), "Доброго дня")

За допомогою команд pytest tests/tests.py > results.txt та python app.py >> results.txt перенаправив результат виконання тестів, а також результат виконання програми, у файл results.txt.
Зробив коміт зі змінами до репозиторію.
