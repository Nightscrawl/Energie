# Energie Process: Start to Finish

in main class folder:
`venv\scripts\activate`

`django-admin startproject energie`

`cd energie`

`python manage.py startapp eapp`

make github repo with project name

remove *everything* from main folder

clone repo into empty folder

move everything back into folder

###### register app and config db -----
in project folder, settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eapp',
]
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'energiedb',
        'USER': 'postgres',
        'PASSWORD': '-----',
        'HOST':'localhost',
        'PORT':'-----',
    }
}
```

in pgAdmin4:
right-click on 'databases' and create new db, same name as one registered in settings.py

###### migrate db -----
`python manage.py migrate`

###### redirect project urls -----
```python
in project folder, urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eapp/', include('eapp.urls')),
]
```

in eapp folder, create urls.py