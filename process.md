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

#### register app and config db -----
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

#### migrate db -----
`python manage.py migrate`

#### redirect project urls -----
in project folder, urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('eapp/', include('eapp.urls')),
]
```

in eapp folder, create urls.py

#### create first view -----
in eapp, views.py:

```python
from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request, 'eapp/index.html')
```

#### register the view with the urls -----
in eapp, urls.py:

```python
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
]
```

#### set up templates -----
in eapp, create 'templates' folder  
in templates, create base.html and add starter code  
in templates, create folder 'eapp' [same name as app; all other templates go here]  
in templates/eapp, create index.html and add code

#### run server -----
`python manage.py runserver`  
url is [ http://127.0.0.1:8000/eapp/ ]

#### create model classes -----
in eapp, models.py:

```python
from django.db import models
from django.contrib.auth.models import User
```

create model classes from given examples

#### migrate models to db -----
`python manage.py makemigrations`

#### register models in admin.py -----
in eapp, admin.py:

```python
from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(ExerciseType)
admin.site.register(Exercise)
```

#### create super user -----
`python manage.py createsuperuser`

#### run server and log in to admin -----
`python manage.py runserver`  
url is [ http://127.0.0.1:8000/admin/ ]

add sample data

#### import models -----
in views.py:

```python
from .models import *
```

#### create exercise types view -----

```python
def getExerciseTypes(request):
    type_list=ExerciseType.objects.all()
    return render(request, 'eapp/extypes.html', {'type_list': type_list})
```

#### add the url -----
in eapp, urls.py:

```python
path('extypes/', views.getExerciseTypes, name='extypes'),
```

#### create template -----
in templates/eapp, create extypes.html and add code

#### add link to base.html -----

```html
<ul class="nav navbar-nav">
	<li><a href="{% url 'extypes' %}">Exercise Types</a></li>
               
</ul>
```

#### create exercise view -----

```python
def getExercises(request):
    exercise_list=Exercise.objects.all()
    return render(request, 'eapp/exercises.html', {'exercise_list': exercise_list})
```

#### add the url -----
in eapp, urls.py:

```python
path('exercises/', views.getExercises, name='exercises')
```

#### create template -----
in templates/eapp, create exercises.html and add code

#### add link to base.html -----

```html
<li><a href="{% url 'exercises' %}">Exercises</a></li>
```

#### create details view -----
in views.py, add new import:

```python
from django.shortcuts import get_list_or_404, get_object_or_404
```

add new view:

```python
def exerciseDetails(request, id):
    exer=get_object_or_404(Exercise, pk=id)  # don't forget the model name here!!
    context={
        'exer' : exer,
    }
    return render(request, 'eapp/exdetails.html', context=context)
```

#### register url -----
in eapp, urls.py:

```python
path('exdetails/<int:id>', views.exerciseDetails, name='exdetails'),
```

### modify exercise template -----

```html
<td><a href="{% url 'exdetails' id=e.id %}">{{ e.exerciseName }}</a></td> <!-- make sure to update object! (e) -->
```

#### create details template -----
in templates/eapp, create exdetails.html and add code
