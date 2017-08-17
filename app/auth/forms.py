from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')
# 登陆表单 p83

class RegistrationForm(Form):
    email=StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField('账号',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9]_.]*$',0,
                            '用户名必须只包含字母，数字或下划线，点')])
    password=PasswordField('密码',validators=[DataRequired(),EqualTo('password2',message='密码必须一致')])
    password2=PasswordField('确认密码',validators=[DataRequired()])
    submit=SubmitField('注册')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('注册邮件已经发送')
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在，你不能使用')