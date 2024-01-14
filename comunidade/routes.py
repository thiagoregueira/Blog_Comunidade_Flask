from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from comunidade import app, database, bcrypt
from comunidade.forms import LoginForm, FormCriarConta
from comunidade.models import Usuario
from flask_login import login_user, logout_user, current_user  # noqa: F401


lista_usuarios = ["Lira", "Marcelo", "Joaquina", "Rafael", "Carla"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = LoginForm()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and "submit_login" in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(
            usuario.password, form_login.password.data
        ):
            login_user(usuario, remember=form_login.lembrar.data)
            flash(
                f"Login feito com sucesso!\n Seja bem-vindo de volta {form_login.email.data}!",
                "alert-success",
            )
            return redirect(url_for("home"))
        else:
            flash("Email ou senha inválidos!", "alert-danger")

    if form_criar_conta.validate_on_submit() and "submit_conta" in request.form:
        # cryptografar senha
        senha_cryptografada = bcrypt.generate_password_hash(
            form_criar_conta.password.data
        )
        # criar usuario
        novo_usuario = Usuario(
            username=form_criar_conta.username.data,
            email=form_criar_conta.email.data,
            password=senha_cryptografada,
        )
        # adicionar sessao do usuario
        database.session.add(novo_usuario)

        # commitar no banco de dados
        database.session.commit()

        flash(
            f"Conta criada com sucesso!\n Seja bem-vindo {form_login.email.data}!",
            "alert-success",
        )
        return redirect(url_for("home"))

    return render_template(
        "login.html", form_login=form_login, form_criar_conta=form_criar_conta
    )


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/sair")
def sair():
    logout_user()
    flash("Logout efetuado com sucesso!", "alert-success")
    return redirect(url_for("home"))


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


@app.route("/post/criar")
def criar_post():
    return render_template("criar_post.html")
