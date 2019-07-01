from flask import Blueprint, render_template, flash, url_for, redirect, abort, request, current_app
from flask_login import login_required, current_user
from flask_sqlalchemy import Pagination
from jobplus.forms import CompanyProfileForm, JobForm
from jobplus.models import User, Job, UserRole, Company, db, Delivery
from jobplus.utils import getCurrentUser

company: Blueprint = Blueprint('company', __name__, url_prefix='/company')


@company.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    query = Company.query.filter(Company.role == UserRole.COMPANY.value)
    keyword = request.args.get('keyword') or request.form.get('keyword')
    if isinstance(keyword, str):
        keyword = keyword.strip()
    if keyword:
        query = query.filter(Company.role == UserRole.COMPANY.value and Company.name.contains(keyword))

    pagination = query.order_by(Company.update_at.desc()).paginate(
        page=page,
        per_page=12,
        error_out=False
    )
    return render_template('company/index.html', pagination=pagination, active='company')


@company.route('/<int:companyID>/admin/')
@login_required
def admin_index(companyID: int):
    companyObject: User = getCurrentUser()
    if not companyObject.is_admin and not companyObject.id == companyID:
        abort(404)
    page = request.args.get('page', default=1, type=int)
    pagination: Pagination = Job.query.filter_by(companyID=companyID).paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('company/admin_index.html', companyID=companyID, pagination=pagination)


@company.route('/<int:companyID>/admin/apply/')
@login_required
def admin_apply(companyID):
    userObject = getCurrentUser()
    if not userObject.is_admin and not userObject.id == companyID:
        abort(404)
    status = request.args.get('status','all')
    page = request.args.get('page', default=1, type=int)
    jobDelivery = Delivery.query.filter_by(companyID=companyID)
    if status == 'waiting':
        jobDelivery = jobDelivery.filter()


@company.route('/<int:companyID>/admin/publish_job/', methods=['GET', 'POST'])
@login_required
def admin_publish_job(companyID):
    if current_user.id != companyID:
        abort(404)
    form = JobForm()
    if form.validate_on_submit():
        form.create_job(current_user)
        flash('职位创建成功', 'success')
        return redirect(url_for('company.admin_index', companyID=current_user.id))
    return render_template('company/publish_job.html', form=form, companyID=companyID)


@company.route('/<int:companyID>/admin/jobs/<int:jobID>/delete/')
@login_required
def admin_delete_job(companyID, jobID):
    if current_user.id != companyID:
        abort(404)
    jobObject = Job.query.get_or_404(jobID)
    if jobObject.companyID != companyID:
        abort(404)
    db.session.delete(jobObject)
    db.session.commit()
    flash('职位删除成功', 'success')
    return redirect(url_for('company.admin_index', companyID=companyID))


@company.route('/<int:companyID>/admin/edit_job/<int:jobID>/', methods=['GET', 'POST'])
@login_required
def admin_edit_job(companyID, jobID):
    if current_user.id != companyID:
        abort(404)
    jobObject = Job.query.get_or_404(jobID)
    if jobObject.companyID != companyID:
        abort(404)
    form = JobForm(obj=jobObject)
    if form.validate_on_submit():
        form.update_job(jobObject)
        flash('职位更新成功', 'success')
        return redirect(url_for('company.admin_index', companyID=companyID))
    return render_template('company/edit_job.html', form=form, companyID=companyID, job=jobObject)


@company.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    companyObject = getCurrentUser()
    if not companyObject.is_company:
        flash('你不是企业用户', 'warning')
        return redirect(url_for('front.index'))

    form: CompanyProfileForm = CompanyProfileForm(obj=companyObject.detail)
    form.name.data = companyObject.name
    form.email.data = companyObject.email
    form.phone.data = companyObject.phone
    if form.validate_on_submit():
        form.updated_profile(companyObject)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)


@company.route('/<int:companyID>')
def detail(companyID):
    companyUser: Company = Company.query.get_or_404(companyID)
    return render_template('company/detail.html', company=companyUser, active='', panel='about')


@company.route('/<int:companyID>/jobs/')
def company_jobs(companyID):
    companyUser = Company.query.get_or_404(companyID)
    if not companyUser.is_company:
        abort(404)
    return render_template('company/detail.html', company=companyUser, active='', panel='job')
