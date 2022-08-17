from app import db
from datetime import datetime


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    address = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'<Address | {self.first_name}>'

    def __str__(self):
        return f""""
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Phone Number: {self.phone_number}
        Address: {self.address}
        """

    


