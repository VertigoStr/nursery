# Запуск

## С докером:
Убедитесь, что 80 и 35432 порты свободны и выполните `./scripts/up.sh`.

В браузере откройте https://nursery.lvh.me. Если главная страница не открылась, то подождите минуту
и попробуйте ещё раз (при первом запуске подождать стоит больше). Если проблема не решилась, то
отправьте последние логи backend разработчику.

Postgresql: доступен на порту 35432
Swagger: https://nursery.lvh.me/api/

Содание суперпользователя:
```
./scripts/bash_app.sh
python server/manage.py createsuperuser
```

#### Возможные проблемы:

Если контейнер с базой данных запустится чуть позже чем контейнер uwsgi-nursery,
то, возможно, миграции не успеют выполниться, чтобы решить эту проблему, достаточно выполнить:
`./scripts/migrations.sh`

## Без докера:
Выполнить миграции:
```
python server/manage.py migrate --settings=core.settings.local
```

Создать суперпользователя:
```
python server/manage.py createsuperuser --settings=core.settings.local
```

Запустить проект:
```
python server/manage.py runserver --settings=core.settings.local
```
Swagger: https://127.0.0.1:8000/api/


# Структура
* client/src/ - папка для фронта.
* server/apps/ - приложения
* server/core/settings - настройки


# Отладка
Для создания точки остановки, добавьте следующий код в нужное место:
```
from pudb.remote import set_trace; set_trace(term_size=(120, 35))
```

После чего со своей локальной машины запустите команду:
```
telnet 0.0.0.0 6900
```
Если после выхода из отладчика возникают какие-то проблемы - перезапустите 
uwsgi контейнер или проект целиком.

# Переменные окружения
  * __SECRET_KEY__
  * __DISABLE_COLLECTSTATIC__ - включить (0) или выключить (1) автоматический запуск collectstatic в бесконечном цикле. 
  * **ENABLE_DEBUG_TOOLBAR**
  * **PUDB_RDB_HOST**
  * **PUDB_RDB_PORT**

# Тесты
```
python server/manage.py test apps.child
python server/manage.py test apps.journal
```
