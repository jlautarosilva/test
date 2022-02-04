Setting up the application
===========================

* Create a Virtualenv

* Install required packages

>pip install -r requirements

* Add the products and graphenecatalog in settings.py INSTALLED_APPS section

    >INSTALLED_APPS = [
    >    ...
    >    'products',
    >    'catalog',
    >    'graphene_django',
    >]

* Run migrations

>python manage.py makemigrations

>python manage.py migrate

* Add in settings.py

>GRAPHENE = {
>    "SCHEMA": "catalog.schema.schema"
>}


* Load data

>python manage.py

* Run the server

>python manage.py runserver


Running unit tests
===========================

* Run the tests for models and graphql catalog

>python manage.py test