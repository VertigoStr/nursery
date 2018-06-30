# Запуск
Убедитесь, что 80 и 35432 порты свободны и выполните `./scripts/up.sh`.

В браузере откройте https://nursery.lvh.me. Если главная страница не открылась, то подождите минуту
и попробуйте ещё раз (при первом запуске подождать стоит больше). Если проблема не решилась, то
отправьте последние логи backend разработчику.

Postgresql: доступен на порту 35432

Swagger: https://nursery.lvh.me/api/


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