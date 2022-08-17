from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone_number = StringField('Phone_Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField()


