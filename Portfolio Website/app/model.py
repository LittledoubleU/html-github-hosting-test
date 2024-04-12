from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from random import sample #Use with get_random_data

#make it easier to see which one is clarified as database method
db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    profile_picture_url = db.Column(db.String) #keep in url path
    created_at = db.Column(db.DateTime, default=func.now())
    bio = db.Column(db.Text)
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))
    
    def has_role(self, role_name):
        return any(role.name == role_name for role in self.roles)

#I have to manaully add role by adding session -.-
class Role(db.Model):
    __tablename__ = "role"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

#user_role table \(^o^)/ ~ ~ ~
user_roles = db.Table(
    'user_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Certificate(db.Model):
    __tablename__ = 'certificate'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    issuer = db.Column(db.String)
    date_issued = db.Column(db.String)
    images_associated = db.relationship("Image", backref="certificate")
    
# Define a WorkExperience class representing the work_experience table
class WorkExperience(db.Model):
    __tablename__ = 'work_experience'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    company = db.Column(db.String)
    description = db.Column(db.Text)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    images_associated = db.relationship("Image", backref="work_experience")

# Define a TrainingWorkshop class representing the training_workshops table
class TrainingWorkshop(db.Model):
    __tablename__ = 'training_workshops'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    organization = db.Column(db.String)
    description = db.Column(db.Text)
    date_attended = db.Column(db.String)
    images_associated = db.relationship("Image", backref="trainingworkshop")

# Define a Project class representing the projects table
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    images_associated = db.relationship("Image", backref="project")

# Define an Image class representing the images table
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable=False)
    
    certificate_id = db.Column(db.Integer, db.ForeignKey('certificate.id'))
    certificate_associated = db.relationship("Certificate", backref="images")
    
    work_experience_id = db.Column(db.Integer, db.ForeignKey('work_experience.id'))
    work_experience_associated = db.relationship("WorkExperience", backref="images")
    
    training_workshop_id = db.Column(db.Integer, db.ForeignKey('training_workshops.id'))
    training_workshop_associated = db.relationship("TrainingWorkshop", backref="images")
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    project_associated = db.relationship("Project", backref="images")
    
#get randomly amount of data to display uwu
def get_random_data(model, limit=5):
    # Retrieve all data from the table
    all_data = model.query.all()
    # Limit the data to a maximum of 5 records randomly
    return sample(all_data, min(limit, len(all_data)))