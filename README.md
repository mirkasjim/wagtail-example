# Getting started with Lagoon & Wagtail

This is a simple example demonstrating how to get [Wagtail](https://wagtail.org/) running on [Lagoon](https://www.github.com/uselagoon/lagoon). 

The important files to examine are
* ./docker-compose.yml
* ./.lagoon.yml
* mysite/mysite/settings/base.py

*Please note this example is purely for demonstration and not suitable for production.*

## Getting Started

```
Open up a command line prompt.
Clone the repo.
cd into the repo.
Run docker-compose build.
Run docker-compose up -d.
```

## Included Services

This example contains the following services:
* Python 3.11
* Postgres 15

To see similar projects with additional services, please visit https://github.com/lagoon-examples and to find out more about the services, please visit the documentation at https://docs.lagoon.sh/lagoon

## Wagtail and uWSGI

This example utilises uWSGI with Wagtail. 

The Wagtail project is copied into the Dockerfile from the host, has its relevant dependencies installed and served via [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/#).

The Postgres database connection to the Wagtail project is defined via *mysite/mysite/settings/base.py* utilizing [dj_database_url](https://pypi.org/project/dj-database-url/).

