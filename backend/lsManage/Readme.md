Setting up the appltication
===========================
* Create a Virtualenv
* pip install -r requirements
* Add the products and graphenecatalog in settings.py INSTALLED_APPS section
    INSTALLED_APPS = [
        ...s
        'products',
        'graphenecatalog'
    ]
* Run migrations
python manage.py makemigrations
python manage.py migrate

* Load data

* Run the server
python manage.py runserver