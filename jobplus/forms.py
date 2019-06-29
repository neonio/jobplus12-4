import os

from flask import url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, Field, ValidationError
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import Email, EqualTo, DataRequired, Length, NumberRange
from jobplus.models import User, db
from typing import List


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    rememberMe = BooleanField('记住我')
    submit = SubmitField('提交')

    # getattr(self.__class__, 'validate_%s' % name, None)
    def validate_email(self, field: Field):
        if field.data and not User.first(email=field.data):
            raise ValidationError('该邮箱未注册')

    def validate_password(self, field):
        user = User.first(email=self.email.data)
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')


class RegisterForm(FlaskForm):
    name = StringField('用户名', validators=[DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 24)])
    repeatPassword = PasswordField('重复密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self, field):
        if User.first(name=field.data):
            raise ValidationError('名字已经存在')

    def validate_email(self, field):
        if User.first(email=field.data):
            raise ValidationError('邮箱已经存在')

    def createUser(self):
        user = User.createFrom(name=self.name.data,
                               email=self.email.data,
                               password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class UserProfileForm(FlaskForm):
    real_name = StringField('姓名', [DataRequired(), Length(3, 24)])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码(不填写保持不变)')
    phone = StringField('手机号', validators=[Length(11)])
    work_years = IntegerField('工作年限', validators=[NumberRange(min=0)])
    resume = FileField('上传简历', validators=[FileRequired()])
    submit = SubmitField('提交')

    def validate_phone(self, field):
        phone = field.data
        if phone[:1] == '1':
            raise ValidationError('请输入有效的手机号')

    def upload_resume(self):
        f = self.resume.data
        filename = self.real_name.data + '.pdf'
        f.save(os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'static',
            'resumes',
            filename
        ))
        return filename

    def update_profile(self, user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        filename = self.upload_resume()
        user.resume_url = url_for('static', filename=os.path.join('resumes', filename))
        db.session.add(user)
        db.session.commit()
