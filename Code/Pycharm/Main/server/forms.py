from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class UserCreateForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired(), Length(min=3, max=20)])
    userpw1 = PasswordField('PW', validators=[DataRequired()])
    userpw2 = PasswordField('PW CHECK', validators=[DataRequired(), EqualTo('userpw1', '비밀번호가 일치하지 않습니다.')])
    name = StringField('NAME', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('EMAIL', validators=[DataRequired(), Email()])
    phone = StringField('PHONE', validators=[DataRequired(), Length(min=7, max=16)])
