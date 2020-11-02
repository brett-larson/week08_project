"""

"""
import string
import random


def write_to_db(web_dict, vendor_dict):
    transaction_number = get_transaction_guid()
    combined_dict = combine_dictionaries(web_dict, vendor_dict)



def get_transaction_guid():
    """Create a GUID for each transaction
    :return: string transaction GUID
    """
    numbers = string.digits
    transaction_number = ''.join((random.choice(numbers) for i in range(10)))

    return transaction_number


def combine_dictionaries(web_dict, vendor_dict):
    web_dict.update(vendor_dict)
    web_dict[transaction_number] = transaction_number
    return web_dict
