# Getting started with Lagoon & Wagtail

This is a simple example demonstrating how to get [Wagtail](https://wagtail.org/) running on [Lagoon](https://www.github.com/uselagoon/lagoon). 

The important files to examine are
* ./docker-compose.yml
* ./.lagoon.yml
* mysite/mysite/settings/base.py

*Please note this example is purely for demonstration and not suitable for production without some knowledge of Wagtail and Django.*

## Getting Started

* Open up a command line prompt.
* Clone the repo.
* cd into the repo.
* Run `docker-compose build` to build the containers
* Run `docker-compose up -d` to stand up the wagtail stack

You can interact with your site using `docker-compose exec python sh` and `/code/mysite/manage.py` to see the admin options for wagtail

## Included Services

This example contains the following services:
* Python 3.11
* PostgreSQL 15

To see similar projects with additional services, please visit https://github.com/lagoon-examples and to find out more about the services, please visit the documentation at https://docs.lagoon.sh/lagoon

## The `mysite` folder

The main wagtail project is inside the mysite folder - created using a `wagtail start mysite2` command. The only config modification from the standard installed version is the database stanza, which has been edited to refer to the PostgreSQL database connection in *mysite/mysite/settings/base.py* utilizing [dj_database_url](https://pypi.org/project/dj-database-url/) to read the `DATABASE_URL` created in the `.lagoon.env` file, which is populated in the docker container entrypoint.

```
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}
```

## Wagtail and uWSGI

This example utilises uWSGI with Wagtail. 

The Wagtail project is copied into the Dockerfile from the host, has its relevant dependencies installed and served via [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/#).

## Contributions

We welcome any contributions to our example projects - please feel free to raise an issue or pull request and we will work with you to improve!
