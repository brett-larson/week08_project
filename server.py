import json

from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
from forms import PaymentForm
from credit_card_processor import *
from database import *
from server_functions import *

# Application Variables
database_name = 'transactions.db'

# Create the database
create_database_and_tables(database_name)

# Create the Flask web server application
app = Flask(__name__)

# Secret key required for utilizing Flask forms
app.config['SECRET_KEY'] = 'mysecretkey'


# Route for loading the homepage
@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


# Route for loading the payment complete page
@app.route('/approved', methods=['GET'])
def approved():
    return render_template('approved.html')


# Route for loading the payment complete page
@app.route('/declined', methods=['GET'])
def declined():
    return render_template('declined.html')


# Rout for loading the main payment page
@app.route('/payment', methods=['GET', 'POST'])
def payment():

    # Create the form for use within the payment webpage
    form = PaymentForm()

    # Logic used when the user clicks "Submit" on the payment page
    if form.validate_on_submit():
        form_data_dict = request.form.to_dict()
        json_data = json.dumps(form_data_dict)
        authorization = json.loads(authorize_transaction(json_data))
        write_to_db(form_data_dict, authorization)
        auth = authorization.get('approval_status')
        if auth == 'approve':
            return render_template('approved.html', json_string=authorization)
        elif auth == 'decline':
            return render_template('declined.html', json_string=authorization)

    # Provide the payment.html page and payment form with GET requests
    return render_template('payment.html', form=form)


if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True, port=4000)
