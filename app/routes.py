from app import app
from flask import render_template
from app.forms import RegisterForm
from app.models import Contact



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regis', methods=["GET", "POST"])
def regis():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Form is validated. NICE')
        first_name=form.first_name.data
        last_name=form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
    return render_template('regis.html', form=form)

