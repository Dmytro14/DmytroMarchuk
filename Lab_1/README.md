# DmytroMarchuk

## Лабораторна робота №1

1. git clone https://github.com/Dmytro14/DmytroMarchuk.git

2. Закомітив README.md командою git add. Потім задопомогою команди `git commit` закомітив файл до репозиторію.

3. Командою git log дізнався хеш коміту з інформацією про всі коміти звідки я взяв хеш попереднього коміту: git log 6e24bc7dc9990d27ecc1e9f919f88be4ae39b4ac

4.  Створив відгалуження/гілку (branch) командою git branch NewBranch та перейшов з поточної main на новостворену. Для переключення між гілками використав команду git checkout NewBranch.

5. При переході на гілку master виявив, що внесені зміни не відображаються, будучи на гілці NewBranch, вони не впливають на основну гілку NewBranch.

6. Створив pull request на злиття (merge) новоствореної гілки у головну main. У ході злиття виникли конфлікт, який було усунено.

7. Я вважаю що, конфлікт виник через те, що робота виконувалась на тій самій стрічці файлу, як на гілці main, так і на гілці NewBranch, а саме на 13-тій стрічці. На кожній гілці був свій текст і гіт не зміг сумістити ці файли. Через це доводилось власноруч редагувати файли.

8. Створивши папку Lab_ та перемістивши файл README.md у неї, впевнився у відображенні вмісту у web-версії.

9. У Web версії GitHub вибрав файл README.md та натиснув на піктограму редагування файлу.