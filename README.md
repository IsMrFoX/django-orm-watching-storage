# Bank security console

This is the internal repository of the bank "Radiance", if you got here by accident, then you will not be able to run this project at home, but you can use this code in your projects.
This project is aimed at identifying suspicious individuals in the bank.
---
### How to install:
Before starting, you need to create a .env file containing:

```python
BD_PASSWORD = 'Database password',
BD_HOST = 'Databdase host',
PROJECT_SECRET_KEY = 'Secret key',
DEBUG = 'true or false'
DB_PORT = 'Database port'
DB_NAME = 'Database name'
DB_USER = 'Database user'
ALLOWED_HOSTS = 'ALLOWED_HOSTS'
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
---
## Starting the server:
```
python manage.py runserver
```
---
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).