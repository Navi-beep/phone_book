from app import app
from flask import render_template
from app.forms import RegisterForm



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regis', methods=["GET", "POST"])
def regis():
    form = RegisterForm()
    if form.validate_on_submit():
        print('Form is validated. NICE')
        name = form.name.data
        phone_number = form.phone_number.data
        address = form.address.data
    return render_template('regis.html', form=form)

