from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class PaymentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    card_number = StringField("Credit Card Number", validators=[DataRequired()])
    exp_date = StringField("Expiration Date", validators=[DataRequired()])
    zip_code = StringField("Zip Code", validators=[DataRequired()])
    purchase_amt = StringField("Purchase Amount", validators=[DataRequired()])
    submit = SubmitField("Submit")
