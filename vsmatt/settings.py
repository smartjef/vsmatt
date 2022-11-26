"""
Django settings for vsmatt project.

Generated by 'django-admin startproject' using Django 4.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3dxpn&!736o$(pbypmhr4hnd$gftc&%+n2iinx-3h%7@+&0zd2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'vsmatt.azurewebsites.net',
    '*.vstech.live',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Local Apps
    'shop.apps.ShopConfig',
    'core.apps.CoreConfig',
    'users.apps.AccountConfig',
    'api.apps.ApiConfig',
    'business.apps.BusinessConfig',
    'products.apps.ProductsConfig',
    'order.apps.OrderConfig',

    # Third Party Apps
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',

    # 'django.contrib.gis', #needs a lot of dependencies
]

MIDDLEWARE = [
    # ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vsmatt.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'products.context_processor.product_categories',
                'cart.context_processor.cart',
                'business.context_processor.business_categories',
                'core.context_processor.vsmatt',

            ],
        },
    },
]

WSGI_APPLICATION = 'vsmatt.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# GOOGLE_MAPS_API_KEY = "AIzaSyBqovBTE3mf_f0ySwLd0XFpSOCuqY_3OWA"geoffre
GOOGLE_MAPS_API_KEY = "AIzaSyA0WoecFWukfc9lUgCVcA20W11Eoj49jpo"
MAPS_QUEST_API_KEY = "2dVBKmPmnGAdhlP4AG9HPv7X4dAznIYt"

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.users.auth_backends.AuthenticationBackend',
# ]

# Allauth configurations
SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_USERNAME_REQUIRED = True

# cart
CART_SESSION_ID = 'cart'
META_SESSION_ID = 'session_meta'

CSRF_TRUSTED_ORIGINS = [
    'https://*.azurewebsites.net',
    'http://*.vstech.live',
    'https://*.vstech.live',
]
