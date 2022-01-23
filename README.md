# learnet

## Installation
You need to have python installed on your computer.
You need to install `pipenv` with pip:
```
pip install pipenv
```

Then on your project folder (you need to do once for the first time)
```
pipenv install
```
Then get into virtualenv with the command below
```
pipenv shell
```
Now if you are running it for first time you need to make migrations to set up database.
```
python manage.py makemigrations
python manage.py migrate
```
Now you need to setup a superuser (with admin access)
```
python manage.py createsuperuser
```

Finally to run the server
```
python manage.py runserver
```
