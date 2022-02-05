
Application architecture
========================

lsManage is an application developed for testing purposes that implement a simple catalog backend for managing products

This application has been created using:
- Django
- GraphQL (graphene_django & graphql_auth)
- Amazon SES (django_ses)

Each component live in an independent django application, this are:
- lsManage: The main application that contains the Django settings
- products: Product django application
- catalog: GraphQL catalog service for manage Users and Products

Future enhacement
- Decoupling email as an independent django app
- Implement separated settings.py files for local and server
- Implement more functionality to the models as:
    - Storage
    - Location
- Complement location with geodjango to know the location of Products


Deploy with docker
=================
* Download whis repository

* Move to the folder that contains docker-compose.yml file

* Run docker-compose

    >docker-compose up


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

    >python manage.py migrate

* Add in settings.py

    >GRAPHENE = {
    >    "SCHEMA": "catalog.schema.schema"
    >}


* Load data

    >python manage.py loaddata

* Run the server

    >python manage.py runserver


Running unit tests
===========================

* Run the tests for models and graphql catalog

    >python manage.py test