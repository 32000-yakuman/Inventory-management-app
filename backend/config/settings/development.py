from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_db",
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
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# 開発環境はｈｔｔｐ
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
]

# フロントとバックで同一ドメインを使うまで
JWT_COOKIE_SECURE = False
JWT_COOKIE_SAMESITE = "Lax"