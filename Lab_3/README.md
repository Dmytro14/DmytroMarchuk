

Створив папку з назвою лабораторної роботи у власному репозиторію. Перейшовши у папку ініціалізував середовище pipenv та встановив необхідні пакети:

pipenv --python 3.7
pipenv install django

За допомогою Django Framework створив заготовку (template) мого проекту  Для зручності виніс всі створені файли на один рівень вище щоб структура проекту була такою як показано нижче:

pipenv run django-admin startproject Dmytro_site

mv Dmytro_site/Dmytro_site/* Dmytro_site/
mv Dmytro_site/manage.py ./

lab3/
├── Dmytro_site/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
├── Pipfile.lock
├── Pipfile
└── manage.py

Переконався що все встановилось правильно і я можу запустити Django сервер. Виконав команду вказану нижче та перейшов за посиланням яке вивелось у консолі:

pipenv run python manage.py runserver

Все запустилось успішно і стартова сторінка Django відображається коректно, зупинив сервер виконавши переривання Ctrl+C.
![Alt text](./home/dmytro/Зображення/1.png)
