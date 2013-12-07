# listomatic

A simple list application to demonstrate web development concepts.

## Dependencies

- [Flask](http://flask.pocoo.org/)
- [Flask-Login](https://flask-login.readthedocs.org/en/latest/)
- [Flask-OAuth](http://pythonhosted.org/Flask-OAuth/)
- [Flask-SqlAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/)
- [SqlAlchemy](http://www.sqlalchemy.org/)
- [jQuery](http://jquery.com)
- [Bootstrap](https://flask-login.readthedocs.org/en/latest/)
- [X-editable](http://vitalets.github.io/x-editable/index.html)

## Installation

First install a few things through apt:

```
sudo apt-get install python-pip
sudo pip install virtualenv
```

Createa virtual environment:

```
mkdir ~/virtualenvs
virtualenv ~/virtualenvs/listomatic
source ~/virtualenvs/listomatic/bin/activate
```

Install Python requirements:

```
pip install -r requirements.txt
```

## Configuration

Copy the configuration file and setup a few important variables:

```
cp doc/config.py .
```

The `SECRET_KEY` is used for securing session state. Generate one
using a Python shell:

```
python
>>> import os
>>> os.urandom(24)
```

Copy this value into the SECRET KEY as a string. Next, create a new
application for Twitter sign-ons using their [developer
page](https://dev.twitter.com/apps).

Be sure to create a callback URL (even a fake one) and check the "Sign
in with Twitter" box. The Consumer key and Consumer secret listed here
should be copied into `TWITTER_KEY` and `TWITTER_SECRET` as strings.

## Run the app

```
python app.py
```

![Screenshot](/static/img/screenshot.png "Screenshot")
