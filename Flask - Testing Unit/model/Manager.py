from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import os

db = SQLAlchemy()


class Manager(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    CompanyName = db.Column(db.String(100), unique = True, nullable = False)
    Location = db.Column(db.String(40), nullable = False)
    Address = db.Column(db.String(150), nullable = False)
    Email = db.Column(db.String(120), unique = True, nullable = False)
    Password = db.Column(db.String(60), nullable = False)

class RegistrationForm(FlaskForm):
    CompanyName = StringField('CompanyName', validators = [DataRequired(), Length(min=4, max=100)])
    Location = StringField('Location', validators=[DataRequired(), Length(min=4, max=100)])
    Address = StringField('Address', validators=[DataRequired(), Length(min=4, max=100)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('SingUp')

class LoginForm(FlaskForm):
    Email = StringField('Email', validators = [DataRequired(), Email()])
    Password = PasswordField('Password', validators = [DataRequired()])
    Remember = BooleanField('Remember Me')
    submit = SubmitField('Login')