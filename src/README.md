# DjangoGit

Python backend developer assignment. Integrating GitHub with a Django application via the GitHub REST API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Django==3.0.5
psycopg2==2.8.5
django-crispy-forms==1.9.0
requests==2.23.0
django-service-objects==0.6.0
djangorestframework==3.11.0
PostgreSQL 12.2
Ngrok
```

### Installing

Clone the project. Then first create a virtualenv in the project directory ( you can create anywhere you want ). If you don't have virtualenv installed, simply install it using pip.

```
pip install virtualenv
```
then create a virtualenv in the desired directory. In this example I am giving the virtual environment name env (you can give any name). 

```
virtualenv env
```
you will find a env directory where the virtual environment is created. From terminal run the following command to activate the virtual environment.

##### Windows
```
env\scripts\activate
```
##### Mac OS / Linux
```
source env\bin\activate
```

now that your virtual env is setup and activated, we are ready to install our project Prerequisites.

#### To install all the prerequisites at once, from src directory (where the project_requirements.txt is) run:

```
pip install -r project_requirements.txt
```

you can check if all prerequisites are installed by the following command. It will display all the packages installed in the virtualenv.

```
pip freeze
```
## Setup Database (PostgreSQL): Create a role and a database and set all privileges to the role

1. db name = django_git
2. user = django_git
3. password = 1234

## Run db migration:

from src run:

```
python manage.py migrate
```

## Setting up Ngrok

download Ngrok from : [https://dashboard.ngrok.com/get-started/setup](https://dashboard.ngrok.com/get-started/setup)
Ngrok is needed for forwarding your localhost endpoint to live server.

**A.** Unzip the donwloaded file.  
**B.** From the extracted directory:  
for **Windows** using cmd run:  
```
ngrok http 8000
```
for **linux/mac** using terminal run:  
```
./ngrok http 8000
```
This will add the port and give you a link that will forward to 8000. You can use any other port that you want it to forward to.  
Ngrok terminal will open and you will find the line: 
```
Forwarding                    http://<###>.ngrok.io -> http://localhost:8000
```
**C.** Now copy the given link(example: "http://<###>.ngrok.io") and go to **src/DjangoGit** and open **application_properties.py**.  
**D.** Here assign the copied link to **forwarded_url** variable.   

### Run Server:

```
python manage.py runserver
```



