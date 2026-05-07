from flask_wtf import FlaskForm
from wtforms.fields import (StringField, PasswordField, IntegerField,
                            DateField, RadioField, SelectField,
                            SubmitField)


class RegisterForm(FlaskForm):
    username = StringField("Enter Username")
    password = PasswordField("Enter Password")
    confirm_password = PasswordField("Confirm Password")
    mobile = IntegerField()
    birthdate = DateField()
    gender = RadioField(choices=["Male", "Female", "I'm a mekanik"])
    country = SelectField(choices=["Choose Country", "Georgia", "USA", "Japan"])

    register = SubmitField("Register")

