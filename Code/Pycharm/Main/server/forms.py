from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# 회원가입 양식
class UserCreateForm(FlaskForm):
    userid = StringField('ID', validators=[DataRequired(), Length(min=3, max=20)])
    nickname = StringField('별명', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password', '비밀번호가 일치하지 않습니다.')])
    name = StringField('이름', validators=[DataRequired(), Length(min=2, max=8)])
    email = EmailField('EMAIL', validators=[DataRequired(), Email()])
    phone = StringField('PHONE', validators=[DataRequired(), Length(min=7, max=16)])

class UserPwForm(FlaskForm):
    password = PasswordField('변경할 비밀번호', validators=[DataRequired()])
    confirm_password = PasswordField('비밀번호 확인', validators=[DataRequired(), EqualTo('password', '비밀번호가 일치하지 않습니다.')])

