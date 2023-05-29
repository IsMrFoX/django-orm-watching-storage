import os
from dotenv import load_dotenv

load_dotenv()
db_password = os.getenv('BD_PASSWORD')
db_host = os.getenv('BD_HOST')
project_key = os.getenv('PROJECT_SECRET_KEY')
debug = os.getenv('DEBUG')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
allowed_hosts = os.getenv('ALLOWED_HOSTS')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': db_host,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = project_key

DEBUG = debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS =  allowed_hosts.split(',')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
