from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(100),)
    token = db.Column(db.String(100))
    secret = db.Column(db.String(100))

    def __init__(self,username,token,secret):
        self.username = username
        self.token = token
        self.secret = secret

    @staticmethod
    def get(username):
        return User.query.filter_by(username = username).first()
        
    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % (self.username)
