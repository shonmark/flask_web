from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from app.views import init_views
from app.app_api import init_api
from flask_nav import Nav
from app.views import login_manager
from flask_bcrypt import Bcrypt
from app.models import db
from flask_debugtoolbar import DebugToolbarExtension

nav = Nav()
bootstrap = Bootstrap()
csrf = CSRFProtect()
moment = Moment()
mail = Mail()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)
    app.debug = False
    csrf.init_app(app)  # csrf 跨站post保护
    # 必须先执行config再初始化数据库
    app.config.from_pyfile('config')
    db.init_app(app)
    # config[config_name].init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    init_views(app)
    init_api(app)
    bootstrap.init_app(app)
    nav.init_app(app)
    moment.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    toolbar = DebugToolbarExtension(app)
    return app
