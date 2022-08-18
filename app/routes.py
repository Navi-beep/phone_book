from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import Create_account
from app.models import User



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/createacct', methods=['GET', 'POST'])
def createacct():
    form = Create_account()
    if form.validate_on_submit():
        print('Form is validated. NICE')
        email = form.email.data
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash('A user with that username or email already exists!', 'danger')
            return redirect(url_for('createacct'))
        new_user = User(email=email, username=username, password=password)
        flash(f"{new_user.username} has been added to page!", "success")
        return redirect(url_for('index')) 
    return render_template('createacct.html', form=form)











