import os
import subprocess
import sys
from datetime import datetime

from fabric import Connection
from invoke import run as local
from invoke import task

if os.path.exists(".env"):
    # get values from .env file
    # cp example.env .env to create your own .env file
    with open(".env", "r") as f:
        for line in f.readlines():
            if not line or line.startswith("#") or "=" not in line:
                continue
            var, value = line.strip().split("=", 1)
            os.environ.setdefault(var, value)


SSH_URL = os.environ["SSH_URL"]  # the ssh url of your python anywhere account
PYTHON_VERSION = os.environ[
    "PYTHON_VERSION"
]  # the python version your account supports
WSGI_FILE_PATH = os.environ["WSGI_FILE_PATH"]  # the path to your wsgi file
HOME_PATH = os.environ["HOME_PATH"]  # the path to your home directory
APP_NAME = os.environ["APP_NAME"]  # the name of your app
APP_PATH = f"{HOME_PATH}{APP_NAME}"
MEDIA_PATH = APP_PATH + "/media"

PA_MYSQL_USER = os.environ["PA_MYSQL_USER"]  # the mysql user
PA_MYSQL_PASSWORD = os.environ["PA_MYSQL_PASSWORD"]  # the mysql password
PA_MYSQL_DATABASE = os.environ["PA_MYSQL_DATABASE"]  # the mysql database
PA_MYSQL_HOST = os.environ["PA_MYSQL_HOST"]  # the mysql host

DEV_MYSQL_USER = os.environ["DEV_MYSQL_USER"]  # the mysql user
DEV_MYSQL_PASSWORD = os.environ["DEV_MYSQL_PASSWORD"]  # the mysql password
DEV_MYSQL_DATABASE = os.environ["DEV_MYSQL_DATABASE"]  # the mysql database
DEV_MYQL_HOST = os.environ["DEV_MYSQL_HOST"]  # the mysql host


connection = Connection(SSH_URL)


# def exec_db(c, cmd="bash"):
#     return local("docker-compose exec -T db " + cmd)


def out(line="", start="", end=""):
    sys.stdout.write(start + line + end)
    sys.stdout.flush()


def check_git(c):
    out("Checking git status", start="", end=":")
    r = local("git status", hide=True)
    if "nothing to commit, working tree clean" not in r.stdout:
        out(
            "You have un-committed changes. Commit them first.",
            start="\n  WARNING: ",
            end="\n",
        )
        sys.exit(1)
    elif "branch is ahead of" in r.stdout or "have diverged" in r.stdout:
        out("You have commits that are not pushed.", start="\n  WARNING: ", end="\n")
        sys.exit(1)
    else:
        out("OK", start=" ", end="\n")


def check_migrations(c):
    out("Checking for migrations", start="", end=":")
    try:
        result = local(
            "docker-compose exec -T app python manage.py makemigrations --check --dry-run",
            hide=True,
        )
        if "Run 'manage.py makemigrations' to make new migrations" in result.stdout:
            out(
                "You have model changes not reflected in migrations.",
                start="\n  WARNING: ",
                end="\n",
            )
            sys.exit(1)
        else:
            out("OK", start=" ", end="\n")
    except Exception as e:
        out("Exception: " + str(e), start="  WARNING: ", end="\n")
        out("You have migrations that are not applied.", start="  WARNING: ", end="\n")
        sys.exit(1)


def pip_cmd(c, cmd=None):
    """Run pip at PythonAnywhere"""
    if not cmd:
        with connection as c:
            c.run(f"workon {APP_NAME} && pip list")
    else:
        with connection as c:
            c.run(f"workon {APP_NAME} && pip {cmd}")


@task
def pip_list(c):
    """List requirements at PythonAnywhere"""
    out("Listing requirements", start="", end=":\n")
    pip_cmd(c)
    out("OK", start=" - ", end="\n\n")


@task
def mkvirtualenv(c):
    """Create virtualenv at PythonAnywhere"""
    out("Creating virtualenv", start="", end=":\n")
    with connection as c:
        c.run(f"mkvirtualenv {APP_NAME} -p python{PYTHON_VERSION}")
    out("OK", start="  ", end="\n")


@task
def ssh(c, command=""):
    """SSH into PythonAnywhere"""
    out("SSHing", start="", end=":\n")
    local(f"ssh {SSH_URL} bash -c {command}", pty=True)


@task
def install_requirements(c):
    """Install requirements at PythonAnywhere"""
    out("  Installing requirements", start="", end=": ")
    with connection as c:
        c.run(f"workon {APP_NAME} && pip install -r {APP_PATH}/requirements.txt")
    out("OK", start=" ", end="\n")


@task
def pull(c):
    """Pull from git at PythonAnywhere"""
    out("  Pulling repository at python anywhere", start="", end=":")
    with connection as c:
        c.run(
            f"cd {APP_PATH} && git fetch --all && git reset --hard origin/main",
            hide=True,
        )
    out("OK", start=" ", end="\n")


@task
def migrate(c):
    """Migrate at PythonAnywhere"""
    out("  Migrating", start="", end=": ")
    with connection as c:
        c.run(f"workon {APP_NAME} && cd {APP_PATH} && python manage.py migrate")
    out("OK", start="", end="\n\n")


@task
def collectstatic(c):
    """Collect static at PythonAnywhere"""
    out("Collecting static", start="", end=":")
    with connection as c:
        c.run(
            f"workon {APP_NAME} && cd {APP_PATH} && python manage.py collectstatic --noinput"
        )
    out("OK", start="", end="\n")


@task
def restart(c):
    """Restart app at PythonAnywhere"""
    out("Restarting", start="", end=":")
    with connection as c:
        c.run(f"touch {WSGI_FILE_PATH}")
    out("OK", start=" ", end="\n")


@task
def deploy(c):
    """Deploy at PythonAnywhere"""
    check_git(c)
    check_migrations(c)
    out("Deploying", start="", end=":\n")
    pull(c)
    install_requirements(c)
    migrate(c)
    collectstatic(c)
    restart(c)
    out("Deployment complete", end="\n")


# @task
# def get_wsgi(c):
#     """Copy wsgi file from PythonAnywhere to development machine"""
#     out("Pulling wsgi file", start="", end=":\n")
#     with connection as c:
#         c.get(WSGI_FILE_PATH, "prod.wsgi.py")
#     out("OK", start=" - ", end="\n\n")


# @task
# def put_wsgi(c):
#     """Copy wsgi file from development machine to PythonAnywhere"""
#     out("Pushing wsgi file", start="", end=":\n")
#     with connection as c:
#         c.put("prod.wsgi.py", WSGI_FILE_PATH)
#     out("OK", start=" - ", end="\n\n")


@task
def db_shell(c):
    """SSH into MYSQL Container"""
    subprocess.run(
        [
            "docker-compose",
            "exec",
            "db",
            "bash",
        ]
    )


def download_remote_db_backup(c, timestamp):
    dump_cmd = f"mysqldump -u {PA_MYSQL_USER} -p{PA_MYSQL_PASSWORD} -h {PA_MYSQL_HOST} '{PA_MYSQL_DATABASE}' \
        --set-gtid-purged=OFF --no-tablespaces --column-statistics=0 \
        > {HOME_PATH}pull_db_dumps/{APP_NAME}_{timestamp}.sql"
    get_source = f"{HOME_PATH}pull_db_dumps/{APP_NAME}_{timestamp}.sql"
    get_destination = f"database_dumps/{APP_NAME}_{timestamp}.sql"
    rm_cmd = f"rm {HOME_PATH}pull_db_dumps/{APP_NAME}_{timestamp}.sql"

    c.run(dump_cmd)
    c.get(get_source, get_destination)
    c.run(rm_cmd)


def destroy_local_db(c):
    subprocess.run(["docker-compose", "down", "-v"])


def create_local_db(c):
    subprocess.run(["docker-compose", "up", "-d"])


def remove_local_db_dump(timestamp):
    local(f"rm database_dumps/{APP_NAME}_{timestamp}.sql")


@task
def pull_db(c):
    """Pull database from PythonAnywhere to development machine"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with connection as c:
        download_remote_db_backup(c, timestamp)
        destroy_local_db(c)
        create_local_db(c)
        subprocess.run(
            [
                "docker-compose",
                "exec",
                "db",
                "bash",
                "-c",
                f"mysql -u {DEV_MYSQL_USER} -p{DEV_MYSQL_PASSWORD} {DEV_MYSQL_DATABASE} < /database_dumps/{APP_NAME}_{timestamp}.sql",
            ]
        )
        remove_local_db_dump(timestamp)


@task
def pull_media(c):
    """Pull media from PythonAnywhere to development machine"""
    # print(f"{SSH_URL}:{MEDIA_PATH}")
    # with connection as c:
    local("mkdir -p media")
    local(f"scp -r {SSH_URL}:{MEDIA_PATH}/ .")
