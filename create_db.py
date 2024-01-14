from comunidade import app, database

# Importe seus modelos de dados aqui para que o SQLAlchemy os reconheça
from comunidade.models import Usuario, Post  # noqa: F401

# Crie o banco de dados com a função create_all()
with app.app_context():
    database.create_all()
