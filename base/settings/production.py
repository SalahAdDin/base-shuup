from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.uzman.tech', '.uzman.tech.']

ADMINS = [
    ('SalahAdDin', 'alagunasalahaddin@live.com'),
]

MANAGERS = ADMINS

INSTALLED_APPS += [
    'storages',
]

BASE_URL = 'http://uzman.tech'

GOOGLE_ANALYTICS_CODE = ""

# Server's Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        # 'PASSWORD': 'Uzman2017',
        'HOST': 'db',
        'PORT': '5432',
        'CONN_MAX_AGE': 1000,
        'ATOMIC_REQUESTS': True,
    }
}

# TODO: Review this options, follow tutorial steps
AWS_STORAGE_BUCKET_NAME = 'blog-uzman-tech'
AWS_ACCESS_KEY_ID = 'AKIAJF3FGE5LDIFIVSRQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_HEADERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}
AWS_S3_SECURE_URLS = True
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Static Files
MEDIA_ROOT = ''
STATIC_ROOT = ''
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), "static"),)

MEDIA_URL = '/static/media/'
STATIC_URL = '/static/static/'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        'KEY_PREFIX': 'uzman',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "COMPRESSOR": "django_redis.compressors.zlib.ZlibCompressor",
        }
    }
}

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch5',
        'URLS': ['http://elasticsearch:9200'],
        'INDEX': 'uzman',
        'ATOMIC_REBUILD': True,
        'TIMEOUT': 5,
        'OPTIONS': {},
        'INDEX_SETTINGS': {},
    }
}

CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Web Mail Servers
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_SUBJECT_PREFIX = '[Uzman Tech]'  # '[Rose designs]'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'oficial@.com'
SERVER_EMAIL = 'oficial@.com'

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = 'notification@'

WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True

# Security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True

# Webpack
WEBPACK_LOADER['DEFAULT']['CACHE'] = True

# Celery
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_SEND_TASK_ERROR_EMAILS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'config/logs/%s.log' % SITE_TITLE.lower()),
            'formatter': 'verbose',
            'maxBytes': 1024 * 1024 * 50,
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'error.log'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            'formatter': 'verbose',
        },
        'core': {
            'handlers': ['file', 'mail_admins'],
            'propagate': True,
            'level': 'ERROR',
            'formatter': 'verbose',
        },
        'wagtail': {
            'handlers': [],
            'level': 'INFO',
            'propagate': False,
            'formatter': 'verbose',
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
            'formatter': 'verbose',
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
