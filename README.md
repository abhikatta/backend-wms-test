django_wms - core of the backend app

init file - defines the directory as a package

settings module - app settings are defined here duhh

urls module - yeah think what this does

asgi and wsgi - used for deployment ( to be explored how and what and what they stand for)

manage.py - wrapper around django-admin, for further commands that will be used
(from what i understand, its basically like npx)

# App

an app is NOT the entire app, its a FEATURE of the django app (backend devs call it django project and the feature as app)

IMPORTANT: after creating a new app, add it in the settings.py file under INSTALLED_APPS array

Each app consists:

- migrations folder: used to create db tables(tbd)
- admin.py: how the admin interface for this app(feature) is gonna look like
- apps.py: this is where we configure the app(feature)
- models.py: this is where the models are defined & pull data from db and show to user
- tests.py: unit tests
- views.py: basically a request handler(tbd), SEEMS important

## views.py:

each view or view function, takes in a request and returns a response

## urls mapping:

create a urls.py file for mapping the views(request handlers) to map to urls

what a view is called in other frameworks is called a template in django

template is what a user sees( html or css probably; tbd)
