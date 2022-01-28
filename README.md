### Описание. 
API для проекта YaTube (V1).
Создан в ходе обучения по специальности Python-разработчик Яндекс-практикума.
Январь 2022

### Установка.
Клонировать репозиторий:

```
git clone https://github.com/iurij-n/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
После запуска сервера полная документация API будет доступна по адресу: http://127.0.0.1:8000/redoc/

### Примеры.
Некоторые примеры запросов к API.

Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.
```
http://127.0.0.1:8000/api/v1/posts/
```

Получение всех комментариев к публикации {post_id}.
```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Получение списка доступных сообществ.
```
http://127.0.0.1:8000/api/v1/groups/
```

Получение JWT-токена.
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
