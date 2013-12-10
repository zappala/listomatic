# list-o-matic

A simple list application to demonstrate web development
concepts. Uses the Flask web development framework, with Twitter for
login, Bootstrap for styles, X-editable for inline editing, and
SQLAlchemy as an ORM.

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

## XSS, CSRF Vulnerabilities

Note, for teaching purposes you can modify `templates/index.html` so
that the search variable has the `safe` filter applied:

```
search|safe
```

This allows a XSS vulnerability in the code. An example showing this
would be to search for:

```
test+<script>alert('hello');</script>
```

In addition, the code is constructed so that it allows a CSRF
vulnerability. You can see this by loading `csrf.html` in a browser.

Note, neither of these attacks work with Chrome, but both work with
Firefox.

