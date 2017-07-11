from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _

from shuup.addons import add_enabled_addons


# PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.getenv("SHUUP_WORKBENCH_BASE_DIR") or (os.path.dirname(os.path.dirname(__file__)))
# BASE_DIR = os.path.dirname(PROJECT_DIR)

try:
    SECRET_KEY
except NameError:
    SECRET_FILE = os.path.join(BASE_DIR, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            import random

            SECRET_KEY = ''.join(
                [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)]
            )
            secret = open(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            Exception('Please create a %s file with random characters \
            to generate your secret key!' % SECRET_FILE)

ALLOWED_HOSTS = []

SITE_TITLE = 'Shuup'
SITE_HEADER = _('Development and Design')



SHUUP_ENABLED_ADDONS_FILE = os.getenv("SHUUP_ENABLED_ADDONS_FILE") or (os.path.join(BASE_DIR, "addons"))

SHUUP_APPS = [
    # shuup themes
    'shuup.themes.classic_gray',
    # shuup
    'shuup.core',
    'shuup.admin',
    'shuup.api',
    'shuup.addons',
    'shuup.default_tax',
    'shuup.front',
    'shuup.front.apps.auth',
    'shuup.front.apps.carousel',
    'shuup.front.apps.customer_information',
    'shuup.front.apps.personal_order_history',
    'shuup.front.apps.saved_carts',
    'shuup.front.apps.registration',
    'shuup.front.apps.simple_order_notification',
    'shuup.front.apps.simple_search',
    'shuup.front.apps.recently_viewed_products',
    'shuup.notify',
    'shuup.simple_cms',
    'shuup.customer_group_pricing',
    'shuup.campaigns',
    'shuup.simple_supplier',
    'shuup.order_printouts',
    'shuup.testing',
    'shuup.utils',
    'shuup.xtheme',
    'shuup.reports',
    'shuup.default_reports',
    'shuup.regions',
    'shuup.importer',
    'shuup.default_importer',
]

THIRD_PARTY_APPS = [
    'jet.dashboard',
    'jet',

    'axes',
    'bootstrap3',
    'django_countries',
    'django_extensions',
    'django_jinja',
    'django_filters',
    'easy_thumbnails',
    'filer',
    'registration',
    'rest_framework',
    'rest_framework_swagger',
    'robots',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]

INSTALLED_APPS = add_enabled_addons(SHUUP_ENABLED_ADDONS_FILE, [
] + THIRD_PARTY_APPS + DJANGO_APPS + SHUUP_APPS)

MIDDLEWARE_CLASSES = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'shuup.front.middleware.ProblemMiddleware',
    'shuup.front.middleware.ShuupFrontMiddleware',

]

ROOT_URLCONF = 'base.urls'

_TEMPLATE_CONTEXT_PROCESSORS = [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',

    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.tz',
    'django.template.context_processors.static',

    # 'core.context_processors.analytics',
    # 'core.context_processors.utils',
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
            "newstyle_gettext": True,
            "environment": "shuup.xtheme.engine.XthemeEnvironment",
        },
        "NAME": "jinja2",
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": _TEMPLATE_CONTEXT_PROCESSORS,
        }
    },
]

WSGI_APPLICATION = 'base.wsgi.application'

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

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
    ('tr', _('Turkish')),
]

LANGUAGE_CODE = 'es-co'

PARLER_DEFAULT_LANGUAGE_CODE = "es"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = '/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

AXES_LOGIN_FAILURE_LIMIT = 3
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = 24
AXES_LOCKOUT_TEMPLATE = '429.html'

ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24

ROBOTS_SITEMAP_URLS = [
    'http:///sitemap.xml',
]

ROBOTS_SITEMAP_VIEW_NAME = 'cached-sitemap'

THUMBNAIL_HIGH_RESOLUTION = True

JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'violet',
        'color': '#a464c4',
        'title': 'Violet'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

JET_DEFAULT_THEME = 'default'

# JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'

# JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard'

# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

# JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(PROJECT_DIR, 'client_secrets.json')

SHUUP_PRICING_MODULE = "customer_group_pricing"

SHUUP_ENABLE_MULTIPLE_SUPPLIERS = True

SHUUP_ENABLE_MULTIPLE_SHOPS = True

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'shuup.api.permissions.ShuupAPIPermission',
    )
}

JWT_AUTH = {
    'JWT_ALLOW_REFRESH': True
}

SWAGGER_SETTINGS = {
    "SUPPORTED_SUBMIT_METHODS": [
        "get"
    ]
}

SHUUP_SETUP_WIZARD_PANE_SPEC = [
    "shuup.admin.modules.shops.views:ShopWizardPane",
    "shuup.admin.modules.service_providers.views.PaymentWizardPane",
    "shuup.admin.modules.service_providers.views.CarrierWizardPane",
    "shuup.xtheme.admin_module.views.ThemeWizardPane",
    "shuup.admin.modules.content.views.ContentWizardPane",
    "shuup.admin.modules.sample_data.views.SampleObjectsWizardPane"
]


SHUUP_ERROR_PAGE_HANDLERS_SPEC = [
    "shuup.admin.error_handlers:AdminPageErrorHandler",
    "shuup.front.error_handlers:FrontPageErrorHandler"
]

SHUUP_SIMPLE_SEARCH_LIMIT = 150

if os.environ.get("SHUUP_WORKBENCH_DISABLE_MIGRATIONS") == "1":
    from .utils import DisableMigrations
    MIGRATION_MODULES = DisableMigrations()
