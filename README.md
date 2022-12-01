# Deploy Wagtail CMS to pythonanywhere

This site has been generated form the official Wagtail getting started tutorial.

Branches:

- main: the very basics
- frontend: adds some style
- mysql: adds a mysql database

## Create a site in pythonanywhere

This pretty much follows a [guide](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject) available at pythonanywhere

General steps it follows:

- Upload your code to PythonAnywhere
- Set up a virtualenv and install Django and any other requirements
- Set up your web app using the manual config option
- Add any other setup (static files, environment variables etc)

### Upload your site to python anywhere

From the PA dashboard open a new console. Once open if you run `pwd` you should see the you are in your home/username folder. It doesn't really matter where you clone the repository to.

Clone this repository

```bash
git clone git@github.com:nickmoreton/wagtailcms-pythonanywhere.git
```

### Setup a virtual environment (best practice) and install python dependencies

**In the same console** run the following to create a virtual environment:

```bash
mkvirtualenv --python 3.10 wagtailcms-pythonanywhere
# the virtual env will be activated
```

**In the same console** Install the python dependencies and run the command to collect static files as well as creating a local.py settings file:

```bash
pip install -r wagtailcms-pythonanywhere/requirements.txt
python mysite/manage.py collectstatic --no-input
touch mysite/mysite/settings/local.py
```

You can exit and close this console for the moment.

### Set up your web app using the manual config option

From the dashboard click on the `web` tab and click `add new web app`. *You can add your own domain name here if you want to but the provided sub domain will work just as well, you can always add a new domain later and setup your DNS*.

- Click `next`
- Choose manual configuration
- Choose a python3 version
- Click `next`

After a few seconds you will see the web app configuration screen.

If you click on your domain name to view the site you should see the pythonanywhere generated Hello World page.

Add the following settings:

Code:
- Source code: Enter `wagtailcms-pythonanywhere` and click accept
- Open the wsgi file in the oneline editor by clicking the link

Delete the contents and add:

```python

```

Virtualenv:
- Add `wagtailcms-pythonanywhere` and accept

Static files:
- Url: `/static/` Directory: `wagtailcms-pythonanywhere/static`
- Url: `/media` Directory: `wagtailcms-pythonanywhere/media`


Example wsgi file

```python
import os
import sys

# if you don't put your app in your home directory then hard code the path.
project_folder = "you-absolute-app-folder-name"  # adjust as appropriate, e.g. /home/username/projectname

if project_folder not in sys.path:
    sys.path.append(project_folder)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.production")

application = get_wsgi_application()
```


# Order to play setup

```
make up
```
```
cp .env.example .env
```
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements-dev.txt 
```
```
make migrate
```
```
make superuser # admin/password
```
```
make run
```

Do some work with an empty site OR load from remote site

```
make pull-db
```

```
make pull-media
```
