from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,  BooleanField, TextAreaField, PasswordField, validators, HiddenField, DateField, SelectField
from wtforms.fields import IntegerField
from wtforms.widgets import NumberInput
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User



class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    first_name = StringField(label='First Name:', validators=[Length(min=2, max=30), DataRequired()])
    last_name = StringField(label='Last Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')

class VacationRequestForm(FlaskForm):
    start_date = DateField('Start Date:', format='%Y-%m-%d')
    end_date = DateField('End Date:', format='%Y-%m-%d')
    work_days = IntegerField("Work Days: ", widget=NumberInput(min=1, max=20, step=1))
    reason = StringField(label='Reason:')
    comments = StringField(label='Comments:')
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')


