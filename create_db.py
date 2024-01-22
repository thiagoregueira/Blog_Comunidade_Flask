from comunidade import app, database  # noqa: F401

# Importe seus modelos de dados aqui para que o SQLAlchemy os reconheça
from comunidade.models import Usuario, Post  # noqa: F401

# Crie o banco de dados com a função create_all()
with app.app_context():
    database.create_all()

    # testando consultas ao banco de dados
    # usuario = Usuario.query.filter_by(email="thiago1@email.com").first()
    # print(usuario.cursos)

    # post = Post.query.first()
    # print(post.corpo)
