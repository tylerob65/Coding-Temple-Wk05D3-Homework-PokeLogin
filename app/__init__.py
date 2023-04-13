from app.models import db, User
from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app,db)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view = 'loginPage'

# SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
# my_url = SITE_ROOT + "/static/pokedex.json"
# print(my_url)
# pokedex = json.load(open(my_url))
# g.pokedex = pokedex

from . import routes
from . import models


