# REQUIRED SETTINGS FOR PYTHON ANYWHERE
# at PythonAnyWhere in a console, in the root of your app run:
# cp app/settings/pythonanywhere.local.py app/settings/local.py
# and edit the app/settings/local.py file to add your settings

# DJANGO SETTINGS
SECRET_KEY = "set-a-secret-key-in-production"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# WAGTAIL SETTINGS
WAGTAIL_SITE_NAME = "Your Site Name"

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
ALLOWED_HOSTS = ["your-domain.com"]

# DATABASE SETTINGS
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "db.host.com",
        "NAME": "db_name",
        "PORT": "db_port",
        "USER": "db_user",
        "PASSWORD": "db_password",
    }
}

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "host.com"
EMAIL_PORT = "1025"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = ""
