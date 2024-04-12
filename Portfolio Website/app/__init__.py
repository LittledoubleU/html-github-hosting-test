from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from app.model import db, User
from app.routes import main, auth, portfolio

app = Flask(__name__, static_folder='static')

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

bootstrap = Bootstrap5(app)

#flask sql database
db.init_app(app)
#flask db init
#flask db migrate -m "migrate all database 1st time"
#flask db upgrade
#INFO  [alembic.runtime.migration] Running upgrade  -> " ", migrate all database 1st time
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# flask_login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

#curret_user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#flask blueprint
app.register_blueprint(main.main)
app.register_blueprint(auth.auth)
app.register_blueprint(portfolio.port)