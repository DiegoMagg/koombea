# Koombea Challenge

[![codecov](https://codecov.io/gh/DiegoMagg/koombea/graph/badge.svg?token=S9242WZYHA)](https://codecov.io/gh/DiegoMagg/koombea)
![python](https://img.shields.io/badge/python-3.11-blue)

This repository is my solution proposal to a challenge given to me by [Koombea](https://www.koombea.com/) as part of interviewing process as a Back End Engineer.

## Tools used
- python 3.11
- pipenv
- django
- beautifulsoup
- requests
- jinja2
- tailwind
- postgres
- pytest
- pre-commit
- yapf


To help testing, this project is up and running at https://diegomagg.com.br until the end of the process.


## Testing:

1 - Go to the link above, click register. On the form provide an username and a password (requirement 1)

2 - After register click on back to Login and use the credentials to log in (requirement 2)

3 - After logging in, you will be redirected to the home page. Initially, no data will be displayed because there are no records linked to the user. (requirement 4)

4 - On the initial page, insert an url it need to be http or https like https://google.com

5 - The scrapper will grab the anchors from the page and you'll be able to see the results. (requirent 5 and 4)


## Nice to have
1 - Pagination

2 - Being processed page

## Observation

1 - The scrapper uses an initial version of the urls data and waits for the urls present on the page to be searched, if the request is unsuccessful, this object will be deleted and will not appear on the list page.


## Testing locally

### Requirements
 - Docker
 - Docker compose
 - Make (optional)


```bash
$ git clone git@github.com:DiegoMagg/koombea.git && cd koombea/app && pipenv install
```

Create a .env file inside the app folder with those environment variables:

```bash
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
ALLOWED_HOSTS=localhost
CSRF_TRUSTED_ORIGINS='http://localhost'
SECRET_KEY='y+*m(m4q-2y%xa9#i2=_bq9bvu_ka*toufahnyvc+5-x+dgemu'
```

note: this secret key was generated for local use only.


If you have make then:
``` bash
    $ make install
    $ make dev-server-up
```

This command will create a postgres instance, run the migrations and start the django devserver at http://localhost:8000

You you don't have make, then:

```bash
    $ docker compose -f databases.yml up -d
    $ cd app && pipenv install && pipenv run python manage.py migrate
    $ pipenv run python manage.py runserver 0:8000
```


Testing:

```bash
    $ make test
```
or

```bash
    $ docker compose -f databases.yml up -d
    $ cd app && pipenv run pytest
```
