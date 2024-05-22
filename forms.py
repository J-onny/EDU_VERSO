from wtforms.fields import DateField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

  
class UserForm(FlaskForm):
    student_name = StringField('Student Name', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    class_name = StringField('Class', validators=[DataRequired()])
    school = StringField('School', validators=[DataRequired()])
    date_of_joining = DateField('Date of Joining', format='%Y-%m-%d', validators=[DataRequired()])




