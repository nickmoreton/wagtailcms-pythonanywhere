# Create a site in your PythonAnywhere account

General steps this guide follows:

1. Clone your site code to PythonAnywhere (from a repo on github or another provider)
2. Set up a virtual environment and install the sites python dependencies
3. Set up your web app using the manual config option
4. Add any other setup (database, static and media files location)

*The official [getting start guide](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) is available at PythonAnywhere*

### Clone your site to PythonAnywhere account

From the PA dashboard open a new console. Once open if you run `pwd` you should see the you are in your home folder (/home/your-user-name). *You could create your site root folder in a different location if you prefer*.

### Clone this repository

```bash
git clone git@github.com:nickmoreton/wagtailcms-pythonanywhere.git
```

### Setup a virtual environment (recommended) and install python dependencies

In the same console run:

```bash
mkvirtualenv --python 3.10 your-virtualenv-name
```

Your newley create virtual environment should be activated already. You should see `(your-virtualenv-name)` in your console.

Now run:

```bash
pip install -r wagtailcms-pythonanywhere/requirements.txt
./manage.py collectstatic --no-input
cp app/settings/pythonanywhere.local.py local.py
```

You can exit and close this console for the moment.

### Set up your web app using the manual config option

From the Dashboard click on the `Web` tab and click the `Add new web app` button. *You can add your own domain name here if you want to but the provided sub domain will work just as well, you can always add a new domain later and setup your DNS*.

1. Click `next` and choose `manual configuration`
3. Choose a `python3` version and click `next`

After a few seconds you will see the web app configuration screen.

*If you click on your domain name to view the site you should see the PythonAnywhere generated Hello World page.*

Add the following settings:

**Code:**

- Source code: Enter `/home/your-user-name/your-site-root-folder` and click accept
- Open the WSGI configuration file in the online editor by clicking the link

Delete the contents and add:

```python
import os
import sys

path = "/home/your-user-name/your-site-root-folder"
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "app.settings.production"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Virtualenv:**

- Add `/home/you-user-name/.virtualenvs/your-virtualenv-name` and click accept

**Static files:**

- Url: `/static/` Directory: `/home/you-user-name/your-site-root-folder/static`
- Url: `/media` Directory: `/home/you-user-name/your-site-root-folder/media`

## Create a database in your PythonAnywhere account

It is possible to use sqlite3 as a database but the hosting setup isn't optimised for file based databases. It's recommended to use the provided free MYSQL database.

### Using MYSQL

From the Dashboard click on the `Databases` tab. Enter a name for your database and click on the `Create` button.

It's recommended to set a new password for your databases.

You will need to add your database settings to `/home/your-user-name/your-site-root-folder/app/settings/local.py`.

Create the settings file by running the following command from your `/home/your-user-name/your-site-root-folder`

```bash
cp app/settings/pythonanywhere.local.py app/settings/local.py
```

Return to the Dashboard and click on the `Files` tab. Then navigation to `your-site-root` folder `/app/settings` and open the `local.py` file in the editor.

Update the MYSQL Database settings to match your database settings from the Database tab.

## Update the other settings in local.py

There are a few other settings that will need to be updated in local.py add your own sites settings for:

```python
SECRET_KEY = "set-a-secret-key-in-production"
WAGTAIL_SITE_NAME = "Your Site Name"
WAGTAILADMIN_BASE_URL = "http://localhost:8000"
ALLOWED_HOSTS = ["your-domain.com"]
```

Save the changes and return to the `Web` tab in the Dashboard

Restart the server by clicking the `Reload` button.

You should be able to view your site in a browser using the domain provided or your own domain name.
