from flask import Blueprint, render_template, redirect, url_for
from app.form_class import CertificateForm, WorkExperienceForm, TrainingWorkshopForm, ProjectForm
from app.model import db

port = Blueprint('portfolio', __name__)

@port.route('/port/<int:port_id>')
def portfolio(post_id):
    return render_template('port.html')

@port.route('/port/add', methods=["POST", "GET"])
def add_port():
    certificate_form = CertificateForm()
    work_experience_form = WorkExperienceForm()
    training_workshop_form = TrainingWorkshopForm()
    project_form = ProjectForm()
    return render_template("add_port.html",
                           certificate_form=certificate_form, 
                           work_experience_form=work_experience_form, 
                           training_workshop_form=training_workshop_form, 
                           project_form=project_form
                           )

@port.route('/port/delete/<int:port_id>')
def delete_port(post_id):
    return redirect(url_for('port.portfolio'))

@port.route('/port/update/<int:port_id>')
def update_port(post_id):
    return redirect(url_for('port.portfolio'))

@port.route('/img', subdomain="<int:img_url>")
def image_index(img_url):
    return img_url + ".your-domain.tld"
