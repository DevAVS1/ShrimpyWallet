from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

#Criando uma classe para cado objeto que eu quero construir

#Essa classe é uma subclasse de FlaskForm

#As validações de formulário que vão acontecer aqui são só para identificar se o campo foi preenchido corretamente,
#Nada de autenticação ainda

class FormCriarConta (FlaskForm):
    username = StringField('Nome de Usuário',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(),Email()])
    senha = PasswordField ('Senha', validators=[DataRequired()])
    confirmacao = PasswordField ('Confirme a sua senha',validators=[DataRequired(),EqualTo('senha')])
    submit_button_create = SubmitField ('Criar Conta')

class FormLogin (FlaskForm):
    email = StringField ('E-mail',validators=[DataRequired(), Email()])
    senha = PasswordField ('Senha',validators=[DataRequired(),Length(6,20)])
    submit_button_login = SubmitField ('Login')