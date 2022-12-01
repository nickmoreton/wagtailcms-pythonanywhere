# Ansible secret variables

- `ansible_user` | your pythonanywhere user name
- `home` | home directory for your user
- `path` | path to your app
- `python` | path to the python virtual environment
- `repo` | url to your git repository
- `api_token` | your pythonanywhere api token
- `wsgi_path` | full absolute path to your apps wsgi file (.py)
- `mysql_host` | database host name
- `mysql_user` | database user name
- `mysql_password` | database password
- `mysql_db` | database name

The variable should be defined in /etc/ansible/hosts on your local computer for safe keeping.

**Don't directly include theses var in your development files or push them to your repo, especially if it's publicly available**

To encrypt the vars file you can use [ansible-vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html) if there is a possibility that other users could view the file.

## Sample vars (ini) file

```txt
[any-name-here]
ssh.pythonanywhere.com

[any-name-here:vars]
ansible_user=your-user-name
home=/home/{{ ansible_user }}
path={{ home }}/your-app-dir
python={{ home }}/.virtualenvs/your-virtualenv-name
repo=your-repo-web-url
api_token=your-pythonanywhere-api-token
wsgi_path=your-wsgi-file-path
mysql_host=mysql.host
mysql_user=user
mysql_password=your-mysql-password
mysql_db=user$app-name
```

