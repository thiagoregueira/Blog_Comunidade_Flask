from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    ValidationError,
)
from wtforms.validators import DataRequired, Email, Length, EqualTo
from comunidade.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField("Nome de usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    confirmacao = PasswordField(
        "Confirmar Senha", validators=[DataRequired(), EqualTo("password")]
    )
    submit_conta = SubmitField("Criar conta")

    # validacao de email
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado! Faça o Login para acessar!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6)])
    lembrar = BooleanField("Lembrar-me")
    submit_login = SubmitField("Login")


class FormEditarPerfil(FlaskForm):
    username = StringField("Nome de usuário", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])

    submit = SubmitField("Confirmar Alterações")
