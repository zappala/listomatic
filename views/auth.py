from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_oauth import OAuth
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required

from config import *
from models.user import *

# Login Setup

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


# OAuth Setup

oauth = OAuth()
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=TWITTER_KEY,
    consumer_secret=TWITTER_SECRET
)

auth = Blueprint('auth', __name__)

# Twitter

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        next_url = request.args.get('next') or url_for('index')
        return redirect(next_url)
    next_url=request.args.get('next') or request.referrer or None
    return twitter.authorize(callback=url_for('.oauth',
                                              next=next_url))

@auth.route('/oauth')
@twitter.authorized_handler
def oauth(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    user = User.get(resp['screen_name'])
    if user is None:
        user = User(resp['screen_name'], resp['oauth_token'], resp['oauth_token_secret'])
        db.session.add(user)
        db.session.commit()
        login_user(user)
        resp = twitter.get('/1.1/users/show.json?screen_name=' + user.username)
        print resp.status
        print resp.data
        if resp.status == 200:
            print resp.data['name']
            user.name = resp.data['name']
            db.session.add(user)
            db.session.commit()
    else:
        login_user(user)

    return redirect(next_url)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

@twitter.tokengetter
def get_twitter_token():
    if current_user.is_authenticated:
        return (current_user.token, current_user.secret)
    else:
        return None
