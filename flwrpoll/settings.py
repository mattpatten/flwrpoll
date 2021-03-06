"""
Django settings for flwrpoll project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Environment variables

SECRET_KEY 				= os.environ.get('DJANGO_SECRET_KEY') 	# SECURITY WARNING: keep the secret key used in production secret!
DEBUG 					= os.environ.get('DJANGO_DEBUG', False) == 'True' # SECURITY WARNING: don't run with debug turned on in production! 

# The above is to set debug as False unless explicitly stated as True. Issue arises with environment variables being strings.
#print('Debug status --> ' + str(DEBUG))

#These names are chosen specifically because they are settings for the django-storages package
AWS_ACCESS_KEY_ID 		 = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY 	 = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME  = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME		 = os.environ.get('AWS_REGION')
AWS_LOCATION 			 = 'static' 		# Path to prepend to storage location
AWS_QUERYSTRING_AUTH 	 = False   			# This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_DEFAULT_ACL 		 = None 			#Don't allow public access to reading bucket
AWS_S3_SIGNATURE_VERSION = 's3v4'

# How many fields we will allow on the admin page that can be received in a single get/post request (default 1000)
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000


ALLOWED_HOSTS = [
	'tflwrpoll.ap-southeast-2.elasticbeanstalk.com',
	'tflwrpoll3.ap-southeast-2.elasticbeanstalk.com',
	'watsonvisionlab.org',
	'www.watsonvisionlab.org',
	'127.0.0.1',
	'127.0.0.1:8000',
	'localhost',
]

# Application definition

INSTALLED_APPS = [
	'polls.apps.PollsConfig', #'myapp'
    'django_static_jquery',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'flwrpoll.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'flwrpoll.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
	DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Security

X_FRAME_OPTIONS = 'DENY' #stops the site being shown within a frame of another site/page


# Session variables

SESSION_EXPIRE_AT_BROWSER_CLOSE = False #don't delete sessions when the user closes the browser
SESSION_COOKIE_AGE = 604800  #delete session variable after x seconds (3600 = 1 hour, 86400 = 1 day, 604800 = 1 week, 2592000 = 30 days)


# Constants
MAX_TRIAL_NUM = 70
NUM_QUESTIONS_DISPLAYED = 2 #we show two scales/sliders/questions per slide


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

#static media settings
STATIC_URL = 'https://%s.s3-%s.amazonaws.com/%s/' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_LOCATION) # The URL to use when referring to static files (where they will be served from)
STATIC_ROOT = '/%s/' % (AWS_LOCATION) #where to send static files when using collectstatic


#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "/static")
#STATIC_ROOT = "C:/Matt/django/flwrpoll/polls/static/polls/"
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # The absolute path to the directory where collectstatic will collect static files for deployment.
