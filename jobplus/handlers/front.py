from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.forms import LoginForm, RegisterForm
from jobplus.models import User
from flask_sqlalchemy import BaseQuery
from flask_login import login_user, logout_user
from enum import unique, Enum

front: Blueprint = Blueprint('front', __name__, url_prefix='/front')


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/userregister/', methods=['GET', 'POST'])
def userregister():
    form = RegisterForm()
    if form.validate_on_submit():
        form.createUser()
        flash('注册成功, 请先登录', 'success')
        return redirect(url_for('front.login'))
    return render_template('userregister.html', form=form)


@front.route('/companyregister/')
def companyregister():
    return "companyregister"


@front.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.first(email=form.email.data)
        login_user(user, remember=form.rememberMe.data)
        redirectRoute = 'user.profile'
        if user.is_admin:
            redirectRoute = 'admin.index'
        elif user.is_company:
            redirectRoute = 'company.profile'
        return redirect(url_for(redirectRoute))
    return render_template('login.html', form=form)


@front.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))
