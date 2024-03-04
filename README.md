# Задание:
-------
· 	Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

· 	Django Модель Item с полями (name, description, price)

· 	API с двумя методами:

· 	GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

· 	GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

·   Залить решение на Github

·   Запуск используя `Docker`

·   Просмотр Django Моделей в Django Admin панели доступно по адресу `http://localhost//admin`

·   Запуск приложения на удаленном сервере, доступном для тестирования - запущенно на `http://localhost/`

### Содержание: 

- [Задание:](#задание)
    - [Содержание:](#содержание)
    - [Краткое описание](#краткое-описание)
    - [Технологии](#технологии)
    - [Как запустить проект](#как-запустить-проект)
      - [Запуск проекта для развертывания на удаленном сервере](#запуск-проекта-для-развертывания-на-удаленном-сервере)
    - [Автор](#автор)
### Краткое описание 

### Технологии 


![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white) 
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 


### Как запустить проект 

Клонировать репозиторий: 

``` 
git clone https://github.com/Esperansa08/TestDjangoStripe.git

``` 
Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/Scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```



#### Запуск проекта для развертывания на удаленном сервере 

Должен быть запущен докер

Запустить программу:

```
docker-compose up -d
```

Выполнение миграции
``` 
docker exec -it testdjangostripe-app-1 python manage.py migrate
``` 
Загрузка статики
``` 
docker exec -it testdjangostripe-app-1 python manage.py collectstatic --no-input
``` 
После успешного запуска проект станет доступен по адресу: http://localhost/

Перейдя по ссылке, попадаете на карточку продукта, где можно сделать покупку, нажав на кнопку Buy

http://localhost/item/1

Для тестовой покупики использовать данные:

Эл. почта
``` 
testuser@gmail.com
``` 
Данные карты
``` 
4242 4242 4242 4242
``` 
Срок действия карты любой в будущем, например
``` 
05 / 25
``` 
CVV любое число, напимер
``` 
564
``` 
Имя владельца карты
``` 
testuser
``` 

### Автор 

 * Савельева Анастасия 
 * [Почта](Visteria09@yandex.ru), [Github](https://github.com/Esperansa08) 