#from email.headerregistry import Address
from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import Create_account, AddressForm
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
def addcontact():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.first_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_contact = AddressForm(first_name= first_name, last_name = last_name, phone_number = phone_number, address=address)
        print(f"{new_contact.first_name} has been added to address book.")
        return redirect(url_for('index')) 
    return render_template('addcontact.html', form=form)











