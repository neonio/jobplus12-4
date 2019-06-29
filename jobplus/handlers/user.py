from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from jobplus.forms import UserProfileForm

user: Blueprint = Blueprint('user', __name__, url_prefix='/user')


@user.route('/')
def index():
    redirect(url_for('user.profile'))


@user.route('/profile/', methods=['GET', 'POST'])
def profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_profile(current_user)
        flash('个人信息更新完成', 'success')
        return redirect(url_for('index'))
    return render_template('user/profile.html', form=form)
