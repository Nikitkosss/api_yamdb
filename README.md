# Учебный проект YaMDb

## Команда разработки:

- :sunglasses: [Никита Пискунов (в роли Python-разработчика Тимлид - разработчик 2)](https://github.com/Nikitkosss)
- :white_check_mark: [Николай Ибраев (в роли Python-разработчика - разработчик 1)](https://github.com/Melnik-ni)
- :white_check_mark: [Вячеслав Мельников роль (в роли Python-разработчика - разработчик 3)](https://github.com/ViacheslavMelnikov)

### Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха.
Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число).
На одно произведение пользователь может оставить только один отзыв.
Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Технологии
***
* Python 3.9 
* Django 3.2 
* Django Rest Framework
* SQlite3
***

### Как запустить проект в dev-режиме:

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone git@github.com:Nikitkosss/api_yamdb.git
```

```
cd api_yamdb
```

Cоздайте и активируйте виртуальное окружение.

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установите зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейдите в папку api_yamdb/api_yamdb:

```
cd api_yamdb/api_yamdb
```

Примените миграции:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Запустите проект:

```
python manage.py runserver
```

Подробная документация проекта будет доступна по адресу http://127.0.0.1:8000/redoc/
