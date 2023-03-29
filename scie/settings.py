"""
Django settings for scie project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import environ
import os
from pathlib import Path

env = environ.Env(
    # POSTGRES_ENGINE=str,
    # POSTGRES_USER=str,
    # POSTGRES_PASSWORD=str,
    # POSTGRES_DB=str,
    # POSTGRES_HOST=str,
    # POSTGRES_PORT=str,
    SECRET_KEY=str,
)

# environ.Env.read_env(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/.env')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-yw*1tg0-3!00*&6hhnhy-#p*6$8m5r-#m5e9a)+5!sud13(1l2"

DEBUG = True

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'http://localhost:9000']
ALLOWED_HOSTS = ['ultapp-dev.us-west-2.elasticbeanstalk.com']

ADMINS = [('Admin','admin@admin.com'),('Misael', 'misaelvgm011@gmail.com')]

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.base',
    'apps.diarioVentasCompras',
    'apps.facturaCliente',
    'apps.facturaProveedor',
    'apps.libroDiario',
    'apps.libroMayor',
    'apps.pago',
    'apps.planContable',
    'apps.planificador',
    'apps.producto',
    'apps.proveedor',
    'apps.reporteFinanciero',
    'apps.salidaInventario',
    'apps.solicitudSuministro',
    'apps.transferencia',
    'apps.user',
    
]

THIRD_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'simple_history',
]

INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

TOKEN_EXPIRED_AFTER_SECONDS=900

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

ROOT_URLCONF = 'scie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'files')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'scie.wsgi.application'

if 'DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['DB_NAME'],
            'USER': os.environ['DB_USERNAME'],
            'PASSWORD': os.environ['DB_PASSWORD'],
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ['DB_PORT'],
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': env('POSTGRES_ENGINE'),
            'NAME': 'sci_iu',
            'USER': 'sci_iu',
            'PASSWORD': 'complexpassword123',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'user.User'

STATIC_URL = 'static/'
STATIC_ROOT = 'static'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://localhost:9000",
    "http://localhost:9300",
    "http://localhost"
]
