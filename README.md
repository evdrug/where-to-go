# Активный отдых, интерактивная карта Москвы
Интерактивная карта Москвы, на которой будут все известные виды активного отдыха с подробными описаниями и комментариями. 

Яндекс.Афиша занимается чем-то похожим, но это бездушный робот, собирающий всё подряд. Она никогда не обратит внимание на красивый канализационный люк или отвратительную вывеску.

![Скриншот](https://github.com/evdrug/where-to-go/tree/master/screen/img123.gif)

## Запуск локально (ознакомление, разработка)

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Создайте `.env` файл рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки. А так же подгружалтсь статические файлы при разработке.


Запустите разработческий сервер

```
python3 manage.py runserver
```

## Запуск на сервере (для общего пользования)

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

```sh
pip install -r requirements.txt
```

Создайте базу данных SQLite

```sh
python3 manage.py migrate
```

Создайте `.env` файл рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

- `DEBUG` — дебаг-режим. Поставьте `False`
- `SECRET_KEY` - [секретный ключ](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY).
- `DOMAIN` - [доменное имя вашего сайта](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-ALLOWED_HOSTS).
- `SESSION_COOKIE_SECURE` - [отправка cookie-session только по https](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SESSION_COOKIE_SECURE).
- `CSRF_COOKIE_SECURE`  - [отправка cookie-csrf только по https](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-CSRF_COOKIE_SECURE).

Собирает статические файлы:

```
python manage.py collectstatic
```


## Цели проекта

Код написан в учебных целях — для курса по Python и веб-разработке на сайте [Devman](https://dvmn.org).
