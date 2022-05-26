# Lab 28

## Django REST Framework and Docker

### Author

- Eden Brekke
- Followed the class demo and altered to what I wanted

### How to Run this Application

- python -m venv .venv
- .\.venv\Scripts\activate
- pip install django
- pip install djangorestframework
- django-admin startproject projectname
- python manage.py migrate
- python manage.py runserver
- python manage.py startapp app
- Make TUV and add to settings
- python manage.py makemigrations app
- python manaage.py createsuperuser
- python manage.py runserver

- docker compose up
- docker compose start

### Tests

- to run tests import the class PetPic
- import django.test import APITestCase
- python manage.py test to run tests

- I referenced the tests provided in today's demo

### Overview

- I appreciate the repetition with the labs this week, makes it easy to remember how to do Django.