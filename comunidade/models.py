from comunidade import database, login_manager
from datetime import datetime
from flask_login import UserMixin


# carregar login do usuario
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String(200), nullable=False, unique=True)
    password = database.Column(database.String(80), nullable=False)
    foto_perfil = database.Column(database.String, default="default.jpg")
    cursos = database.Column(
        database.String, nullable=False, default="Sem assuntos cadastrados"
    )
    posts = database.relationship("Post", backref="autor", lazy=True)

    def contar_posts(self):
        return len(self.posts)


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(
        database.DateTime, nullable=False, default=datetime.utcnow
    )
    id_usuario = database.Column(
        database.Integer, database.ForeignKey("usuario.id"), nullable=False
    )
