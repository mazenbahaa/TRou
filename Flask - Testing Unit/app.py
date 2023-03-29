from flask import Flask, render_template, redirect, request, url_for
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_manager, current_user
from flask_migrate import Migrate
from model.Manager import db, Manager, RegistrationForm, LoginForm
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mezo2022@localhost/TRou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret string'

db.init_app(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
csrf.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_Manager(Manager_id):
    return Manager.query.get(int(Manager_id))


@app.route('/', methods=['GET', 'POST'])
def register():
    if RegistrationForm().validate_on_submit():
        register_form = RegistrationForm()
        hashed_password = bcrypt.generate_password_hash(register_form.Password.data).decode('utf-8')
        manager = Manager(CompanyName=register_form.CompanyName.data, Location=register_form.Location.data,
                          Address=register_form.Address.data, Email=register_form.Email.data, Password=hashed_password)
        db.session.add(manager)
        db.session.commit()

        manager = Manager.query.filter_by(Email=RegistrationForm().Email.data).first()

        if manager and bcrypt.check_password_hash(manager.Password, RegistrationForm().Password.data):
            login_user(manager)
        return redirect(url_for('login'))
    return render_template('register.html', register_form=RegistrationForm())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if LoginForm().validate_on_submit():
        login_form = LoginForm()
        manager = Manager.query.filter_by(Email=login_form.Email.data).first()
        if manager and bcrypt.check_password_hash(manager.Password, login_form.Password.data):
            login_user(manager, remember=login_form.Remember.data)
        return redirect(url_for('dashboard'))
    return render_template('login.html', login_form=LoginForm())


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/user', methods=['GET', 'POST'])
def user():
    return render_template('user.html')


@app.route('/driver', methods=['GET', 'POST'])
def driver():
    return render_template('driver.html')


@app.route('/ride', methods=['GET', 'POST'])
def ride():
    return render_template('ride.html')


@app.route('/vehicle', methods=['GET', 'POST'])
def vehicle():
    return render_template('vehicle.html')


@app.route('/request', methods=['GET', 'POST'])
def request():
    return render_template('request.html')


@app.route('/report', methods=['GET', 'POST'])
def report():
    return render_template('report.html')


if __name__ == "__main__":
    app.run(debug=True)
