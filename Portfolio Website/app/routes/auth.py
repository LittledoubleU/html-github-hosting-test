from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.model import User, db
from random import randint
from app.form_class import LogInForm, RegisterForm


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LogInForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user, remember=login_form.remember.data)
            return redirect(url_for('main.index'))
        else:
            flash("Opps. Wrong Username or Password!!! pls try again.")
    return render_template("login.html", form=login_form)
    
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
    
    
@auth.route("/signup", methods=['GET', 'POST'])
def sign_up():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        if user:
            flash('This email is already exist UwU... Go F*ck yourself or do somthing u idiot...')
            return redirect(url_for('auth.sign_up'))
        
        salt_length = randint(16, 32)
        hashed_password = generate_password_hash(
            password,
            method='pbkdf2:sha256:600000',
            salt_length=salt_length
            )
        
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
            )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template("signup.html", form=register_form)
    