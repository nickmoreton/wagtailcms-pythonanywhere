# Python Anywhere paid account deployments

Deployment to paid accounts is a semi automated process.

- Push your code to a remote repository
- Run a deployment command

### Django management commands

| Command | Description |
| ------- | ----------- |
| `collectstatic` | Collect static at PythonAnywhere
| `migrate` | Migrate at PythonAnywhere

### Development utility commands

| Command | Description |
| ------- | ----------- |
| `db-shell` | SSH into MYSQL Docker Container
| `install-requirements` | Install requirements at PythonAnywhere
| `pip-list` | List requirements at PythonAnywhere
| `pull` | Pull from git at PythonAnywhere
| `pull-db` | Pull database from PythonAnywhere to development machine
| `pull-media` | Pull media from PythonAnywhere to development machine

### Deployment Commands

| Command | Description |
| ------- | ----------- |
| `deploy` | Deploy to PythonAnywhere
| `restart` | Restart web app at PythonAnywhere
| `ssh` | SSH into PythonAnywhere
| `mkvirtualenv` | Create a virtualenv at PythonAnywhere

To see all available commands run `fab -l` in your development console.
