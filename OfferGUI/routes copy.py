from OfferGUI import app, db
from flask import render_template, redirect, request, url_for, flash, get_flashed_messages
from OfferGUI.models import User, staff_costs, dropdown_elements, project_info
import OfferGUI.xmltool
from OfferGUI.forms import RegisterForm, LoginForm, ProjectForm, SaveForm
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
import xmltodict
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template('home.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename)))
        filepath = os.path.join(app.config['UPLOAD_PATH'],secure_filename(f.filename))
        # print('file uploaded')
        return redirect(url_for('project_page', filepath=filepath))

@app.route('/project', methods=['GET', 'POST'])
@login_required
def project_page():
    save_form = SaveForm()
    form = ProjectForm()
    if request.method == 'GET':
        # class from from models-py
        dde = dropdown_elements
        # getting filepath from upload_file()
        filepath = request.args.get('filepath')
        # open xml-file in folder uploads
        with open(filepath) as fd:
            doc = xmltodict.parse(fd.read())
        # class from from models.py
        dde = dropdown_elements
        # reading from database
        db_user = User.query.with_entities(User.username, User.username).all()
        db_plant_type = dde.query.with_entities(dde.plant_type, dde.plant_type).filter(dde.plant_type!="NULL")
        db_busbar = dde.query.with_entities(dde.busbar, dde.busbar).filter(dde.busbar!="NULL")
        db_calc_for = dde.query.with_entities(dde.calc_for, dde.calc_for).filter(dde.calc_for!="NULL")
        db_yes_no = dde.query.with_entities(dde.yes_no, dde.yes_no).filter(dde.yes_no!="NULL")
        db_languages = dde.query.with_entities(dde.languages, dde.languages).filter(dde.languages!="NULL")
        # os.remove(filepath)
        # print('file removed')

        # setting choices (forms.py --> class ProjectForm)
        form.calc_for.choices = [k for k in db_calc_for]
        form.editor.choices = [k for k in db_user]
        form.plant_type.choices = [k for k in db_plant_type]
        form.busbar.choices = [k for k in db_busbar]
        form.commissioning.choices = [k for k in db_yes_no]
        form.site_management.choices = [k for k in db_yes_no]
        form.manpower.choices = [k for k in db_yes_no]
        form.manpower_language.choices = [k for k in db_languages]
        form.tools.choices = [k for k in db_yes_no]
        # setting data by imported xml-file (forms.py --> class ProjectForm)
        item = doc['form1']
        form.project_name.data = item['ProjektName']
        form.project_manager_dept.data = item['Vorname'] + " " + item['Nachname'] + " / " + item['Abteilung']
        form.site.data = item['TextField5'] + ", " + item['Projektland']
        form.calc_for.data = item['Angebot']
        form.number_of_bays.data = item['Anzahl']
        form.plant_type.data = item['Anlagentyp']
        form.editor.data = current_user.username
        form.busbar.data = item['SaS']
        form.site_management.data = item['Block1']['Bauleiter']
        form.commissioning.data = item['Block1']['IBSler']
        form.manpower.data = item['Block1']['MPD_2']
        form.manpower_language.data = item['Block1']['DropDownlist11']
        form.tools.data = item['Block2']['Werkzeug_2']

        return render_template('project_info.html', form=form, save_form=save_form)

    if request.method == 'POST':
        project_infos = project_info(project_name=form.project_name.data)
        db.session.add(project_infos)
        db.session.commit()
        return redirect(url_for('home_page'))





    #     if form.validate_on_submit():
    #         print('test')
    #         # project_infos = project_info(project_name=form.project_name.data)
    #         # db.session.add(project_infos)
    #         # db.session.commit()
    #         flash(f"Data from project page stored in database!", category='success')
    
    #     # return "test"#redirect(url_for('project_page'))
    # if form.errors != {}: #If there are not errors from the validations
    #     for err_msg in form.errors.values():
    #         flash(f'There was an error with creating a user: {err_msg}', category='danger')
    # # return render_template('project_info.html', form=form)

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