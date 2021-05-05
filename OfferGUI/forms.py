from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from OfferGUI.models import User, project_info

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists!')

    username = StringField(label='User Name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password', validators=[Length(min=6, max=1000), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):

    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class ProjectForm(FlaskForm):
    '''
    #choices (represented by coerce) of selectfields in routes.py --> project_page

    '''
    def validate_project_name(self, project_name_to_check):
        project_name = project_info.query.filter_by(project_name=project_name_to_check.data).first()
        if project_name:
            raise ValidationError('Project name already exists!')

    def validate_project_id(self, project_id_to_check):
        project_id = project_info.query.filter_by(project_id=project_id_to_check.data).first()
        if project_id:
            raise ValidationError('Project ID already exists!')

    ## project info
    project_name = StringField(label='Project name')
    project_manager_dept = StringField(label='Project manager / department')
    order_indicator = StringField(label='Oder indicator')
    site = StringField(label='Site')
    customer = StringField(label='Customer')
    ## further info
    calc_for = SelectField(u'Calculation for', coerce=str, validators=[DataRequired()])
    date = DateField(label='Date', format='%Y-%m-%d')
    cost_determination = DateField(label='Cost determination until', format='%Y-%d-%m')
    editor = SelectField(u'Editor', coerce=str)
    project_id = StringField(label='Project ID', validators=[DataRequired()])
    ## plant info
    plant_type = SelectField(u'Plant type', coerce=str)
    busbar = SelectField(u'Busbar', coerce=str)
    number_of_bays = IntegerField(label='Number of bays')
    gascomp_empty = StringField(label='Gas compartments (empty)')
    gascomp_pref = StringField(label='Gas compartments (prefilled)')
    assembly_indoor = StringField(label='Assembly (indoor)')
    assembly_outdoor = StringField(label='Assembly (outdoor)')
    harting_plugs = StringField(label='Harting plugs')
    ditec_seals = StringField(label='Ditec seals')
    steel_supp_s = StringField(label='Steel support (small)')
    steel_supp_m = StringField(label='Steel support (medium)')
    steel_supp_l = StringField(label='Steel support (large)')
    drives = StringField(label='Drives')
    core_drilling = StringField(label='Core drillings')
    converter = StringField(label='Converters')
    outdoor_bushing= StringField(label='Outdoor bushings')
    ## general info
    workdays_per_week = IntegerField(label='Workdays per week')
    hours_per_day = IntegerField(label='Hours per day')
    number_of_site_manager = IntegerField(label='Number of site managers')
    number_of_commissioning_engineers = IntegerField(label='Number of commissioning engineers')
    transport_weeks_tools = IntegerField(label='Transport weeks for tools')
    transport_weeks_HVTE = IntegerField(label='Transport weeks for HV-Test equipment')
    arrival_departure_days = IntegerField(label='Arrival and departure days')
    country_factor = IntegerField(label='Country factor')
    customer_training_days = IntegerField(label='Customer training days')
    # inquiry info
    site_management = SelectField(u'Site management', coerce=str)
    commissioning = SelectField(u'Commissioning', coerce=str)
    manpower = SelectField(u'Manpower diagramm', coerce=str)
    manpower_language = SelectField(u'Language', coerce=str)
    tools = SelectField(u'Tools', coerce=str)
    psd_comm = SelectField(u'PSD Commissioning', coerce=str)
    hvt_pd_check = SelectField(u'HV-Test / PD-measurement', coerce=str)
    actas = SelectField(u'ACTAS', coerce=str)
    transports = SelectField(u'Transports', coerce=str)
    indoor_crane = SelectField(u'Indoor crane', coerce=str)
    protect_class_indoor= SelectField(u'Protection class indoor', coerce=str)
    protect_class_outdoor = SelectField(u'Protection class outdoor', coerce=str)
    earthing = SelectField(u'Earthing', coerce=str)
    sec_wiring = SelectField(u'Secondary wiring', coerce=str)
    submit = SubmitField(label='Save')
    
class SaveForm(FlaskForm):
    def validate_project_name(self, project_name_to_check):
        project_name = project_info.query.filter_by(project_name=project_name_to_check.data).first()
        if project_name:
            raise ValidationError('Project name already exists!')

    def validate_project_id(self, project_id_to_check):
        project_id = project_info.query.filter_by(project_id=project_id_to_check.data).first()
        if project_id:
            raise ValidationError('Project ID already exists!')
    # project_name = StringField(label='Project name')
    # project_id = StringField(label='Project ID', validators=[DataRequired()])

    submit = SubmitField(label='Save project!')

class StaffCostForm(FlaskForm):

    service = SelectField(u'Service', coerce=str)
    unitprice = IntegerField(label='Unit price')
    rentalmode = SelectField(u'Rental mode', coerce=str)
    rentalunits = IntegerField(label='Rental units')
    remark = StringField(label='Remark')

class InstallationToolsCostForm(FlaskForm):

    service = SelectField(u'Service', coerce=str)
    unitprice = IntegerField(label='Unit price')
    rentalmode = SelectField(u'Rental mode', coerce=str)
    rentalunits = IntegerField(label='Rental units')
    remark = StringField(label='Remark')