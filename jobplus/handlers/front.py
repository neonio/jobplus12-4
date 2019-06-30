from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.forms import LoginForm, RegisterForm
from jobplus.models import User, Company, Job, UserRole
from flask_login import login_user, logout_user


front: Blueprint = Blueprint('front', __name__)


@front.route('/')
def index():
    jobs = Job.query.order_by(Job.update_at.desc()).limit(8).all()
    companys = Company.query.order_by(Company.update_at.desc()).limit(8).all()
    return render_template('index.html', companys=companys, jobs=jobs)


@front.route('/userregister/', methods=['GET', 'POST'])
def userregister():
    form = RegisterForm()
    form.name.label = "个人注册"
    if form.validate_on_submit():
        form.createUser(role=UserRole.USER)
        flash('注册成功, 请先登录', 'success')
        return redirect(url_for('front.login'))
    return render_template('userregister.html', form=form)


@front.route('/companyregister/', methods=['GET', 'POST'])
def companyregister():
    form = RegisterForm()
    form.name.label = "企业注册"
    if form.validate_on_submit():
        form.createUser(role=UserRole.COMPANY)
        flash('注册成功, 请先登录', 'success')
        return redirect(url_for('front.login'))
    return render_template('companyregister.html', form=form)


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
