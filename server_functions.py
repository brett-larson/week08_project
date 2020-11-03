"""

"""
import string
import random
from datetime import datetime
from database import *


def write_to_db(web_dict, vendor_dict):

    database_name = 'transactions.db'

    current_date_time = str(datetime.now())
    transaction_number = get_transaction_guid()
    web_dict.update(vendor_dict)
    web_dict['transaction_number'] = transaction_number
    web_dict['current_date_time'] = current_date_time
    print(web_dict)
    json_obj = json.dumps(web_dict)
    print(web_dict)
    write_transaction_data(web_dict, database_name)


def get_transaction_guid():
    """

    :return:
    """

    numbers = string.digits
    transaction_number = ''.join((random.choice(numbers) for i in range(10)))

    return transaction_number


def combine_dictionaries(web_dict, vendor_dict):
    """

    :param web_dict:
    :param vendor_dict:
    :return:
    """
    web_dict.update(vendor_dict)
    return web_dict
