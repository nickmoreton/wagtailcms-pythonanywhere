import socket

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DJANGO SETTINGS
SECRET_KEY = "set-a-secret-key-in-production"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# WAGTAIL SETTINGS
WAGTAIL_SITE_NAME = "Wagtail PA Ansible"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "db",
        "NAME": "app",
        "PORT": "3306",
        "USER": "user",
        "PASSWORD": "password",
    }
}

# DEBUG TOOL BAR
INSTALLED_APPS += ["debug_toolbar"]
INTERNAL_IPS = [
    "127.0.0.1",
]
# debug toolbar when developing with docker
ip = socket.gethostbyname(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1"]

try:
    from .local import *  # noqa
except ImportError:
    pass
