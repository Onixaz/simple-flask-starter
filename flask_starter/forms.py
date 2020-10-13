from wtforms.validators import DataRequired, Email, ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from .models import User


class UserForm(FlaskForm):
    """User form."""

    username = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exists!')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Email already exists!')
