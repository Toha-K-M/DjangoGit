*** Instructions: ***

A. Run the following commands in the project root directory

1. virtualenv env
2. env\Scripts\activate
3. cd src
4. pip install -r requirements.txt

B. Setup Database (PostgreSQL): Create a role and a database and set all privileges to the role

1. db name = django_git
2. user = django_git
3. password = 1234



C. Run db migration:

1. python manage.py migrate


D: Run: python manage.py runserver
