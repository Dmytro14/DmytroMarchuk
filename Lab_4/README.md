1. Виконав команди: 
```
sudo docker -v
sudo docker -h
sudo docker run docker/whalesay cowsay Docker is fun
```
2. Виконав команди:
```
sudo docker pull python:3.8-slim
sudo docker images
sudo docker inspect python:3.8-slim
```
3. Скопіював та редагував файл *Dockerfile*
4. Створив репозиторій на DockerHub
5. Виконав команди:
```
sudo docker build -t dmytomarchuk/labs:django .
sudo docker images 
```
REPOSITORY          TAG        IMAGE ID       CREATED          SIZE
dmytomarchuk/labs   django     8084f827509b   7 minutes ago    341MB
<none>              <none>     20eb083d8594   20 minutes ago   276MB
python              3.8-slim   214d62795dbb   2 weeks ago      122MB
hello-world         latest     feb5d9fea6a5   7 weeks ago      13.3kB
docker/whalesay     latest     6b362a9f73eb   6 years ago      247MB
```
sudo docker push dmytomarchuk/labs:django
```
Посилання на [репозиторій](https://hub.docker.com/r/dmytomarchuk/labs)
Посилання на [імейдж](https://hub.docker.com/layers/dmytomarchuk/labs/django/images/sha256-40c95d98f8fd87b6451b5797db2ba5b2f6bff1c3fc493bc15e2605b379da7320?context=explore)

6. Виконав команду
```
sudo docker run -it --rm -p 8000:8000 dmytomarchuk/labs:django
```
7. Створив файл *Dockerfile.monitoring*
8. Виконав білд імейджа:
```
sudo docker build -t dmytomarchuk/labs:monitoring .
sudo docker images
sudo docker push dmytomarchuk/labs:monitoring 
```

9. Запустив імейдж моніторингу в окремому терміналі після чого витягнув з контейнеру server.log
 
