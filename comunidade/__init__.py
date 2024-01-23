from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "um-nome-bem-seguro"

if os.getenv("DATABASE_URL"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "alert-info"


# criar banco de dados postgresql no primeiro uso
from comunidade import models  # noqa: E402, F401

engine = sqlalchemy.create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print("Banco de dados criado com sucesso!")
else:
    print("Banco de dados ja existe!")

from comunidade import routes  # noqa: E402, F401
