from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from OfferGUI.models import User

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
    ## project info
    project_name = StringField(label='Project name')
    project_manager_dept = StringField(label='Project manager / department')
    order_indicator = StringField(label='Oder indicator')
    site = StringField(label='Site')
    customer = StringField(label='Customer')
    ## further info
    calc_for = StringField(label='Calculation for')
    date = DateField(label='Date', format='%Y-%m-%d')
    cost_determination = DateField(label='Cost determination until', format='%Y-%d-%m')
    editor = SelectField(u'Editor', choices=[('choose...'),('Kermer'), ('Hesse'), ('Tran')])
    project_id = StringField(label='Project ID')
    ## plant info
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
    # = StringField(label='')
    submit = SubmitField(label='Save')