from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, MultipleFileField, TextAreaField, DateTimeField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, Length, regexp

class LogInForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=4, max=15)], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)], render_kw={"class": "form-control"})
    remember = BooleanField('Remember Me', render_kw={"class": "form-check-input"})
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired(), Length(min=4, max=15)], render_kw={"class": "form-control"})
    email = StringField(label='Email', validators=[DataRequired(), Email("Invalid Email Address"), Length(min=4, max=15)], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)], render_kw={"class": "form-control"})
    submit = SubmitField('Sign Up' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class CertificateForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = CKEditorField(label='Description', validators=[DataRequired()], render_kw={"class": "form-control"})
    issuer = StringField(label='Issuer', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_issued = DateField(label='Date_Issuer', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class WorkExperienceForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()], render_kw={"class": "form-control"})
    company = StringField(label='Company', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = CKEditorField(label='Description', validators=[DataRequired()], render_kw={"class": "form-control"})
    start_date = DateField(label='Start Date', validators=[DataRequired()], render_kw={"class": "form-control"})
    end_date = DateField(label='End Date', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class TrainingWorkshopForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()], render_kw={"class": "form-control"})
    organization = StringField(label='Organization', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = CKEditorField(label='Description', validators=[DataRequired()], render_kw={"class": "form-control"})
    date_attended = DateField(label='Date Attended', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class ProjectForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()], render_kw={"class": "form-control"})
    description = CKEditorField(label='Description', validators=[DataRequired()], render_kw={"class": "form-control"})
    start_date = DateField(label='Start Date', validators=[DataRequired()], render_kw={"class": "form-control"})
    end_date = DateField(label='End Date', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})
    
class ImageForm(FlaskForm):
    image = MultipleFileField('Image File', validators=[regexp(r'^[^/\\]+\.jpg$')])
    description  = TextAreaField('Image Description')
    submit = SubmitField('Sign In' ,render_kw={"class": "btn btn-dark btn-black border-0 w-100 py-2 fw-semibold"})