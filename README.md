# awesome-api
Awesome API is an example REST API using Django REST framework.
Try our live interactive [docs].


Requirements
============

It is tested with the following versions. Add the missing packages to the requirements.txt of your Django project 

1. [Python]
2. [pip]
3. [Django] ver. 1.9.7
4. [django-filter] ver. 0.13.0
5. [djangorestframework] ver. 3.4.6
6. [Markdown] ver. 2.6.6
7. [gunicorn] ver. 19.6.0
8. [whitenoise] ver. 3.2.1
9. [drfdocs] ver. 0.0.11

Installation
============

1. Clone this repo `git clone https://github.com/aliminaei/awesome-api.git`
2. `pip install -r requirements.txt`
3. `python manage.py collectstatic --noinput`
4. `python manage.py test`
5. `python manage.py runserver`
6. Go to [localhost]

[Python]: https://www.python.org/download/releases/2.7/ "Python 2.7"
[pip]: https://pypi.python.org/pypi/pip "pip"
[django]: https://www.djangoproject.com/ "Django==1.9.7"
[django-filter]: http://django-filter.readthedocs.io/en/latest/usage.html "django-filter"
[djangorestframework]: http://www.django-rest-framework.org/ "djangorestframework"
[Markdown]: https://pypi.python.org/pypi/Markdown/ "Markdown"
[gunicorn]: http://gunicorn.org/ "gunicorn"
[localhost]: http://127.0.0.1:8000/users/ "http://127.0.0.1:8000/users/"
[whitenoise]: https://pypi.python.org/pypi/whitenoise "whitenoise"
[drfdocs]: http://drfdocs.com/ "drfdocs"
[docs]: http://awesome-api.herokuapp.com/docs "docs"
