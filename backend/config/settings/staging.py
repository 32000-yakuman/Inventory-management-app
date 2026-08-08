from .base import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_staging",
        "USER": "root",
        "PASSWORD": "hihuclub",
        "HOST": "app-db",
        "PORT": "3306",
        "OPTIONS": {
            "connect_timeout": 10,
            "ssl": {"ssl-mode": "DISABLED"},
        },
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
