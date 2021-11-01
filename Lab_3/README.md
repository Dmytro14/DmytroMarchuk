Створив папку з назвою лабораторної роботи у власному репозиторію. Перейшовши у папку ініціалізував середовище pipenv та встановив необхідні пакети:
```
pipenv --python 3.7
pipenv install django
```
За допомогою Django Framework створив заготовку (template) мого проекту  Для зручності виніс всі створені файли на один рівень вище щоб структура проекту була такою як показано нижче:
pipenv run django-admin startproject Dmytro_site
```
mv Dmytro_site/Dmytro_site/* Dmytro_site/
mv Dmytro_site/manage.py ./
```
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
```
pipenv run python manage.py runserver
```
Все запустилось успішно і стартова сторінка Django відображається коректно, зупинив сервер виконавши переривання Ctrl+C.
![Img](/pics/1.png "photo 1")
Далі створив темплейт свого додатку (app) у якому описано всі web сторінки сайту. Створив коміт із новоствореними файлами темплейту додатка:
```
pipenv run python manage.py startapp main
```
Використовуючи можливості IntelliJ створив папку main/templates/, а також у даній папці файл з розширенням .html (Dmytro_app.html). Також у папці додатку створив ще один файл Dmytro_app/urls.py. Зробив коміт із даними файлами;
Поєднав функції із реальними URL шляхами за якими будуть доступні веб сторінки заповнив файл Dmytro_app/urls.py згідно зразка.
Запустив сервер та переконався що сторінки доступні. Виконав коміт робочого Django сайту.
![Img](/pics/2.png "photo")
Роль моніторингу буде здійснювати файл monitoring.py який за допомогою бібліотеки requests буде опитувати сторінку health. Встановив дану бібліотеку;
```
pipenv install requests
```
Для здачі/захисту лабораторної потрібно зробити:
модифікувати функцію health так щоб у відповіді були: згенерована на сервері дата, URL сторінки моніторингу, інформація про сервер на якому запущений сайт та інформація про клієнта який робить запит до сервера;
```
def health(request):
    time = datetime.now()
    response = {'date': time.strftime("%Y-%m-%d %H:%M:%S"),
		 'current_page': request.build_absolute_uri(),
    		 'server_info': os.uname(),
    		 'client_info': request.headers['User-Agent']}
    return JsonResponse(response)
```
дописати функціонал який буде виводити повідомлення про недоступність сайту у випадку якщо WEB сторінка недоступна (як можна побачити функція requests.get() буде видавати помилку при недоступності сторінки);
```
try:
     r = requests.get(url)
     data = json.loads(r.content)
     logging.info("Server is available. Server time: %s", data['date'])
     logging.info("Requested page: : %s", data['current_page'])
     logging.info("Server response keys:")
     for key in data.keys():
          logging.info("Key: %s, Value: %s", key, data[key])
     except requests.exceptions.ConnectionError:
     logging.error("Server is unavailable")
return 0;
```
після запуску моніторингу запит йде лише один раз після чого програма закінчується - зробіть так щоб дана програма запускалась раз в хвилину та працювала в бекграунді (період запуску зробити через функціонал мови Python);
```
while True:
     time.sleep(60)
```
спростіть роботу з пайтон середовищем через швидкий виклик довгих команд, для цього зверніть увагу на секцію scripts у Pipfile. Я додав аліас на запуск сервера який тепер буде стартувати за командою представленою нижче. Зробіть аліас на запус моніторингу:
```
[scripts]
server = "python manage.py runserver 127.0.0.1:8000"
monitoring = "python3 monitoring.py"
```
Запустив сервер та переконався що головна сторінка відображається. Перейшов у інше вікно консолі та запустив програму моніторингу. Закомітив файл логів server.logs до репозиторію.