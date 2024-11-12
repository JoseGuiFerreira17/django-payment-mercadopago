from datetime import timedelta
from pathlib import Path
from os import environ

BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = environ.get("SECRET_KEY", default="^a-^xa(@")

DEBUG = bool(environ.get("DEBUG", default="False"))

DEV = bool(environ.get("DEV", default="False"))

ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", default="*").split(",")

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

THIRD_PART_APPS = [
    "django_filters",
    "drf_spectacular",
    "payments",
    "rest_framework",
    "rest_framework_simplejwt",
]

LOCAL_APPS = [
    "apps.core",
    "apps.accounts",
    "apps.payment",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

CACHE_TTL = 60 * 1

DATABASES = {
    "default": {
        "ENGINE": environ.get("DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": environ.get("DB_NAME", default="github-actions"),
        "USER": environ.get("DB_USER", default="postgres"),
        "PASSWORD": environ.get("DB_PASSWORD", default="postgres"),
        "HOST": environ.get("DB_HOST", default="localhost"),
        "PORT": environ.get("DB_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 8},
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# REST_FRAMEWORK
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        [
            "rest_framework_simplejwt.authentication.JWTAuthentication",
            "rest_framework.authentication.SessionAuthentication",
        ]
    ),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "ORDERING_PARAM": "order_by",
}

# SIMPLE_JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(
        minutes=int(environ.get("ACCESS_TOKEN_LIFETIME", default=5))
    ),
    "REFRESH_TOKEN_LIFETIME": timedelta(
        minutes=int(environ.get("REFRESH_TOKEN_LIFETIME", default=10))
    ),
    "TOKEN_OBTAIN_SERIALIZER": "apps.accounts.api.serializers.TokenObtainPairSerializer",
}

# PAYMENTS
PAYMENT_HOST = environ.get("PAYMENT_HOST", default="http://localhost:8000")

# SPECTACULAR
SPECTACULAR_SETTINGS = {
    "TITLE": "Doc. Django Payment API",
    "DESCRIPTION": "Documentação da API Django Payment",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
}

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = environ.get("STATIC_ROOT", default=BASE_DIR / "static/")

MEDIA_URL = "/media/"

MEDIA_ROOT = environ.get("MEDIA_ROOT", default=BASE_DIR / "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
