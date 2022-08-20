from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user 
from app.forms import Create_account, AddressForm, LoginForm
from app.models import User, Add_Contact



@app.route('/')
def index():
    addresses = Add_Contact.query.all()
    return render_template('index.html', addresses=addresses)

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

@app.route('/addcontact', methods=['GET', 'POST'])
@login_required 
def addcontact():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.first_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_contact = Add_Contact(first_name= first_name, last_name = last_name, phone_number = phone_number, address=address)
        flash(f"{new_contact.first_name} has been added to address book.")
        return redirect(url_for('index')) 
    return render_template('addcontact.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash("Welcome back {user.username}!", "success")
            return redirect(url_for('index'))

        else:
            flash('Bad username and/or password. Please try this again', 'danger')
            return redirect (url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You have now logged out. Thanks for stopping by, have a nice day!', 'primary')
    return redirect(url_for('index'))


@app.route('/addresses/<address_id>')
@login_required 
def view_address(address_id):
    address = Add_Contact.query.get_or_404(address_id)
    return render_template('address.html', address=address)


        














