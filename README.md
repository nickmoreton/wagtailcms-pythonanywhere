# Deploy Wagtail CMS to PythonAnywhere

The example site has been created using the official Wagtail [Build Your First Site](https://docs.wagtail.org/en/stable/getting_started/tutorial.html) guide.

You can develop it locally with the requirements below and if you have a paid PythonAnywhere account you can perform deployments over ssh.

*It's possible to deploy the site manually to PythonAnywhere with a free account but the Fabric commands won't work because ssh access to your account is required.*

## Requirements

Hosting:

- A free or paid for [PythonAnywhere](https://www.pythonanywhere.com) account (Hacker)
- Github / Gitlab or other version control repository (optional but recommended)

Development:

- Virtual environment (python3)
- [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)
- [Fabric](https://www.fabfile.org) as a tool to manage and deploy your website.

## Get Started

- [Setup a site at PA](./docs/pa_setup.md)

### Local development setup

- clone this repo
- create a virtual env
- install requirements
- run some setup Make commands
- run some management commands
- create a superuser
- install frontend 
- run npm commands

## Deployments

- [Deploy to a free PA account](./docs/free_account.md)
- [Deploy to a paid PA account](./docs/paid_account.md)

