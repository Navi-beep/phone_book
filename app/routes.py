from app import app
from flask import render_template, redirect, url_for
from app.forms import RegisterForm
from app.models import Contact



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regis', methods=['GET', 'POST'])
def regis():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Form is validated. NICE')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        new_contact = Contact(first_name=first_name, last_name=last_name, phone_number = phone_number, address=address)
        print(f"{new_contact.first_name} has been added to address book.")
        return redirect(url_for('index')) 
    return render_template('regis.html', form=form)

