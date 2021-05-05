from OfferGUI import db, login_manager
from OfferGUI import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

class static_costs_commissioning_tools(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class static_costs_installation_tools(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class static_costs_site_equipment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class static_costs_staff(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class static_costs_testing_tools(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class static_costs_travel_accommodation(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    service = db.Column(db.String())

class temp_staff_costs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Service = db.Column(db.String(length=30), nullable=False, unique=True)
    UnitPrice = db.Column(db.Integer(), nullable=False)
    RentalMode = db.Column(db.String(), nullable=False)
    RentalUnits = db.Column(db.String(), nullable=False)
    Remark = db.Column(db.String(length=60), nullable=False)
    Sum = db.Column(db.Integer(), nullable=False)
    # def __repr__(self):
    #     return f'staff_costs {self.name}'
    
class temp_tool_costs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    Service = db.Column(db.String(length=30), nullable=False, unique=True)
    UnitPrice = db.Column(db.Integer(), nullable=False)
    RentalMode = db.Column(db.String(), nullable=False)
    RentalPeriod = db.Column(db.String(), nullable=False)
    Remark = db.Column(db.String(length=60), nullable=False)
    Sum = db.Column(db.Integer(), nullable=False)
    # def __repr__(self):
    #     return f'staff_costs {self.name}'

class dropdown_elements(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    plant_type = db.Column(db.String())
    busbar = db.Column(db.String())
    calc_for = db.Column(db.String())
    yes_no = db.Column(db.String())
    languages = db.Column(db.String())
    #check database
    rental_mode = db.Column(db.String())
    # def __repr__(self):
    #     return f'dropdown_elements {self.name}'

class project_info(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    project_name = db.Column(db.String(), unique=True)
    project_manager_dept = db.Column(db.String())
    order_indicator = db.Column(db.String())
    site = db.Column(db.String())
    customer = db.Column(db.String())
    ## further info
    calc_for = db.Column(db.String())
    date = db.Column(db.String())
    cost_determination = db.Column(db.String())
    editor = db.Column(db.String())
    project_id = db.Column(db.String())
    ## plant info
    plant_type = db.Column(db.String())
    busbar = db.Column(db.String())
    number_of_bays = db.Column(db.Integer())
    # gascomp_empty = StringField(label='Gas compartments (empty)')
    # gascomp_pref = StringField(label='Gas compartments (prefilled)')
    # assembly_indoor = StringField(label='Assembly (indoor)')
    # assembly_outdoor = StringField(label='Assembly (outdoor)')
    # harting_plugs = StringField(label='Harting plugs')
    # ditec_seals = StringField(label='Ditec seals')
    # steel_supp_s = StringField(label='Steel support (small)')
    # steel_supp_m = StringField(label='Steel support (medium)')
    # steel_supp_l = StringField(label='Steel support (large)')
    # drives = StringField(label='Drives')
    # core_drilling = StringField(label='Core drillings')
    # converter = StringField(label='Converters')
    # outdoor_bushing= StringField(label='Outdoor bushings')
    # ## general info
    # workdays_per_week = IntegerField(label='Workdays per week')
    # hours_per_day = IntegerField(label='Hours per day')
    # number_of_site_manager = IntegerField(label='Number of site managers')
    # number_of_commissioning_engineers = IntegerField(label='Number of commissioning engineers')
    # transport_weeks_tools = IntegerField(label='Transport weeks for tools')
    # transport_weeks_HVTE = IntegerField(label='Transport weeks for HV-Test equipment')
    # arrival_departure_days = IntegerField(label='Arrival and departure days')
    # country_factor = IntegerField(label='Country factor')
    # customer_training_days = IntegerField(label='Customer training days')
    # # inquiry info
    # site_management = SelectField(u'Site management', coerce=str)
    # commissioning = SelectField(u'Commissioning', coerce=str)
    # manpower = SelectField(u'Manpower diagramm', coerce=str)
    # manpower_language = SelectField(u'Language', coerce=str)
    # tools = SelectField(u'Tools', coerce=str)
    # def __repr__(self):
    #     return f'project_info {self.name}'   