from config import *

### Handlers ###

from views.index import index
app.register_blueprint(index)


from views.auth import auth
app.register_blueprint(auth, url_prefix="/auth")


'''
from views.trend import trend
app.register_blueprint(trend, url_prefix="/trend")

from views.admin import admin
app.register_blueprint(admin, url_prefix="/admin")

from views.city import city
app.register_blueprint(city, url_prefix="/city")

'''

if __name__ == '__main__': 
    app.debug = True
    app.run(host='0.0.0.0')
