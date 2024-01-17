from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
)
from comunidade import app, database, bcrypt
from comunidade.forms import LoginForm, FormCriarConta, FormEditarPerfil
from comunidade.models import Usuario
from PIL import Image
from flask_login import (
    login_user,
    logout_user,
    current_user,  # noqa: F401
    login_required,  # noqa: F401
)
import secrets
import os


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
            param_next = request.args.get("next")
            if param_next:
                return redirect(param_next)
            else:
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
@login_required
def usuarios():
    return render_template("usuarios.html", lista_usuarios=lista_usuarios)


@app.route("/contato")
def contato():
    return render_template("contato.html")


@app.route("/sair")
@login_required
def sair():
    logout_user()
    flash("Logout efetuado com sucesso!", "alert-success")
    return redirect(url_for("home"))


@app.route("/perfil")
@login_required
def perfil():
    foto_perfil = url_for(
        "static", filename="fotos_perfil/{}".format(current_user.foto_perfil)
    )
    return render_template("perfil.html", foto_perfil=foto_perfil)


@app.route("/post/criar")
@login_required
def criar_post():
    return render_template("criar_post.html")


# funcao para alterar e salvar a imagem
def salvar_imagem(imagem):
    # gerar nome aleatorio para a imagem
    codigo = secrets.token_hex(8)
    # pegar a extensao da imagem
    nome, extensao = os.path.splitext(imagem.filename)
    # juntar o nome e a extensao
    nome_arquivo = nome + codigo + extensao
    # criar o caminho da imagem
    caminho_imagem = os.path.join(app.root_path, "static/fotos_perfil", nome_arquivo)
    # redimensionar a imagem
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    # salvar a imagem
    imagem_reduzida.save(caminho_imagem)
    return nome_arquivo


# funcao para atualizar os cursos
def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if "curso_" in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return ";".join(lista_cursos)


@app.route("/perfil/editar", methods=["GET", "POST"])
@login_required
def editar_perfil():
    # criar o formulario
    form_editar_perfil = FormEditarPerfil()
    # validar o formulario
    if form_editar_perfil.validate_on_submit():
        # atualizar os dados do usuario
        current_user.email = form_editar_perfil.email.data
        current_user.username = form_editar_perfil.username.data
        # atualizar a foto de perfil
        if form_editar_perfil.foto_perfil.data:
            nome_imagem = salvar_imagem(form_editar_perfil.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        # atualizar os cursos
        current_user.cursos = atualizar_cursos(form_editar_perfil)
        # commitar no banco de dados
        database.session.commit()
        flash("Seu perfil foi atualizado com sucesso!", "alert-success")
        return redirect(url_for("perfil"))
    elif request.method == "GET":
        form_editar_perfil.email.data = current_user.email
        form_editar_perfil.username.data = current_user.username
    foto_perfil = url_for(
        "static", filename="fotos_perfil/{}".format(current_user.foto_perfil)
    )
    return render_template(
        "editar_perfil.html", foto_perfil=foto_perfil, form=form_editar_perfil
    )
