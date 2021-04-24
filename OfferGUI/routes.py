from OfferGUI import app, db
from flask import render_template, redirect, request, url_for, flash, get_flashed_messages, send_from_directory
from OfferGUI.models import User, staff_costs
from OfferGUI.xmltool import xml_reader
from OfferGUI.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename
import os
import xmltodict
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
    item = {}
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename)))
        filepath = os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename))
        print('file uploaded')
        return redirect(url_for('project_page', filepath=filepath)) 

@app.route('/project', methods=['GET', 'POST'])
@login_required
def project_page():
    if request.method == 'GET':
        filepath = request.args.get('filepath', None)
        # print(filepath)
        with open(filepath) as fd:
            doc = xmltodict.parse(fd.read())
        item = doc['form1']['Projektland']
        os.remove(filepath)
        print('file removed')
        return render_template('project_info.html', item=item)

@app.route('/costs', methods=['POST', 'GET'])
@login_required

def costs_page():
    StaffCosts = staff_costs.query.all()
    return render_template('costs.html', StaffCosts=StaffCosts)

@app.route('/register', methods=['POST', 'GET'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'User and/or Password wrong! Try again', category='success')

    return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))




# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_files():
#     # item = []#request.args.get('item', None)
#     if request.method == 'POST':
#         f = request.files['file']
#         print(f.filename)
#         # f.save(os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename)))
#         # filepath = os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename))
#         print('file uploaded')
#         print(filepath)
#         with open(filepath) as fd:
#             doc = xmltodict.parse(fd.read())
#         item = doc['form1']
#         os.remove(filepath)
#         print('file removed')
    # return 'Success'#redirect(url_for('home_page'))#, item=item))
    # return render_template('home.html', item=item)

# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
#     print('file?')
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename)))
#         filepath = os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename))
#         print('file uploaded')
#         print(filepath)
#         with open(filepath) as fd:
#             doc = xmltodict.parse(fd.read())
#         item = doc['form1']
#         os.remove(filepath)
#         print('file removed')
#     return redirect(url_for('home_page', item=item))
        # return render_template('home.html', item=item)