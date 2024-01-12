from flask import (
    Flask,
    render_template,
    url_for,
    request,
    flash,
    redirect,
)
from forms import LoginForm, FormCriarConta


app = Flask(__name__)
app.config["SECRET_KEY"] = "um-nome-bem-seguro"


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


if __name__ == "__main__":
    app.run(debug=True, port=5001)
