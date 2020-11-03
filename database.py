"""
    Author: Brett Larson
    Date: 11/01/2020

    Functionality:
        The database file acts as the server writing transaction data to the database.
"""

# Required Imports
import sys
import sqlite3
import json


def create_database_and_tables(database_name):
    """This function creates a database with tables to hold transaction data"""

    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            date text,
                            transaction_guid text,
                            name text,
                            card_number text,
                            exp_date text,
                            zip_code text,
                            purchase_amt real,
                            approval_status text,
                            approval_code text
                            )''')
        conn.commit()
        conn.close()

    except sqlite3.OperationalError:
        print(f"There was an error attempting to create the table. It is possible that the table"
              f" already exists. Please review and try again. The program will now exit.")
        conn.rollback()
        conn.close()
        sys.exit(1)


def write_transaction_data(transaction, database_name):
    """This function writes investment data to the database"""

    print(transaction)
    sql_insert_string = f"INSERT INTO transactions VALUES ('{transaction['current_date_time']}', " \
                        f"'{transaction['transaction_number']}', '{transaction['name']}', " \
                        f"'{transaction['card_number']}', '{transaction['exp_date']}', " \
                        f"'{transaction['zip_code']}', '{transaction['purchase_amt']}', " \
                        f"'{transaction['approval_status']}', '{transaction['authorization_code']}')"

    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()
        cursor.execute(sql_insert_string)
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        print(f"There was an error attempting to add data to the database. Please review "
              f"transaction data before continuing. The program will now exit.")
        conn.rollback()
        conn.close()
        sys.exit(1)
    except sqlite3.IntegrityError:
        print(f"Data you are attempting to add is invalid or not formatted properly. Please review "
              f"data. The program will now exit.")
        conn.rollback()
        conn.close()
        sys.exit(1)


def read_json_investment_data(filename):
    """This function opens the JSON file provided when the function is called
    :returns data set of the data from the JSON file
    """

    # Attempt to open the file provided and copy its contents into the data_set variable
    try:
        with open(filename) as json_file:
            data_set = json.load(json_file)

    except FileNotFoundError:
        print(f"WARNING: The file {filename} does not exist. Please confirm the file name and "
              f"location before trying again. The program will now exit.")
        json_file.close()
        sys.exit(1)

    json_file.close()
    return data_set
