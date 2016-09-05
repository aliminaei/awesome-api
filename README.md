# awesome-api
Awesome API is an example REST API using Django REST framework.
Try our live interactive [docs] or [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)


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
5. `python manage.py runserver 0.0.0.0:8080`
6. Go to [api docs]

[Python]: https://www.python.org/download/releases/2.7/ "Python 2.7"
[pip]: https://pypi.python.org/pypi/pip "pip"
[django]: https://www.djangoproject.com/ "Django==1.9.7"
[django-filter]: http://django-filter.readthedocs.io/en/latest/usage.html "django-filter"
[djangorestframework]: http://www.django-rest-framework.org/ "djangorestframework"
[Markdown]: https://pypi.python.org/pypi/Markdown/ "Markdown"
[gunicorn]: http://gunicorn.org/ "gunicorn"
[api docs]: http://127.0.0.1:8080/docs/ "http://127.0.0.1:8080/docs/"
[whitenoise]: https://pypi.python.org/pypi/whitenoise "whitenoise"
[drfdocs]: http://drfdocs.com/ "drfdocs"
[docs]: http://awesome-api.herokuapp.com/docs "docs"

API Usage
============
## Create a new API User [POST /api/users/]

+ Parameters
    + username:  (required, unique, string, min length=3, max length=254) - The username of the API user in form of a string. 
    + email:     (required, string, max length=254) - The email address of the API user in form of a string. 
    + password   (required, string, min length=3, max length=254) - The password of the API user in form of a string. 
    + first_name (optional, string, max length=254) - The first name of the API user in form of a string. 
    + last_name  (optional, string, max length=254) - The last name of the API user in form of a string. 

+ Request (application/json)
    + Body
        ```js
        {
            "username": "username",
            "password": "password",
            "email": "mail@mail.com"
            "first_name": "fname",
            "last_name": "lname",
        }
        ```

+ Response 201

    + Body
        ```js
        {
            "username": "username",
            "email": "mail@mail.com"
            "first_name": "fname",
            "last_name": "lname",
        }
        ```

## Retrive the list of all API Users [GET /api/users/]

+ Response 200

    + Body
        ```js
        [
            {
                "username": "username",
                "email": "mail@mail.com"
                "first_name": "fname",
                "last_name": "lname",
            },
            {
                "username": "username2",
                "email": "mail2@mail.com"
                "first_name": "fname2",
                "last_name": "lname2",
            },
            {
                "username": "username3",
                "email": "mail3@mail.com"
                "first_name": "fname3",
                "last_name": "lname3",
            }
        ]
        ```

## Retrive the details of an API Users [GET /api/users/{username}]

+ Path Parameters
    + username:  (required, unique, string, min length=3, max length=254) - The username of the API user in form of a string. 

+ Response 200

    + Body
        ```js
        {
            "username": "username",
            "email": "mail@mail.com"
            "first_name": "fname",
            "last_name": "lname",
        }
        ```

## Delete the API Users [DELETE /api/users/{username}]

+ Path Parameters
    + username:  (required, unique, string, min length=3, max length=254) - The username of the API user in form of a string. 

+ Header Parameters
    + API_SECRET:  (required, unique, string, max length=254) - Your api secret. 

+ Response 204

