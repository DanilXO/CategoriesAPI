# CategoriesAPI

### Описание:
   Решение задания представленно в приложении categoriestree.
   Для API реализовано с помощью Django и Django REST framework.
   Для работы с деревьями данных использал: django-mptt.
   При разработке использовал Python 3.6
   Для простоты проверки и работы (так как пример небольшой и простой) использовал sqlite в качестве БД.
    
### Структура проекта:
    ├── categoriesapi
        ├── categoriestree
            ├── migrations
                ├──
            ├── static
                ├── categoriestree
                    ├── tests              # JSON файлы, представленные в задании (для тестирования)
            ├── admin.py                   # Для удобства Category model добавлена в админку
            ├── models.py                  # Модель Category c необходимыми полями. Наследуется от MPTTModel.
            ├── serializers.py             # Serializers для Category
            ├── test.py                    # Небольшие unit-тесты проверяющие корректную работу приложения
            ├── urls.py                    # Routes приложения
            ├── views.py                   # ViewSet для Category
    ├── manage.py                          
    ├── README.md                          
    ├── requirements.txt                   # Необходимые зависимости
            
