ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
SECRET_KEY = "your_secret_key"

WAGTAIL_SITE_NAME = "My Site"
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = "mailhog"
EMAIL_PORT = "1025"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = ""

# MYSQL connection
# DATABASE_URL = "mysql://user:password@db:3306/app"

DATABASES = {
    # mysql connection
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "app",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "db",
        "PORT": "3306",
    }
}
