import socket

from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

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
