from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from comunidade import app
from comunidade.forms import LoginForm, FormCriarConta

lista_usuarios = ["Lira", "Marcelo", "Joaquina", "Rafael", "Carla"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = LoginForm()
    form_criar_conta = FormCriarConta()
    if form_login.validate_on_submit() and "submit_login" in request.form:
        flash(
            f"Login feito com sucesso!\n Seja bem-vindo de volta {form_login.email.data}!",
            "alert-success",
        )
        return redirect(url_for("home"))

    if form_criar_conta.validate_on_submit() and "submit_conta" in request.form:
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
