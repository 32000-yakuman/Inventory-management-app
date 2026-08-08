from .base import *

DEBUG = False

# 本番環境のドメインを入力
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app_product",
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

#CSRF_TRUSTED_ORIGINS = [ "https://example.com", ]

#本番環境はHTTPS
CSRF_COOKIE_SECURE = True 
SESSION_COOKIE_SECURE = True 

# JWT Cookie 
JWT_COOKIE_SECURE = True
JWT_COOKIE_SAMESITE = "None"